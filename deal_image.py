#!/usr/bin/env python
# coding:utf-8
from PIL import Image
from pylab import *

image_name = "shot.png"

my_image = Image.open(image_name)


def crop_img(img):
    chart_box = (400, 450, 1400, 820)
    chart_image = img.crop(chart_box)
    chart_image.save('chart.jpg')

    search_box = (0, 80, 998, 289)
    search_img = chart_image.crop(search_box)
    search_img.save('search.jpg')
    return chart_image, search_img

c_i,s_i = crop_img(my_image)
s_i.convert('L').save("gray.jpg")
# search_data = array(search_img)

# 绘制图像
# imshow(search_data)

# if __name__ == "__main__":

