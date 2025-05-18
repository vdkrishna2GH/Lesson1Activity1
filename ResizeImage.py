import cv2 # type: ignore

image =cv2.imread("car1.jpg")  #Load the image

cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL) # Create a resizeable window
cv2.resizeWindow('Loaded Image',800,300)  #Sets the window size in 800 X 300 (width , height)

cv2.imshow('Loaded image',image) #Load the image in the resized window
cv2.waitKey(0) #Wait for the keypress

cv2.destroyAllWindows() #Closes all the windows

print(f"Image Dimensions are {image.shape}")  #Height, Width, RGB

