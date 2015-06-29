#!/usr/bin/env python
# coding:utf-8
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
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


def img2data(img):
    return list(img.getdata())


def gray_img(img):
    return img.convert('L')

def enhance(img, value = 2.0):
    return ImageEnhance.Contrast(img).enhance(value)

def twovalue_img_data(img, threhold=180):
    dst = img
    pix_list = list(dst.getdata())
    for n in range(len(pix_list)):
        if pix_list[n] < threhold:
            pix_list[n] = 0
        else:
            pix_list[n] = 255
    dst.putdata(pix_list)
    return dst

def onevalue_gray(gray_img, threhold = 253):
    dst = gray_img
    pix_list = img2data(gray_img)
    for n in range(len(pix_list)):
        if pix_list[n] == threhold:
            pix_list[n] = 0
        else:
            pix_list[n] = 255
    dst.putdata(pix_list)
    return dst

def onevalue_color(img):
    blue_color = [(237, 255, 255) ,(233, 255, 255),(239, 255, 255)]
    dst = img
    # dst.show('enhance')
    pix_list = img2data(img)
    for n in range(len(pix_list)):
        if pix_list[n][0] !=0 or pix_list[n][1] > 2 or pix_list[n][2] ==0 or \
            pix_list[n][0] == pix_list[n][1] == pix_list[n][2]:
            pix_list[n] = (255,255,255)
    dst.putdata(pix_list)
    # dst.show()
    # day_2_x(dst,30,True)
    gray = gray_img(dst)
    # gray.show()
    twovalue = twovalue_img_data(gray, 20)
    # static_img_color(dst)
    return twovalue
    # for n in range(len(pix_list)):
    #     if pix_list[n][0] < (pix_list[n][1]+pix_list[n][2])/2:
    #         pix_list[n] = (0,0,0)
    # dst.putdata(pix_list)
    # static_img_color(dst)
    # gray_img(dst).show()
    # for n in range(len(pix_list)):
    #     if sum(pix_list[n])<100:
    #         pix_list[n] = (255,255,255)
    # dst.putdata(pix_list)
    return dst    

def img_xy_rotate(img):
    return img.transpose(Image.ROTATE_270)
    # width, height = img.size
    # pix_list = list(img.getdata())
    # pix_xy_rotate_list = []
    # pix_height_list = []
    # for x in range(width):
    #     y_list = []
    #     for y in range(height):
    #         y_list.append(pix_list[y * width + x])
    #         pix_height_list.append(y_list[-1::-1])
    #     pix_xy_rotate_list.append(pix_height_list)
    # return img.transpose(Image.ROTATE_270), pix_xy_rotate_list


def day_2_x(img, x_day, show_lines=False):
    # dst = twovalue_img_data(img, 180)
    dst =img
    (width, height) = dst.size
    gap = width * 1.0 / (x_day - 1)
    draw = ImageDraw.Draw(dst)
    day2x = []
    for n in range(0, x_day):
        if n == 0:
            x = 1
        elif n < x_day - 1:
            x = int(gap * n)
        elif n == x_day:
            x = width - 1
        day2x.append(x)
        if show_lines is True:
            draw.line([(x, 0), (x, height)], width=1)
    if show_lines is True:
        dst.show()
    return day2x
    # print days_data[1]
    # print day2x


def data_of_day(day2x, img_270):
    # data_list = []
    img_270_list = list(img_270.getdata())
    print img_270_list


def zhifang_img(gray_img):
    pix_list = img2data(gray_img)
    zhifang_list = []
    for i in range(256):
        zhifang_list.append(0)
    for n in range(len(pix_list)):
        zhifang_list[pix_list[n]] += 1
    # print zhifang_list
    plot(range(256), zhifang_list)
    axis([240,256,0,zhifang_list[-1]])
    show()

def static_img_color(img):
    pix_list = img2data(img)
    color_dic = {}
    list_color = []
    for n in pix_list:
        if list_color.count(n) == 0:
            list_color.append(n)
            color_dic[n] = 0
        color_dic[n] += 1
    print len(color_dic)
    color_dic = sorted(color_dic.items(), key=lambda d:d[1], reverse=True)
    for (c,m) in color_dic:
        print 'color:',c,' number:',m

#get index number of x day's point
def x_days_index(gray,x_day_list):
    im = img_xy_rotate(gray)
    # im.show()
    xy_rotate_list = img2data(im)
    x_days_index = []
    for n in x_day_list:
        x_day_data = xy_rotate_list[n*search_height:(n+1)*search_height]
        point_count = 0
        point_number = 0
        for m in range(search_height):
            if x_day_data[m] == 0:
                point_count += m
                point_number += 1
        x_days_index.append(point_count * 1.0 / point_number)
    return x_days_index


if __name__ == '__main__':
    crop_img(my_image)
    search_fil = Image.open("search_filter_img.jpg")
# search_enhance = ImageEnhance.Contrast(search_fil).enhance(2.0)
    v = onevalue_color(enhance(search_fil))
    days2x = day_2_x(v, 30)
    print x_days_index(v, days2x)
# search_enhance.show()
# gray = gray_img(search_fil)
# print img2data(search_fil)
# static_img_color(enhance(search_fil))
# v.show()
# day_2_x(v, 30, True)
# value_2 = twovalue_img_data(gray, 180)
# value_2.show()
# data_of_day(days2x, value_2)

# zhifang_img(gray)
# onevalue_gray(gray,239).show()
# print days2x

# gray.show()
# im = gray
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.show()

#
# value_2[0].show()
# img_xy_rotate(value_2[0]).show()
# for i in range(4):
# print xy_list[18]

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
