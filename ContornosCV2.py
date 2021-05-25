import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("AaFix.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cuadro = cv2.rectangle (gris,(150, 150), (350,350), (0, 255, 0), 2)
ret, thresh = cv2.threshold(gris, 200, 255,0)
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),2)
#cv2.imshow("Aa.png",img)
print(str(contours[-1].reshape(-1)).replace('\n',',').replace(' ',',').replace(',,',',').replace(',,',',').replace('[,','['))
plt.imshow(img)
plt.show()
#cv2.waitKey()
#cv2.destroyAllWindows()