import os.path
import fast.metodosRotate as metodosRotate
import basicos.manipulDir as mDir
import basicos.manipulFile as mFile
import pix2pix.pixConfig as config
import basicos.manipulImage as mImage

iaRot = metodosRotate.metodosRotate()


def prepararIma(path):
    # Gerar o diretório para processamento das imagens
    mDir.deletPasta(config.dirTemp)
    mDir.gerarSubPasta(config.dirTemp)
    list = mDir.getFiles(path)
    contador = 1
    for item in list:
        path,name = item
        name = name.lower()
        if name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png"):
            ext = name.split(".")
            if mImage.openImage(path) is None:
                mFile.deletFile(path)
            else:
                mFile.copyFile(path,"{}/{}.{}".format(config.dirTemp,contador,ext[1]))
        contador +=1


def fase2():
    # Gerar os diretórios
    mDir.gerarSubPasta(config.dirVal)
    mDir.gerarSubPasta(config.dirTest)
    mDir.gerarSubPasta(config.dirTrain)

    list = mDir.getFiles(config.dirTemp)
    # Separa diretório
    qtdTest  = int(len(list) * 0.2)
    qtdVal = int(len(list) * 0.1)

    qtd = 1
    for item in list:
        path, name = item
        name = name.lower()
        name2 = name.split(".")
        print(name)
        if name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png"):
            iaRot.vertical(path)
            img = mImage.openImage(path)
            imgR = mImage.resizeImage(img,(256,256))
            bin = mImage.binarizar(imgR)
            join =mImage.hconcat_resize([imgR,bin])


        try:
            if qtd < qtdVal:
                mImage.salvarImagem("{}{}.jpg".format(config.dirVal,name2[0]),join)
            elif qtd > (qtdVal) and qtd < (qtdVal + qtdTest):
                mImage.salvarImagem("{}{}.jpg".format(config.dirTest, name2[0]), join)
            else:
                mImage.salvarImagem("{}{}.jpg".format(config.dirTrain, name2[0]), join)
        except BaseException as e:
            print(e)
        qtd +=1





