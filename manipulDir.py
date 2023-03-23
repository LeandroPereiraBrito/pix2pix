import shutil
import os
import config
import basicos.manipulFile as mFile


# ==================================================
# Gerar subpastas
# ==================================================
def gerarSubPasta(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)

# ==================================================
# Apagar pastas
# ==================================================
def deletPasta(caminho):
    try:
        shutil.rmtree(caminho)
        print("pasta:{} removida com sucesso.".format(caminho))
    except BaseException as e:
        print(e)

# ==================================================
# Gerar as pasta necessarías
# ==================================================
def gerarPastas(path):
    gerarSubPasta(path)

# ==================================================
# Gerar lista com todos os arquivos
# ==================================================
def getFiles(dir):
    listFiles = []
    for currentFolder, subFolder, files in os.walk(dir):
        for file in files:
            arquivo = "{}\{}".format(dir, file)
            if os.path.exists(arquivo) and arquivo not in listFiles:
                listFiles.append((arquivo, file))
    return listFiles

# ==================================================
# Gerar lista com todos os arquivos
# ==================================================
def balanceamento(dir1, dir2):
    list0 = getFiles(dir1)
    list1 = getFiles(dir2)
    poda = 0
    if len(list0) > len(list1):
        remove = list0
        poda = len(list1)
    elif len(list0) < len(list1):
        remove = list1
        poda = len(list0)

    if poda > 0:
        for item in remove:
            path, name = item
            path = path.replace("\\", "/")
            poda -= 1
            if poda < 0:
                mFile.deletFile(path)