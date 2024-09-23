import sys
import random
import math 
from random import randrange
from PIL import Image, ImageDraw 
# from pygments import highlight
# from pygments.formatters.terminal import TerminalFormatter
# from pygments.lexer import RegexLexer
# from pygments.token import Token

totalLength = 160 # 160 cm
workingLength = 0
lowLen = 3
uppLen = 12
colorList = ["white", "turquoise", "cinnamon", "oldrose", "lightblue", "winered"]
colorCodeDict = {"white":(247, 240, 225),
                 "turquoise": (0, 68, 82),
                 "cinnamon": (122, 49, 22),
                 "oldrose": (179, 121, 133),
                 "lightblue": (141, 186, 235),
                 "winered": (112, 16, 35)}
workingList = colorList.copy()
random.shuffle(workingList)
prevColor = ""
curX = 0
f = open('instructions.txt', 'w')
outimg = Image.new("RGB", (150, 1600))

if __name__ == "__main__":
  # gen sequence
  while workingLength < totalLength:
    if workingList == []:
      workingList = colorList.copy()
      random.shuffle(workingList)
    
    # color
    curColor = workingList.pop(0)
    if curColor == prevColor:
      workingList.append(curColor)
      curColor = workingList.pop(0)
    curCode = colorCodeDict[curColor]
          
    # length
    if workingLength >= (totalLength - uppLen):
      curLength = totalLength - workingLength
    else:
      if curColor == 'white':
        curLength = randrange(start=lowLen+3, stop=uppLen)
      else:
        curLength = randrange(start=lowLen, stop=uppLen)
    
    st = str(curColor)+" -- "+str(curLength)+" cm"
    print(st)
    f.write(st+'\n')
    
    shape = [0, curX, 150, curX+curLength*10]
    curImg = ImageDraw.Draw(outimg)
    curImg.rectangle(shape, fill=curCode)
    curX += curLength*10+1

    prevColor = curColor
    workingLength += curLength
  
  # draw
  outimg.show()
  outimg.save("scarf.png", "PNG")
  f.close()