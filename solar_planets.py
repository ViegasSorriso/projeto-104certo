import cv2

img = cv2.imread("solar-System.jpg")


cv2.putText(img, "sol",(100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0))
cv2.putText(img, "Mercurio",(50,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (56,55,0))
cv2.putText(img, "Venus",(200,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,5,0))
cv2.putText(img, "Terra",(300,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (9,225,0))
cv2.putText(img, "Marte",(400,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (9,55,49))
cv2.putText(img, "Jupiter",(500,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (9,225,49))
cv2.putText(img, "Saturno",(700,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (9,55,49))
cv2.putText(img, "Urano",(1000,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (63,55,52))
cv2.putText(img, "Netuno",(1100,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (87,55,20))



cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.imwrite("planetas.jpg", img)