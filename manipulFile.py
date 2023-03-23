import shutil
import os
import tempfile
import basicos.manipulDir as mDir
import datetime
from pdf2image import convert_from_path


# =================================================
# Deletar arquivo
# ==================================================
def deletFile(path):
    if os.path.exists(path):
        try:
            os.remove(path)
        except BaseException as e:
            print(e)


# ==================================================
# Mover arquivos
# ==================================================
def moveFile(origem, destino):
    try:
        shutil.move(origem, destino)
    except BaseException as e:
        print(e)

# ==================================================
# Copiar arquivos
# ==================================================
def copyFile(origem, destino):
    try:
        shutil.copy(origem, destino)
    except BaseException as e:
        print(e)


# ===================================================
# #Gerar nome de arquivos temporarios
# ===================================================
def nameTemp(dir):
    temp = tempfile.NamedTemporaryFile()
    name = temp.name.split("\\")
    nameTemp = name[len(name) - 1]
    if os.path.exist(dir + nameTemp):
        return nameTemp + datetime.today().strftime('%d%m%Y%H%M%S')
    else:
        return nameTemp

# =============================================
#  Transforma PDF para imagens
# =============================================
def transformPDFtoImage(file, dir):
    path, name = file
    newPath = []
    extension = name.split(".")
    if len(extension) > 1:
        if extension[1].lower() == "pdf":
            try:
                images = convert_from_path(poppler_path=r"C:\poppler-0.68.0\bin", pdf_path=path)
                for i in range(len(images)):
                    newName = path.lower().replace("pdf", "jpg")
                    images[i].save(newName)
                    if os.path.exists(newName):
                        newPath.append(newName)
                        deletFile(path)
                    else:
                        moveFile(path, "{}falha/{}".format(dir, name))

            except BaseException as e:
                print(e)
    else:
        moveFile(path, "{}falha/{}".format(dir, name))
    return newPath

# ===================================================
#  Transforma PDF em imagem em lote
# ===================================================
def processLote(dir):
    listFiles = mDir.getFiles(dir)
    for file in listFiles:
        transformPDFtoImage(file, dir)