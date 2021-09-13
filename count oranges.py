#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def count_oranges(image):
    
    #lowerBound=np.array([5,50,50])
    #upperBound=np.array([15,255,255])
    lowerBound=np.array([1,100,80])
    upperBound=np.array([22,256,256])
   
    while True:
        img=cv2.imread(image)
    
 
    
        #img=cv2.resize(img, (1000,700))
        cv2.imshow("Original Image",img)
    
         #convert to HSV image
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    
        #mask image
        mask=cv2.inRange(imgHSV,lowerBound,upperBound)
        cv2.imshow("Masked Image",mask)
    
    
        #find contours(shape outlines)
        contours, hierarchy =cv2.findContours(mask ,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(img,contours,-1,(255,0,0),1)
    
        count=0
        #   highlight only required sized masked shapes
        for c in contours:
            area=cv2.contourArea(c)
            #approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
            #remove noise-small sections
        
            if area >=400:
            #if ((len(approx) > 8) and (area > 150)):
                count+=1
                x,y,w,h =cv2.boundingRect(c)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0, 255), 2)
                cv2.drawContours(img, c, -1, (255, 0, 0), 3)
                cv2.putText(img, str(count),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255))
                cv2.imshow("Final Image", img)
                #print(area)
            
            #  print(approx)
            #print("\n")
       
    
    
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
    print(count)


# In[ ]:


if __name__=='__main__':
    image='C:/Users/Admin/Desktop/Project/project/oranges2.jpg'
    count_oranges(image)


# In[ ]:




