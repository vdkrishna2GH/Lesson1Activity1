# Image Annotation
import cv2
import matplotlib.pyplot as plt

#Load the image
image_path = 'car1.jpg'
image = cv2.imread(image_path)

#Convert BGR to RGB 
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Get Dimensions
height,width, _ = image_rgb.shape
rect1_width,rect1_height = 150,150
top_left1 = (20,20) #fixed 20 pixels padding from top-left
bottom_right1 = (top_left1[0] + rect1_width,top_left1[1]+rect1_height)

cv2.rectangle(image_rgb,top_left1,bottom_right1,(0,255,255),3) #yellow rectangle 

rec2_width,rec2_height = 200,150
top_left2 = (width - rec2_width - 20, height - rec2_height - 20) #20 pixel padding
bottom_right2 = (top_left2[0]+ rec2_width, top_left2[1]+rec2_height)

cv2.rectangle(image_rgb,top_left2,bottom_right2,(255,0,255),3) #magenta rectangle

# Draw circles
center1_x = top_left[0] + rect1_width // 2
center1_y = top_left2[1] + rect1_height // 2
center2_x = top_left1[0] + rec2_width // 2
center2_y = top_left2[1] + rec2_height // 2

cv2.circle(image_rgb,(center1_x,center1_y),15,(0,255,0),-1)  #filled green circle
cv2.circle(image_rgb,(center1_x,center1_y),15,(255,0,0),-1)  #filled red circle

#draw connecting lines between centers of rectangle
cv2.line(image_rgb,(center1_x,center1_y),(center2_x,center2_y),(0,255,0),3)

#add text labels for regions and centers
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,'Region1',(top_left1[0],top_left1[1] - 10),font,0.7,(0,255,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Region2',(top_left2[0],top_left2[1] - 10),font,0.7,(255,0,255),2,cv2.LINE_AA)
