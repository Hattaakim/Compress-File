from PySide6.QtWidgets import QAbstractItemView, QApplication, QFileDialog, QListWidgetItem, QMainWindow, QMessageBox, QListWidget
from PySide6.QtCore import QEvent, QObject, QStandardPaths, QTimer, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtNetwork import QLocalServer, QLocalSocket
import sys, os, math, shiboken6
from typing import Literal
from multiprocessing import Pool, cpu_count, Queue, Pipe, Process

######### Externally Managed Module #########
import backend, compressModule

######### Window ##########
from MainWindow import Ui_MainWindow

######### Global Const #########
APPID = "Compress Foto@hattaakim"

######### Internal Functions ##########
def showInfo(parent, judul:str, 
             pesan:str, 
             ikon:Literal["info", "warning", 
                          "error", "question"]):
    """Fungsi buat memunculkan dialog info pakai Qt"""
    ikonMap = {
        "info": QMessageBox.Icon.Information,
        "warning": QMessageBox.Icon.Warning,
        "error": QMessageBox.Icon.Critical,
        "question": QMessageBox.Icon.Question
    }
    msgBox = QMessageBox(parent)
    msgBox.setWindowTitle(judul)
    msgBox.setText(pesan)
    msgBox.setWindowModality(Qt.WindowModality.ApplicationModal)
    msgBox.setIcon(
        ikonMap.get(ikon, QMessageBox.Icon.Information)
    )
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    return msgBox.exec()

def makeStandardItem(text, alignment=Qt.AlignmentFlag.AlignCenter):
    item = QStandardItem(text)
    item.setTextAlignment(alignment)
    return item

def bringQuestion(parent, judul:str,
                  pesan:str, ikon:Literal["info", "warning",
                                          "error", "question"],
                                          tombol1:Literal["yes", "no"],
                                          tombol2:Literal["yes", "no"]):
    """Fungsi buat memunculkan dialog pertanyaan di QT"""
    ikonMap = {
        "info": QMessageBox.Icon.Information,
        "warning": QMessageBox.Icon.Warning,
        "error": QMessageBox.Icon.Critical,
        "question": QMessageBox.Icon.Question
    }
    tombolMap = {
        "yes": QMessageBox.StandardButton.Yes,
        "no": QMessageBox.StandardButton.No,
        "ok": QMessageBox.StandardButton.Ok
    }
    msgBox = QMessageBox(parent)
    msgBox.setWindowTitle(judul)
    msgBox.setText(pesan)
    msgBox.setWindowModality(Qt.WindowModality.ApplicationModal)
    msgBox.setIcon(
        ikonMap.get(ikon, QMessageBox.Icon.Information)
    )
    msgBox.setStandardButtons(
        tombolMap.get(tombol1) | tombolMap.get(tombol2)
    )
    return msgBox.exec()

def chooseFiles(parent, judul:str):
    """Buat memunculkan dialog file choose besar, khusus extension gambar"""
    downloadsPath = QStandardPaths.writableLocation(
        QStandardPaths.DownloadLocation
    )
    validExt = [".jpg", ".jpeg", ".png"]
    fileDlg = QFileDialog(parent)
    fileDlg.setWindowModality(Qt.WindowModality.ApplicationModal)
    selectedFile, _ = fileDlg.getOpenFileNames(
        parent,
        judul,
        downloadsPath,
    )
    if selectedFile:
        validFiles = [f for f in selectedFile
                      if os.path.splitext(f)[1].lower() in validExt]
        if validFiles:
            return validFiles
        return None
    return None

def chooseFolder(parent, judul:str):
    """Buat munculin dialog explorer memilih folder aja (file dihidden)"""
    downloadsPath = QStandardPaths.writableLocation(
        QStandardPaths.DownloadLocation
    )
    fileDlg = QFileDialog(parent)
    fileDlg.setWindowModality(Qt.WindowModality.ApplicationModal)
    folderPath = fileDlg.getExistingDirectory(
        parent,
        judul,
        downloadsPath,
        QFileDialog.Option.ShowDirsOnly
    )

    if folderPath:
        return folderPath
    return None

