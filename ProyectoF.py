from cv2 import *
import numpy as np
import matplotlib.pyplot as plt

namedWindow("webcam")
vc = VideoCapture(0)

while True:
    next, frame = vc.read()
    #Cuando se deja presionado la tecla W la camara se activara, si se deja de pulsar esta se detendra con la ultima iagen que se detecte
    if waitKey(2) == ord("w"):
        cuadro = cv2.rectangle (frame,(0, 0),(200,200), (0, 255, 0), 2)
        rectangulo = cv2.rectangle (frame,(40, 15),(150,200), (0, 0, 255), 2)
        cv2.imshow("webcam", frame)
    #Cuando se presiona la tecla e se tomara una captura del ultimo frameq.
    if waitKey(3) == ord("e"):
        cv2.imwrite("captura.png",frame)
        print("Foto tomada correctamente")
        #Cuando se presiona la tecla C se muestra la captura tomada con aterioridad
    if waitKey(4) == ord("c"):
        cv2.imshow("captura.png",frame)
       #Cuando se presion r la captura se recorta a los parametros necesarios
    if waitKey(5) == ord ("r"):
        img = cv2.imread("captura.png")
        crop_img = img[0:200, 0:200]
        cv2.imwrite("Rcaptura.png", crop_img)
        cv2.imshow("Rcaptura.png",crop_img)
        cv2.waitKey()
        #cv2.destroyAllWindows()
        #Cuando se preciona i se contornea una de las letras del abcedario y da sus coordenadas
    if waitKey(6) == ord ("i"):
        img2 = cv2.imread(input("Escribe el nombre de la letra deseada(agrega .png al final): "))
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        gris = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        _,binaria = cv2.threshold(gris, 200, 255, cv2.THRESH_BINARY_INV)
        contours,_ = cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img2,contours,-1,(0,0,255),2)
        plt.imshow(img2)
        A1 = print(str(contours[-1].reshape(-1)).replace('\n',',').replace(' ',',').replace(',,',',').replace(',,',',').replace('[,','['))
        plt.show()
        #Cuando se preciona o se contornea la captura recortada
    #if waitKey(7) == ord ("o"):
        img3 = cv2.imread("Rcaptura.png")
        img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        gris2 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)  
        ret, thresh = cv2.threshold(gris2, 127, 255,0)
        contourss,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img3,contourss,-1,(0,0,255),2)    
        plt.imshow(img3)
        A2 = print(str(contourss[-1].reshape(-1)).replace('\n',',').replace(' ',',').replace(',,',',').replace(',,',',').replace('[,','['))
        plt.show() 
        if A1 == A2 or A1 == A2+1 or A1 == A2-1:  
            print("Si es la letra seleccionada")
        else:
            print("No se encuentra ninguna letra")
    if waitKey(1) == ord("q"):
        break
cv2.waitKey()
cv2.destroyAllWindows()