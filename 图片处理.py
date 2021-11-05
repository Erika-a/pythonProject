import os
import shutil
from PIL import Image
from http.client import HTTPResponse


im = Image.open('Image/R-C.jpg')

# print(im.size)
#
# width,heiht = im.size
# print(width,heiht)
#
# print(im.filename)
#
# print(im.format)
#
# print(im.format_description)

# im.save('Image/R-C.PNG')

# im = Image.new('RGBA',(100,200),'purple')
# im.save('Image/purpleImage.png')
# im2 = Image.new('RGBA',(20,20))
# im2.save('Image/transparentImage.png')

cropim = im.crop((200,300,500,600))
copyim = im.copy()
print(cropim.size)
copyim.paste(cropim,(0,0))
copyim.paste(cropim,(400,500))

#图像平铺

imwidth,imheight = im.size
cropimwidth,cropimheight = cropim.size
copyimtwo = im.copy()
for left in range(0,imwidth,cropimwidth):
    for top in range(0,imheight,cropimheight):

        copyimtwo.paste(cropim,(left,top))

#图像放大缩小

width,heiht = im.size
qsizeim = im.resize((int(width/2),int(heiht/2)))
# qsizeim.save('Image/qsize.jpg')
wsizeim = im.resize((width,heiht + 300))
# wsizeim.save('Image/wsizeim.jpg')

#图像的旋转和翻转

im.rotate(90).save('Image/rotate90.jpg')
im.rotate(180).save('Image/rotate180.jpg')
im.rotate(270).save('Image/rotate270.jpg')

for foldername,subfolders,filenames in os.walk('C"\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if (filename.endswith('.png')) or (filename.endswith('.jpg')):
            numPhotoFiles += 1