def humanReadableSize(fileSize):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    if fileSize == 0:
        return "0 B"

    i = min(int(math.log(fileSize, 1024)), len(units)-1)
    return f"{fileSize / (1024**i):.2f} {units[i]}"

######### Custom Filter For Qt6 Apps###########
class SingleInstance(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.server = None
        self.isRunning = False

        socket = QLocalSocket()
        socket.connectToServer(APPID)
        if socket.waitForConnected(100):
            socket.write(b"APP_ALREADY_RUNNING")
            socket.flush()
            socket.waitForBytesWritten(100)
            socket.disconnectFromServer()
            self.isRunning = True
            return

        self.server = QLocalServer()
        if not self.server.listen(APPID):
            self.isRunning = True
            return
        self.server.newConnection.connect(self.onNewInstanceResponse)

    def onNewInstanceResponse(self):
        conn = self.server.nextPendingConnection()
        if not conn:
            return
        conn.waitForReadyRead(100)
        data = bytes(
            conn.readAll()
        ).decode(errors="ignore")
        if data.strip() == "APP_ALREADY_RUNNING":
            window.showNormal()
            window.raise_()
            window.activateWindow()

    def cleanSocket(self):
        if self.server:
            self.server.removeServer(APPID)
            self.server.close()

class DropFilter(QObject):
    """Filter biar QTableView bisa accept drop, dengan fokus utama buat table dragndrop halaman pertama"""
    def __init__(self, tableview, tablemodel):
        super().__init__()
        self.table = tableview
        self.model = tablemodel

    def eventFilter(self, watched, event):
        if watched == self.table:
            if event.type() == QEvent.DragEnter:
                if event.mimeData().hasUrls():
                    event.acceptProposedAction()
                    return True

            elif event.type() == QEvent.Drop:
                fileSudahAda = [self.model.item(row,1).text()
                                for row in range(self.model.rowCount())]
                validExt = [".jpg", ".jpeg", ".png"]
                if event.mimeData().hasUrls():
                    for url in event.mimeData().urls():
                        filePath = url.toLocalFile()
                        if filePath not in fileSudahAda and os.path.isfile(filePath):
                            if os.path.splitext(filePath)[1].lower() in validExt:
                                self.model.appendRow(
                                    [makeStandardItem(os.path.basename(filePath)),
                                     makeStandardItem(filePath, alignment=Qt.AlignmentFlag.AlignLeft)]
                                )
                    event.acceptProposedAction()
                    return True
        return False

######### Window Class GUI #########
class JendelaUtama(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Kompres Gambar")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.stackedWidget.setCurrentIndex(0)

        ######### Const Global ##########
        self.allPages = {0: [self.stepOneNumber, self.stepOneTitle],
                         1: [self.stepTwoNumber, self.stepTwoTitle],
                         2: [self.stepThreeNumber, self.stepThreeTitle],
                         3: [self.stepFourNumber, self.stepFourTitle]}
        self.nowExitAble = True

        ######### INIT Code ##########
        self.initGUI()

        ######### Signal & Slots #########
        allPageSwitcher = list(self.allPages.keys())
        for key in allPageSwitcher:
            for n in range(len(self.allPages[key])):
                button = self.allPages[key][n]
                button.clicked.connect(self.pageSwitcher)

        ######### Variabel Halaman Pertama #########
        self.fileMode = 0 #### 1 = folder | 2 = file ####
        self.folderPath = None
        self.fileList = []
        """Mode folder 1, Mode file 2"""
        self.pageOneInteractable = {
            1: [self.folderBerisiFile, self.pilihFolderFile],
            2: [self.fileTable, self.tambahFile, self.hapusFile, self.resetTable]
        }
        self.pageOneOpsi = [self.opsiFolder, self.opsiFile]
        self.tableModel = QStandardItemModel(self)
        self.currentRowClicked = None
        self.tableDropFilter = DropFilter(self.fileTable, self.tableModel)
        self.fileTable.installEventFilter(self.tableDropFilter)

        ######## Signal & Slots Halaman Pertama ########
        self.firstPageGUI()
        self.opsiFolder.clicked.connect(self.firstPageOpsiFolder)
        self.opsiFile.clicked.connect(self.firstPageOpsiFile)
        self.pilihFolderFile.clicked.connect(self.pilihFolderFoto)
        self.tambahFile.clicked.connect(self.pilihFileFoto)
        self.hapusFile.clicked.connect(self.hapusFileFoto)
        self.resetTable.clicked.connect(self.resetTableData)
        self.pageOneLanjut.clicked.connect(self.continuePageOneVerify)

        ######## Variabel Halaman Kedua #########
        self.verifyTableModel = QStandardItemModel(self)
        self.pConn = None
        self.cConn = None
        self.p1 = None
        self.t1 = QTimer(self)
        self.t1.timeout.connect(self.getAllFile)
        self.verifyFileQueue = Queue()
        self.fileCount = 0
        self.doneVerify = 0
        self.pool = None
        self.t2 = QTimer(self)
        self.fileStatusMap = {
            1: "✔", 2: "✘"
        }

        ######## Signal & Slot Halaman Kedua #########
        self.startVerify.clicked.connect(self.verifyFile)
        self.pageTwoLanjut.clicked.connect(self.continuePageTwo)
        self.t2.timeout.connect(self.checkQueueVerifyFile)


        ######## Variabel Halaman Ketiga ##########
        self.pageThreeInteractable = [self.imgCompress, self.imgMpx,
                                      self.pilihFolder, self.hapusFIleAsli,
                                      self.pageThreeNext]
        self.qualityTip = []
        self.compressSummary = []
        self.verifiedFileDirPath = []
        self.allFileCategory = []
        self.saveDir = None

        ######## Signal & SLot Halaman Ketiga #######
        self.imgMpx.currentIndexChanged.connect(self.megaPixelChanged)
        self.imgMpx.currentIndexChanged.connect(self.ringkasanUpdater)
        self.imgCompress.valueChanged.connect(self.qualityChanged)
        self.imgCompress.valueChanged.connect(self.ringkasanUpdater)
        self.pilihFolder.clicked.connect(self.chooseSaveDir)
        self.dirTujuan.textChanged.connect(self.ringkasanUpdater)
        self.hapusFIleAsli.clicked.connect(self.deleteOriginalFile)
        self.hapusFIleAsli.checkStateChanged.connect(self.ringkasanUpdater)
        self.pageThreeNext.clicked.connect(self.continuePageThreeVerify)

        ####### Variabel Halaman Keempat ########
        self.preferredMaxPix = 0
        self.preferredQuality = 0
        self.compressionPenghematan:float = 0.00
        self.deleteOriFile = False
        self.doneCompress = 0
        self.compressTableModel = QStandardItemModel(self)
        self.uTimer = QTimer(self)
        self.compressTask = None
        self.compressTaskComms = Queue()
        self.fileToCompress = None

        ####### Signal & Slot Halaman Keempat ######
        self.uTimer.timeout.connect(self.checkCompressProgress)
        self.startCompression.clicked.connect(self.compressFotoParalell)

    def initGUI(self):
        """First boot, hanya opsi pertama yang muncul"""
        self.stackedWidget.setCurrentIndex(0)
        for key, pushButtonList in self.allPages.items():
            if key > 0:
                for pushButton in pushButtonList:
                    pushButton.setDisabled(True)

    def pageSwitcher(self):
        """Page Switcher supaya opsi di atas (nomor & title) bisa buat geser halaman"""
        senderButton = self.sender()
        for key, pushButtonList in self.allPages.items():
            if senderButton in pushButtonList:
                self.stackedWidget.setCurrentIndex(key)

    ######## First Page Only #########
    def firstPageGUI(self):
        """GUI Halaman pertama ketika dibuka"""
        for _, qtObjectList in self.pageOneInteractable.items():
            for qtObject in qtObjectList:
                qtObject.setDisabled(True)
        self.folderBerisiFile.setReadOnly(True)

    def firstPageOpsiFolder(self):
        """Simplenya ini mode folder"""
        for key, qtObjectList in self.pageOneInteractable.items():
            if key == 1:
                for qtObject in qtObjectList:
                    qtObject.setEnabled(True)

            elif key == 2:
                for qtObject in qtObjectList:
                    qtObject.setDisabled(True)
        self.fileMode = 1

    def pilihFolderFoto(self):
        """User pilih folder yang isinya foto"""
        folderFoto = chooseFolder(self, "Pilih Folder Foto Anda!")
        if folderFoto != None:
            self.folderPath = folderFoto
            self.folderBerisiFile.setText(self.folderPath)

        else:
            showInfo(self, "Perhatian",
                     "Anda belum memilih folder apapun!", "info")

    def firstPageOpsiFile(self):
        """Simplenya ini mode table"""
        for key, qtObjectList in self.pageOneInteractable.items():
            if key == 1:
                for qtObject in qtObjectList:
                    qtObject.setEnabled(False)

            elif key == 2:
                for qtObject in qtObjectList:
                    qtObject.setEnabled(True)

        if not self.fileTable.model():
            self.tableModel.setHorizontalHeaderLabels(
                ["Nama File", "Direktori"]
            )
            self.fileTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.fileTable.setModel(self.tableModel)
            self.fileTable.clicked.connect(self.onRowClicked)
            self.fileTable.setAcceptDrops(True)

        self.fileMode = 2

    def onRowClicked(self, index):
        """Respons ketika user klik pada row table, hendak menghapus"""
        self.currentRowClicked = index.row()

    def pilihFileFoto(self):
        """Ketika user mau pakai fitur pilih foto satu persatu alih-alih drag and drop"""
        fileSudahAda = [self.tableModel.item(row, 1).text()
                        for row in range(self.tableModel.rowCount())]
        files = chooseFiles(self, judul="Test")
        if files:
            for file in files:
                if file not in fileSudahAda and os.path.isfile(file):
                    self.tableModel.appendRow(
                        [makeStandardItem(os.path.basename(file)),
                         makeStandardItem(file, alignment=Qt.AlignmentFlag.AlignLeft)]
                    )

    def hapusFileFoto(self):
        """Supaya user bisa hapus data yang dia pilih di kolom"""
        if self.currentRowClicked != None:
            jawaban = bringQuestion(self, "Konfirmasi", "Yakin untuk menghapus kolom yang Anda pilih?",
                                    "question", "yes", "no")
            if jawaban == QMessageBox.Yes:
                self.tableModel.removeRow(self.currentRowClicked)
                self.currentRowClicked = None

            else:
                self.currentRowClicked = None
                self.fileTable.clearSelection()
                self.fileTable.clearFocus()
                pass
        else:
            showInfo(self, "Tidak Dipilih", "Anda belum memilih kolom data apapun untuk dihapus!",
                     "info")

    def resetTableData(self):
        """For reset table data function"""
        if self.tableModel.rowCount() > 0:
            jawaban = bringQuestion(self, "Area Berbahaya", "Yakin untuk menghapus seluruh kolom terisi?",
                                    "warning", "yes", "no")
            if jawaban == QMessageBox.Yes:
                self.tableModel.clear()
                self.tableModel.setHorizontalHeaderLabels(
                                ["Nama File", "Direktori"]
                            )
            else:
                pass

    def continuePageOneVerify(self):
        """verifikasi sebelum lanjut"""
        if self.fileMode != 0:
            if self.fileMode == 1:
                if self.folderPath != None and os.path.isdir(self.folderPath):
                    konfirmasi = bringQuestion(self, "Konfirmasi", 
                                               "Siap untuk melanjutkan? Data pada halaman sebelumnya akan menjadi baca-saja (tidak dapat diedit)",
                                               'question','yes','no')
                    if konfirmasi == QMessageBox.Yes:
                        self.continuePageOne()

                else:
                    showInfo(self, "Mode Folder: Kesalahan", 
                             "Jalur folder yang dituju belum dipilih atau tidak ada sama sekali. Silahkan lakukan verifikasi mandiri!",
                             'error')

            elif self.fileMode == 2:
                if self.tableModel.rowCount() > 0:
                    konfirmasi = bringQuestion(self, "Konfirmasi", 
                                               "Siap untuk melanjutkan? Data pada halaman sebelumnya akan menjadi baca-saja (tidak dapat diedit)",
                                               'question','yes','no')
                    if konfirmasi == QMessageBox.Yes:
                        self.continuePageOne()

                else:
                    showInfo(self, "Mode File: Kesalahan",
                             "Anda belum memasukkan file apapun ke dalam tabel file. Silahkan lakukan verifikasi mandiri!",
                             'error')

        else:
            showInfo(self, "Belum Dipilih",
                     "Anda belum memilih mode apapun. Silahkan pilih salah satu diantaranya!",
                     'info')

    def continuePageOne(self):
        for _, qtObjectList in self.pageOneInteractable.items():
            for qtObject in qtObjectList:
                qtObject.setDisabled(True)

        for chooseAble in self.pageOneOpsi:
            chooseAble.setDisabled(True)

        for key, buttonList in self.allPages.items():
            if key == 1:
                for button in buttonList:
                    button.setEnabled(True)

        self.pageOneLanjut.setDisabled(True)
        self.stackedWidget.setCurrentIndex(1)
        self.pageTwoInit()

    ###### Second Page Only #######
    def pageTwoInit(self):
        """Initialize Page Two so it's ready to use"""
        self.pageTwoLanjut.setDisabled(True)
        self.fileVerifyProgress.setText("Proses Verifikasi File Belum Dimulai!")
        if not self.tabelVerifikasi.model():
            self.verifyTableModel.setHorizontalHeaderLabels(
                ["Nama", "Ukuran", "Ekstensi File", "Format File", "File Didukung", "Integritas File", "File Aman", "Path File"]
            )
            self.tabelVerifikasi.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tabelVerifikasi.setModel(self.verifyTableModel)

        if self.fileMode == 1:
            self.pConn, self.cConn = Pipe()
            self.p1 = Process(
                target=backend.returnAllFileFromPath,
                args=(self.folderPath, self.cConn)
            )
            self.p1.start()
            self.t1.start(500)

        elif self.fileMode == 2:
            for row in range(self.tableModel.rowCount()):
                items = [makeStandardItem(self.tableModel.item(row,0).text())]
                items.extend(makeStandardItem("-") for _ in range(6))
                items.append(makeStandardItem(self.tableModel.item(row,1).text(), 
                                              alignment=Qt.AlignmentFlag.AlignLeft))
                self.verifyTableModel.appendRow(items)

    def getAllFile(self):
        """Subprocess for secondary thread check, comms, and terminate"""
        if self.pConn.poll():
            allFile = self.pConn.recv()
            self.t1.stop()
            self.pConn.close()
            if self.p1.is_alive():
                self.p1.kill()

            for pFile in allFile:
                ### REV 2
                items = [makeStandardItem(os.path.basename(pFile))]
                items.extend(makeStandardItem("-") for _ in range(6))
                items.append(makeStandardItem(pFile, 
                                              alignment=Qt.AlignmentFlag.AlignLeft))
                self.verifyTableModel.appendRow(items)

    def verifyFile(self):
        """Lakukan verifikasi secara async menggunakan multiprocessing pool"""
        self.startVerify.setDisabled(True)
        allNeedVerifyFile = [self.verifyTableModel.item(row, 7).text()
                         for row in range(self.verifyTableModel.rowCount())]
        self.fileCount = len(allNeedVerifyFile)
        self.doneVerify = 0
        self.verifyFileQueue = Queue()

        self.pool = Pool(processes=cpu_count()-2)
        for file in allNeedVerifyFile:
            self.pool.apply_async(backend.verifyImageFile, 
                                  args=(file,), callback=self.verifyFileQueue.put)
        self.pool.close()
        self.t2.start(100)

    def checkQueueVerifyFile(self):
        """Timer untuk mengecek proses verifikasi"""
        while not self.verifyFileQueue.empty():
            hasil = self.verifyFileQueue.get()
            namaFile, ukuranAwal, ekstensiFile, formatFile, dukunganFile, tidakCorrupt, bukanVirus = hasil
            for row in range(self.verifyTableModel.rowCount()):
                if self.verifyTableModel.item(row,0).text() == namaFile:
                    items = [
                        makeStandardItem(humanReadableSize(ukuranAwal)),
                        makeStandardItem(ekstensiFile),
                        makeStandardItem(formatFile),
                        makeStandardItem(self.fileStatusMap.get(dukunganFile, "?")),
                        makeStandardItem(self.fileStatusMap.get(tidakCorrupt, "?")),
                        makeStandardItem(self.fileStatusMap.get(bukanVirus, "?"))
                    ]
                    for col, item in enumerate(items, start=1):
                        self.verifyTableModel.setItem(row, col, item)
                    break
            self.doneVerify += 1
            self.fileVerifyProgress.setText(f"{self.doneVerify} dari {self.fileCount} File Telah Diproses")
            if self.doneVerify == self.fileCount:
                self.t2.stop()
                self.pageTwoLanjut.setEnabled(True)
    
    def continuePageTwo(self):
        """Lanjut menuju halaman selanjutnya (halaman 3)"""
        jawaban = bringQuestion(self, "Konfirmasi Untuk Melanjutkan",
                                "Apakah hasil verifikasi yang ditunjukkan oleh halaman ini sudah memenuhi ekspektasi Anda?\nFile tidak didukung, corrupt dan berpotensi mengandung virus tidak akan diikutsertakan untuk proses kompresi.",
                                "question", "yes", "no")
        if jawaban == QMessageBox.Yes:
            for key, pushButtonList in self.allPages.items():
                if key == 2:
                    for pushButton in pushButtonList:
                        pushButton.setEnabled(True)
            self.pageTwoLanjut.setDisabled(True)
            self.stackedWidget.setCurrentIndex(2)
            self.pageThreeInit()

    ###### Third Page Only #######
    def pageThreeInit(self):
        """Initialize page three supaya siap pakai"""
        self.verifiedFileDirPath = [os.path.dirname(self.verifyTableModel.item(row, 7).text())
                                    for row in range(self.verifyTableModel.rowCount())
                                    if self.verifyTableModel.item(row, 4).text()
                                    and self.verifyTableModel.item(row, 5).text()
                                    and self.verifyTableModel.item(row, 6).text() == "✔"]
        self.allFileCategory = sorted(set(
            [self.verifyTableModel.item(row, 3).text()
             for row in range(self.verifyTableModel.rowCount())]
        ))
        self.pageThreeNext.setDisabled(True)
        self.dirTujuan.setReadOnly(True)
        self.ringkasanUpdater()

    def megaPixelChanged(self, index):
        """Respons on mpx changed below 18mp (index 1)"""
        tips = "Resolusi dibawah 12mp mungkin menghasilkan gambar yang blur"
        if index > 1:
            if tips not in self.qualityTip:
                self.qualityTip.append(tips)
            self.qualityTipsUpdater()

        elif index <=1:
            if tips in self.qualityTip:
                self.qualityTip.remove(tips)
            self.qualityTipsUpdater()

    def qualityChanged(self, value):
        """Respons on quality changed below 70%"""
        tips = r"Kualitas dibawah 70% berdampak pada kualitas secara langsung"
        if value < 70:
            if tips not in self.qualityTip:
                self.qualityTip.append(tips)
            self.qualityTipsUpdater()

        elif value >= 70:
            if tips in self.qualityTip:
                self.qualityTip.remove(tips)
            self.qualityTipsUpdater()

    def qualityTipsUpdater(self):
        """Updating the tips below the settings"""
        baseText = "Saran:" if len(self.qualityTip) > 0 else "Saran: Semua terlihat baik!"
        for number, tip in enumerate(self.qualityTip, start=1):
            baseText += f"\n{number}. {tip}"
        self.compressionTips.setText(baseText)

    def chooseSaveDir(self):
        """Memilih folder tujuan dengan syarat folder tujuan tidak boleh sama dengan folder asal foto"""
        folderTujuan = chooseFolder(self, "Pilih Folder untuk menyimpan hasil")
        if folderTujuan:
            fileDirCategory = sorted(set(self.verifiedFileDirPath))
            if folderTujuan not in fileDirCategory:
                self.saveDir = folderTujuan
                self.dirTujuan.setText(self.saveDir)

            else:
                showInfo(self, "Kesalahan: Folder Sama",
                         "Maaf, Anda tidak diizinkan untuk menyimpan gambar hasil kompresi pada folder yang sama dengan gambar aslinya. Silahkan pilih folder yang lain!", 
                         "info")

    def deleteOriginalFile(self):
        """BERBAHAYA: Sistem menghapus file asli (original) setelah kompresi selesai"""
        if self.hapusFIleAsli.checkState() == Qt.CheckState.Checked:
            jawaban = bringQuestion(self, "Area Berbahaya", 
                                    "Apakah Anda yakin untuk menghapus file asli Anda setelah proses kompresi selesai (tidak direkomendasikan?\nFile asli yang akan dihapus adalah file yang telah diverifikasi.",
                                    "warning", "yes", "no")
            if jawaban == QMessageBox.Yes:
                showInfo(self, "Area Berbahaya", "File terverifikasi akan dihapus setelah proses kompresi selesai!", 'warning')
                self.hapusFIleAsli.setCheckState(Qt.CheckState.Checked)

            else:
                self.hapusFIleAsli.setCheckState(Qt.CheckState.Unchecked)

        else:
            self.hapusFIleAsli.setCheckState(Qt.CheckState.Unchecked)

    def ringkasanUpdater(self):
        """Fungsi untuk memperbarui ringkasan"""
        headerText = "Ringkasan Kompresi:"

        strukturSummary = [
            f"{len(self.verifiedFileDirPath)} dari {self.verifyTableModel.rowCount()} foto akan diproses",
            f"Foto yang diproses memiliki ekstensi {",".join(self.allFileCategory[:-1]) + " dan " + self.allFileCategory[-1] if len(self.allFileCategory) > 1 else self.allFileCategory[0]}",
            f"Hasil kompresi beresolusi {self.imgMpx.currentText()} dan mempertahankan {self.imgCompress.value()}% kualitas aslinya",
        ]
        if len(self.dirTujuan.text()) > 0:
            self.pageThreeInteractable[-1].setEnabled(True)
            strukturSummary.append(f"Hasil disimpan pada folder {self.dirTujuan.text()}")

        if self.hapusFIleAsli.checkState() == Qt.CheckState.Checked:
            strukturSummary.append("Foto asli akan dihapus setelah diproses untuk kompresi")

        for number, summaryCategory in enumerate(strukturSummary, 1):
            headerText += f"\n{number}. {summaryCategory}"
        self.dataSummary.setText(headerText)

    def continuePageThreeVerify(self):
        """Lanjut menuju halaman terakhir (halaman 4)"""
        if len(self.dirTujuan.text()) > 0:
            if not os.path.isdir(self.dirTujuan.text()):
                os.makedirs(self.dirTujuan.text(), exist_ok=True)
            for qObject in self.pageThreeInteractable:
                qObject.setDisabled(True)
            self.continuePageThree()

        else:
            showInfo(self, "Ups! Ada yang Dilupakan", 
                     "Anda belum memilih lokasi penyimpanan (folder) untuk menyimpan file hasil kompresi. Silahkan pilih lokasinya terlebih dahulu!",
                     'error')

    def continuePageThree(self):
        """Trigger untuk menuju halaman terakhir"""
        for key, pushButtonList in self.allPages.items():
            if key == 3:
                for pushButton in pushButtonList:
                    pushButton.setEnabled(True)
        self.stackedWidget.setCurrentIndex(3)
        self.pageForthInit()

    ##### Forth (Last) Page Only #####
    def pageForthInit(self):
        """Fungsi untuk mempersiapkan halaman terakhir"""
        if not self.fileCompressionTable.model():
            self.compressTableModel.setHorizontalHeaderLabels(
                ["Nama File", "Size Awal", "Size Akhir", "Dihemat", "Status", "Disimpan Di", "Dihapus"]
            )
            self.fileCompressionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            self.fileCompressionTable.setModel(self.compressTableModel)

        self.fileToCompress = [self.verifyTableModel.item(row, 7).text()
                                for row in range(self.verifyTableModel.rowCount())
                                if self.verifyTableModel.item(row, 4).text()
                                and self.verifyTableModel.item(row, 5).text()
                                and self.verifyTableModel.item(row, 6).text() == "✔"]

        self.preferredMaxPix = int("".join([char for char in self.imgMpx.currentText() if char.isdigit()]))*100000
        self.preferredQuality = self.imgCompress.value()
        self.deleteOriFile = True if self.hapusFIleAsli.checkState() == Qt.CheckState.Checked else False

        #elf.fileCompressionProgress.setText(f"0 dari {len(self.fileToCompress)} foto telah diproses")
        for index in range(len(self.fileToCompress)):
            items = [makeStandardItem(os.path.basename(self.fileToCompress[index])),
                     makeStandardItem(self.verifyTableModel.item(index,1).text()),]
            items.extend(makeStandardItem("-") for _ in range(5))
            self.compressTableModel.appendRow(items)

    def compressFotoParalell(self):
        """Proses parallel untuk kompres gambar"""
        jawaban = bringQuestion(self, "Konfirmasi: Proses Kompresi",
                                "Apakah Anda yakin ingin memulai proses kompresi? Proses tidak dapat dihentikan, sehingga Anda tidak dapat menutup aplikasi ini demi mencegah kegagalan sistem.",
                                "question", 'yes', 'no')
        if jawaban == QMessageBox.Yes:
            self.nowExitAble = False
            self.startCompression.setDisabled(True)
            self.compressTask = Pool(processes=cpu_count()-2)
            for fDir in self.fileToCompress:
                self.compressTask.apply_async(compressModule.compressImage,
                                        args=(fDir, self.saveDir, self.preferredMaxPix, self.preferredQuality, self.deleteOriFile),
                                        callback=self.compressTaskComms.put)
            self.compressTask.close()
            self.uTimer.start(100)

    def checkCompressProgress(self):
        """Fungsi untuk mengecek proses verifikasi"""
        while not self.compressTaskComms.empty():
            hasil = self.compressTaskComms.get()
            namaFile, fileSizeAkhir, penghematanSize, statCompress, outPath, statDelete = hasil
            for row in range(self.compressTableModel.rowCount()):
                if self.compressTableModel.item(row, 0).text() == namaFile:
                    items = [
                        makeStandardItem(humanReadableSize(fileSizeAkhir)),
                        makeStandardItem(humanReadableSize(penghematanSize)),
                        makeStandardItem(self.fileStatusMap.get(statCompress, "-")),
                        makeStandardItem(outPath, alignment=Qt.AlignmentFlag.AlignLeft),
                        makeStandardItem(self.fileStatusMap.get(statDelete, "-"))
                    ]
                    self.compressionPenghematan += penghematanSize
                    for col, item in enumerate(items, 2):
                        self.compressTableModel.setItem(row, col, item)
                    break
            self.doneCompress +=1
            self.fileCompressionProgress.setText(f"{self.doneCompress} dari {len(self.fileToCompress)} foto telah diproses")
            if self.doneCompress == len(self.fileToCompress):
                self.uTimer.stop()
                self.nowExitAble = True
                self.fileCompressionProgress.setText(f"Semua proses selesai. Anda berhasil menghemat {humanReadableSize(self.compressionPenghematan)}")

    def closeEvent(self, event):
        """Preventing user for accidently closing application"""
        if self.nowExitAble:
            jawaban = bringQuestion(self, "Keluar Aplikasi?", "Apakah Anda yakin ingin keluar dari aplikasi?",
                                    ikon="question", tombol1="yes", tombol2="no")
            if jawaban == QMessageBox.StandardButton.Yes:
                app.cleanSocket()
                event.accept()

            else:
                event.ignore()

        else:
            showInfo(self, "Penutupan Aplikasi: Ditolak!",
                     "Sistem sedang menolak penutupan aplikasi secara keseluruhan karena ada proses berat yang sedang berjalan. Harap coba lagi ketika proses sudah selesai!",
                     'error')
            event.ignore()

if __name__ == "__main__":
    app = SingleInstance(sys.argv)
    if app.isRunning:
        showInfo(None, "Informasi", 
                 "Aplikasi sudah berjalan di perangkat Anda. Silahkan cek kembali!", 'info')
        sys.exit(0)

    else:
        window = JendelaUtama()
        window.show()
        app.exec()