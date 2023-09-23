from PIL import Image
import easyocr
import numpy as np
import time
import cv2
from avi import solverV2
board=[[0,6,0,4,2,0,0,0,1],
         [1,9,0,0,8,3,0,2,0],
         [0,0,2,0,1,0,7,0,0],
         [0,0,0,8,7,0,5,0,0],
         [0,5,1,3,4,9,0,0,2],
         [4,0,3,0,5,0,0,8,0],
         [6,0,5,1,3,2,0,0,0],
         [7,0,4,0,0,8,0,1,0],
         [0,1,0,0,6,0,8,5,0]]
#from avi import checkcolor

reader = easyocr.Reader(['en','tr'])

pngList = list()
def Relize(png):           
    resim = cv2.imread(png) 
    resim = cv2.resize(resim, (900,900))  
    return resim

    
key = 0
key2 = 0
png = Relize("sudoku.png")
png2 = png
height, width, channels = png.shape
# Number of pieces Horizontally 
W_SIZE  = 9 
# Number of pieces Vertically to each Horizontal  
H_SIZE = 9

for ih in range(H_SIZE ):
   for iw in range(W_SIZE ):
   
      x = width/W_SIZE * iw 
      y = height/H_SIZE * ih
      h = (height / H_SIZE)
      w = (width / W_SIZE )
      #print(x,y,h,w)
      #print(int(y),int(y+h),int(x),int(x+w),"\n")
      png = png[int(y):int(y+h), int(x):int(x+w)]
      NAME = str(time.time()) 
      cv2.imwrite("parsel" + str(ih)+str(iw) +  ".png",png)
      image = Image.open("parsel" + str(ih)+str(iw) +  ".png")
      image_rgb = image.convert("RGB")
      result = reader.readtext(png, detail=0) 
      if len(result) == 0:
            for t in range(15):
                if image_rgb.getpixel((t+53,56)) == (52,72,97) :
                    pngList.append(["1"])
                    key=1
                    break
                elif image_rgb.getpixel((38,t+23)) == (52,72,97) :
                    pngList.append(["7"])
                    key2=1
                    break
                
            if(key != 1 and key2 !=1):
                pngList.append(['0'])
            key=0
            key2=0

           
                       
      else: 
        pngList.append(result)
      
             
      
            
      png = png2

#print(pngList)
for n in range(81):
    pngList[n] = (int(pngList[n][0]))

i = 0
while i != 81:

    for y in range(9):
        for x in range(9):
            board[y][x] = pngList[i]
            i +=1
#solver.sudokuSolver(pngList)
print(np.matrix(board))
solverV2.start(board)
   

