import cv2
import os
from PIL import Image
import numpy as np

# ========================================   
# Redimencionar imagem
# ========================================
def resizeImage(img,newAlt):
    try:
        return cv2.resize(img, newAlt, interpolation = cv2.INTER_AREA)
    except BaseException as e:
        print(e)
        return img

# ========================================
# Salvar imagem binarizada
# ========================================
def binarizar(src):
    edges = cv2.Canny(src, 100, 100)
    kernel = np.ones((1,1), np.uint8)
    dilation = cv2.dilate(edges, kernel, iterations=1)

    return np.asarray(edges)
    
# ========================================
# Funçãos de apoio apresentar a imagens
# ========================================
def apresentar( img):
    cv2.imshow("teste", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ========================================
# Funçãos de apoio abrir imagens imagens
# ========================================
def openImage(path):
    try:
        imagem = cv2.imread(path)
    except:
        imgPill = Image.open(path)
        imagem = np.asarray(imgPill)
    if imagem is not None:
        return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        return None
    
# ========================================
# Girar imagem
# ========================================
def rotacionar(pathFile, angulo):
    try:
        imgPil = Image.open(pathFile)
        imgPil = imgPil.rotate(angulo, expand=True)
        imgPil.save(pathFile)
    except BaseException as e:
        print(e)

# ========================================
# Salvar Imagem
# ========================================
def salvarImagem(destino, imagem):
    try:
        try:
            cv2.imwrite(destino, imagem)
        except:
            img = Image.fromarray(imagem)
            img.save(destino)
    except BaseException as e:
        print(e)
    
# ========================================
# Juntar imagens
# ========================================
def joinImagem(img1,img2, posicao):


    try:
        if posicao.lower() == "v":
            return cv2.vconcat(img1, img2)
        else:
            join = cv2.hconcat(img1, img2)
            apresentar(join)
            return join
    except BaseException as e:
        print(e)


def hconcat_resize(img_list,interpolation =cv2.INTER_CUBIC):
    h_min = min(img.shape[0]
                for img in img_list)

    im_list_resize = [cv2.resize(img,
                                 (int(img.shape[1] * h_min / img.shape[0]),
                                  h_min), interpolation
                                 =interpolation)
                      for img in img_list]

    return cv2.hconcat(im_list_resize)