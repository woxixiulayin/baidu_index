#!/usr/bin/env python
# coding:utf-8
from PIL import Image, ImageDraw, ImageFilter
from pylab import *

image_name = "shot.png"

my_image = Image.open(image_name)

search_width = 996
search_height = 209


def crop_img(img):
    chart_box = (400, 450, 1400, 820)
    chart_image = img.crop(chart_box)
    chart_image.save('chart.jpg')

    search_box = (0, 80, search_width, 80 + search_height)
    search_img = chart_image.crop(search_box)
    search_img.save('search.jpg')
    search_filter_img = search_img.filter(ImageFilter.DETAIL)
    search_filter_img.save('search_filter_img.jpg')
    return chart_image, search_img


def gray_img(img):
    return img.convert('L')


def twovalue_img_data(img, threhold=125):
    dst = img
    pix_list = list(dst.getdata())
    for n in range(len(pix_list)):
        if pix_list[n] < threhold:
            pix_list[n] = 0
        else:
            pix_list[n] = 255
    dst.putdata(pix_list)
    return dst, pix_list


def img_xy_rotate(img):
    width, height = img.size
    pix_list = list(img.getdata())
    pix_xy_rotate_list = []
    for x in width:
        y_list = []
        for y in height:
            y_list

def get_x_day_data(img, x_day):
    dst, pix_list = twovalue_img_data(img, 150)
    (width, height) = dst.size
    gap = width * 1.0 / (x_day - 1)
    draw = ImageDraw.Draw(dst)
    day2x = []
    days_data = []
    for n in range(0, x_day):
        if n < x_day - 1:
            x = int(gap * n)
        elif n == x_day:
            x = width - 1
        day2x.append(x)
        draw.line([(x, 0), (x, height)], width=1)
        day_data = []
        for m in range(height):
            # print x,m,dst.getpixel((x,m))
            day_data.append(dst.getpixel((x, m)))
        days_data.append(day_data)
    # print days_data[1]
    # print day2x
    # dst.show()


crop_img(my_image)
search_fil = Image.open("search_filter_img.jpg")
get_x_day_data(gray_img(search_fil), 30)
gray = gray_img(search_fil)
# twovalue_img(gray,150)
# print len(list(gray.getdata()))


# crop_img(my_image)
# c_i,s_i = crop_img(my_image)

# gray = Image.open("gray.jpg")
# search_filter_img = gray.filter(ImageFilter.SHARPEN)
# search_filter_img.save('gray_img.jpg')
# s_i.convert('L').save("gray.jpg")
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
# line = (100, 0, 100, 200)
# gray.putpixel(line, 100)
# gray.show()
# gray_draw = ImageDraw.ImageDraw(gray)
# gray_draw.line(line)


# 绘制图像
# imshow(search_data)

# if __name__ == "__main__":
