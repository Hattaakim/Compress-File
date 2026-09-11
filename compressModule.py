import os, math
from PIL import Image, ImageFile, ImageOps
import pillow_heif

#antisipasi file rusak
ImageFile.LOAD_TRUNCATED_IMAGES = True
#untuk gambar HEIF/HEIC
pillow_heif.register_heif_opener()

def compressImage(fPath, outDir: os.PathLike,
                max_pixels:int=12_000_000, quality:int=85, delOriFile:bool=False):
    """Return namaFile, sizeAkhir, Dihemat, Status, DisimpanDi, DIhapus (0 stip 1 centang 2 silang)"""
    # default to 12mp 85% quality
    namaFile = ""
    statusKompresi = 0
    fileSizeAwal = 0
    fileSizeAkhir = 0
    penghematanSize = 0
    outPath = False
    fileDeleted = 0

    try:
        fileSizeAwal = os.path.getsize(fPath)
        namaFile = os.path.basename(fPath)
        namaFileSplit = os.path.splitext(namaFile)
        outPath = os.path.join(outDir, 
                               f"{namaFileSplit[0]}-Compressed{namaFileSplit[1].lower()}")

        imgObj = Image.open(fPath)
        imgObj = ImageOps.exif_transpose(imgObj)

        if imgObj.mode in ('RGBA', 'LA') or (imgObj.mode == 'P' and 'transparency'
                                                in imgObj.info):
            alpha = imgObj.convert('RGBA').split()[-1]
            emptyBg = Image.new("RGB", imgObj.size, (255,255,255))
            emptyBg.paste(imgObj, mask=alpha)
            imgObj = emptyBg
        elif imgObj.mode != 'RGB':
            imgObj = imgObj.convert('RGB')

        w,h = imgObj.size
        currentPixels = w*h
        if currentPixels > max_pixels:
            rasio = math.sqrt(max_pixels/currentPixels)
            widthBaru = int(w*rasio)
            heightBaru = int(h*rasio)
            imgObj = imgObj.resize((widthBaru, heightBaru),
                                    Image.Resampling.LANCZOS) 

        imgObj.save(outPath, 'JPEG',
                    quality=quality, optimize=True)
        imgObj.close()

        statusKompresi = 1
        fileSizeAkhir = os.path.getsize(outPath)
        penghematanSize = fileSizeAwal - fileSizeAkhir

        if delOriFile == True:
            try:
                os.remove(fPath)
                fileDeleted = 1

            except (FileNotFoundError, PermissionError, OSError, IsADirectoryError):
                fileDeleted = 2

        return(namaFile, fileSizeAkhir, penghematanSize, statusKompresi, outPath, fileDeleted)

    except Exception as e:
        return(namaFile, fileSizeAkhir, penghematanSize, statusKompresi, outPath, fileDeleted)