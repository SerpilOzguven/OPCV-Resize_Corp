import cv2


image = cv2.imread("lenna.png")
print("Resim boyutu:",  image.shape)


cv2.imshow("Orginal:", image)


imageResized = cv2.resize(image, (800,800))
print("Resize image shape:", imageResized)
cv2.imshow("İmage Resized",imageResized)



#kırp
imgCropped = image[:200,:300]#(height,width(opencvde)) , normalde yaptığımız programlarda(width,height)
cv2.imshow("Kirpik resim:", imgCropped)