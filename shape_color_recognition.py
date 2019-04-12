import cv2
import imutils
import os.path
from scipy.spatial import distance as dist
from ALLColors import colors
import numpy as np
colorNames1 = []
for (i, (name, rgb)) in enumerate(colors.items()):
        colorNames1.append(name);
sh=["Triangle","Square","Rectangle","Pentagon","Hexagon","Star","Circle"]
cnt=[0]*7
cntColor=[0]*139

class ShapeDetector:
        def __init__(self):
                pass

        def detect(self, contour):
                # initialize the shape name and approximate the contour
                shape = "unidentified"
                
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

                # if the shape is a triangle, it will have 3 vertices
                if len(approx) == 3:
                        shape = "triangle"
                        cnt[0]=cnt[0]+1;
                # if the shape has 4 vertices, it is either a square or
                # a rectangle
                elif len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        if w==h :
                            shape = "Square"
                            cnt[1]=cnt[1]+1;
                        else:
                            shape="Rectangle"
                            cnt[2]=cnt[2]+1;

                # if the shape is a pentagon, it will have 5 vertices
                elif len(approx) == 5:
                        shape = "pentagon"
                        cnt[3]=cnt[3]+1;
                elif len(approx)==6:
                        shape="Hexagon"
                        cnt[4]=cnt[4]+1;
                elif len(approx)==10:
                        shape="Star"
                        cnt[5]=cnt[5]+1;
                # otherwise, we assume the shape is a circle
                elif len(approx)>=7:
                        shape = "circle"
                        cnt[6]=cnt[6]+1;
                # return the name of the shape
                return shape      
      
class ColorLabeler:
        def __init__(self):
                # initialize the colors dictionary, containing the color
                # name as the key and the RGB tuple as the value
                
                # allocate memory for the L*a*b* image, then initialize
                # the color names list
                self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
                
                self.colorNames = []
                # loop over the colors dictionary
                for (i, (name, rgb)) in enumerate(colors.items()):
                        # update the L*a*b* array and the color names list
                        self.lab[i] = rgb
                        
                        self.colorNames.append(name)
                        #print(self.colorNames[i])

                # convert the L*a*b* array from the RGB color space
                # to L*a*b*
                self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

        def label(self, image, contour):
                # construct a mask for the contour, then compute the
                # average L*a*b* value for the masked region
                mask = np.zeros(image.shape[:2], dtype="uint8")
                cv2.drawContours(mask, [contour], -1, 255, -1)
                #cv2.imshow('m',mask)
                mask = cv2.erode(mask, None, iterations=2)
                mean = cv2.mean(image, mask=mask)[:3]
                #print(mean)
                # initialize the minimum distance found thus far
                minDist = (np.inf, None)
                #print(minDist[0])
                # loop over the known L*a*b* color values
                for (i, row) in enumerate(self.lab):
                        # compute the distance between the current L*a*b*
                        # color value and the mean of the image
                       
                        d = dist.euclidean(row, mean)
                        # if the distance is smaller than the current distance,
                        # then update the bookkeeping variable
                        if d < minDist[0]:
                                minDist = (d, i)
                                print(minDist)
                cntColor[minDist[1]]=cntColor[minDist[1]]+1;
                # return the name of the color with the smallest distance
                return self.colorNames[minDist[1]]


# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
with open("input.txt") as fp:
      ipimage=fp.readlines()
ipimage[0]='inputImages/'+ipimage[0];
print(ipimage[0]);
image = cv2.imread(ipimage[0])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# initialize the shape detector and color labeler
sd = ShapeDetector()

cl = ColorLabeler()

# loop over the contours
for contour in cnts:

        # compute the center of the contour
    M = cv2.moments(contour)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)

        # detect the shape of the contour and label the color
    shape = sd.detect(contour)
    color = cl.label(lab, contour)

        
    contour = contour.astype("float")
    contour *= ratio
    contour = contour.astype("int")
    text = "{} {}".format(color, shape)
    cv2.drawContours(image, [contour], -1, (0, 255, 255), 2)
    cv2.putText(image, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0,0), 1)
    
        # show the output image
    cv2.imshow("Image", image)
cv2.imwrite('output.jpg',image);

f = open("countShape.txt", "w")

for (i, j) in enumerate(cnt):
        if(j>0):
                f.write(sh[i]+"\t\t"+str(j)+"\n");
                #f.write(j);
                print(sh[i],j);
f1=open("countColor.txt", "w")
print("\nColorwise counting");
for (i, j) in enumerate(cntColor):
        if(j>0):
                f1.write(colorNames1[i]+"\t\t"+str(j)+"\n");
                print(colorNames1[i],j);
f.close();
f1.close();
