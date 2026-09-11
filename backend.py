import os, filetype
from multiprocessing import Queue
from PIL import Image

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
    return (namaFile, ukuranAwal, ekstensiFile, formatFile, dukunganFile, tidakCorrupt, bukanVirus)

def returnAllFileFromPath(dirs:os.PathLike, conn):
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