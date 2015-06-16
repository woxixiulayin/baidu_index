#!/usr/bin/env python
# coding:utf-8
from PIL import Image
from pylab import *

image_name = "shot.png"

my_image = Image.open(image_name)

search_width = 998
search_height = 209
def crop_img(img):
    chart_box = (400, 450, 1400, 820)
    chart_image = img.crop(chart_box)
    chart_image.save('chart.jpg')

    search_box = (0, 80, search_width, 80 + search_height)
    search_img = chart_image.crop(search_box)
    search_img.save('search.jpg')
    return chart_image, search_img

c_i,s_i = crop_img(my_image)

print s_i.getpixel((400,100))



#s_i.convert('L').save("gray.jpg")
# gray = Image.open("gray.jpg")
# yuzhi = 140
# pix_list = list(gray.getdata())
# a=[]
# for n in range(len(pix_list)):
#     if pix_list[n] > yuzhi:
#         a.append(255)
#     else:
#         a.append(0)

# gray.putdata(a)
# gray.show()

# search_data = array(search_img)

# 绘制图像
# imshow(search_data)

# if __name__ == "__main__":

