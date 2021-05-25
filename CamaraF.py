from cv2 import *
import numpy as np

namedWindow("webcam")
vc = VideoCapture(0)

while True:
    next, frame = vc.read()
    #Cuando se deja presionado la tecla W la camara se activara, si se deja de pulsar esta se detendra con la ultima iagen que se detecte
    if waitKey(2) == ord("w"):
        cuadro = cv2.rectangle (frame,(1, 1),(200,200), (0, 255, 0), 2)
        cv2.imshow("webcam", frame)
    #Cuando se presiona la tecla e se tomara una captura del ultimo frameq.
    if waitKey(3) == ord("e"):
        cv2.imwrite("captura.png",frame)
        print("Foto tomada correctamente")
        #Cuando se presiona la tecla C se muestra la captura tomada con aterioridad
    if waitKey(4) == ord("c"):
        cv2.imshow("captura.png",frame)
       #Cuando se presion Q la camara se apaga y finaliza el programa
    if waitKey(1) == ord("q"):
        break
cv2.waitKey()
cv2.destroyAllWindows()