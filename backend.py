import os
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PIL import Image

class fileDatabase:
    def __init__(self):
        self.fileDatabase = QSqlDatabase.addDatabase("QSQLITE")
        self.fileDatabase.setDatabaseName(":memory:")
        self.fileDatabase.open()

        self.dbQuery = QSqlQuery(db=self.fileDatabase)
        self.qCreateTable = [
"""CREATE TABLE IF NOT EXISTS fileTable(
id INTEGER PRIMARY KEY,
fileName TEXT NOT NULL,
fileDir TEXT NOT NULL)""",

"""CREATE TABLE IF NOT EXISTS fileVerify(
id INTEGER PRIMARY KEY,
fileName TEXT,
fileExt TEXT DEFAULT '-',
fileFormat TEXT DEFAULT '-',
fileSize FLOAT DEFAULT 0.00,
isSupported INTEGER DEFAULT 0,
isNotCorrupted INTEGER DEFAULT 0,
isNotVirus INTEGER DEFAULT 0,
filePath TEXT)""",

"""CREATE TABLE IF NOT EXISTS fileProcess(
id INTEGER PRIMARY KEY,
fileName TEXT,
fileStatus INTEGER DEFAULT 0,
fileSize0 FLOAT DEFAULT 0.00,
fileSize1 FLOAT DEFAULT 0.00,
sizeReduced FLOAT DEFAULT 0.00,
fileSavePath TEXT DEFAULT '-',
fileDeleted INTEGER DEFAULT 0)""",

"""CREATE TRIGGER IF NOT EXISTS fileDir_Inserted
AFTER INSERT ON fileTable
BEGIN
    INSERT INTO fileVerify(fileName, filePath)
    VALUES (NEW.fileName, NEW.fileDir);
END;""",

"""CREATE TRIGGER IF NOT EXISTS fileVerify_Inserted
AFTER INSERT ON fileVerify
BEGIN
    INSERT INTO fileProcess(fileName)
    VALUES (NEW.fileName);
END;""",

"""CREATE TRIGGER IF NOT EXISTS fileVerify_SizeUpdated
AFTER UPDATE OF fileSize on fileVerify
BEGIN
    UPDATE fileProcess
    SET fileSize0 = NEW.fileSize
    WHERE fileName = NEW.fileName;
END;"""
        ]
        for qSql in self.qCreateTable:
            self.dbQuery.exec(qSql)
        print(self.dbQuery.lastError().text())

    def runQuery(self, querySQL, params=None, fetch=False):
        """params for VALUES (?,?) and FETCH for return data"""
        self.dbQuery.prepare(querySQL)
        if params:
            for param in params:
                self.dbQuery.addBindValue(param)

        if not self.dbQuery.exec():
            raise Exception(f"QSqlError: {self.dbQuery.lastError().text()}")

        if fetch:
            hasil = []
            while self.dbQuery.next():
                row = tuple(self.dbQuery.value(i)
                            for i in range(self.dbQuery.record().count()))
                hasil.append(row)
            return hasil
        else:
            return True

def verifyImageFile(filePath):
    """return nama file, ukuran awal, ekstensi file, format file, dukungan, tidak corrupt, bukan virus (0 uncheck 1 true 2 false)"""
    namaFile = ""
    ukuranAwal = 0
    ekstensiFile = "!"
    formatFile = "!"
    dukunganFile = 0
    tidakCorrupt = 0
    bukanVirus = 0

    ###### Constant ######
    supportedExtension = ['.jpg', '.jpeg', '.png', '.webp', 'mpo', '.heic', '.heif']
    supportedFormat = ['JPG', 'JPEG', 'PNG', 'WEBP', 'MPO', 'HEIC', 'HEIF']

    ###### First Step adalah Cek Nama dan Ukuran File ######
    namaFile = os.path.basename(filePath)
    ukuranAwal = os.path.getsize(filePath)

    try:
        imgPtr = Image.open(filePath)
        imgFormat = imgPtr.format

        ###### Second Step adalah PIL.Image.Load() dengan .verify() #######
        imgPtr.verify()
        if imgPtr:
            imgPtr.close()
        tidakCorrupt = 1

        imgPtr = Image.open(filePath)
        imgPtr.load()
        bukanVirus = 1

        ###### Third Step adalah cek Format gambar ######
        fExtension = os.path.splitext(filePath)[1].lower()
        if fExtension in supportedExtension:
            if imgFormat in supportedFormat:
                ekstensiFile = fExtension
                formatFile = imgFormat
                dukunganFile = 1

            else:
                formatFile = "✗ (Tidak Didukung)"
        else:
            ekstensiFile = "✗ (Tidak Didukung)"

    except (IOError, SyntaxError) as e:
        tidakCorrupt = 2

    except (Image.DecompressionBombWarning, Image.DecompressionBombError) as e:
        bukanVirus = 2

    if imgPtr:
        imgPtr.close()
        del imgPtr
    return (namaFile, ekstensiFile, formatFile, ukuranAwal, dukunganFile, tidakCorrupt, bukanVirus)

def returnAllFileFromPath(dirs:os.PathLike, conn):
    """Return a list of file from a dir, also verify is file exists and file in valid image extension"""
    allFile = []
    validExt = [".jpg", ".jpeg", ".png"]
    for root, _, files in os.walk(dirs):
        for file in files:
            fullPath = os.path.join(root, file)
            if os.path.isfile(fullPath) and os.path.splitext(fullPath)[1].lower() in validExt:
                allFile.append(os.path.join(root, file))
            else:
                pass
    conn.send(allFile)
    conn.close()