#!/usr/bin/env python
#!coding:utf-8
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from pylab import *
from deal_image import *
from pytesser import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

number_zone_width = 60
number_zone_height = search_height
height_gap = int(number_zone_height / 7)
number_zone_box = (
    search_width - number_zone_width, 0, search_width, number_zone_height)


def crop_number_zone(img, show=False):
    global number_zone_box
    img = img.crop(number_zone_box)
    if show == True:
        img.show()
    return img


def get_each_number_img(img_zone):
    global height_gap
    img_list = []
    for n in range(7):
        img_list.append(enhance(img_zone.crop((0,
                                               height_gap * n, number_zone_width, height_gap * (n + 1)))))
    return img_list


def img2string(img_list):
    return [twovalue_img_data(gray_img(img), 100) for img in img_list]


def hist_img(img):
    global height_gap
    img_list = img2data(img_xy_rotate(img))
    hist_list = []
    for n in range(number_zone_width):
        hist_list.append(
            sum(img_list[height_gap * n:height_gap * (n + 1)]) / height_gap)
    print len(img_list)
    figure()
    # 不使用颜色信息
    gray()
    # 在原点的左上角显示轮廓图像
    contour(array(img), origin='image')
    axis('equal')
    axis('off')
    figure()
    print hist_list
    plot(range(number_zone_width), hist_list)
    # ylim(0,255)
    # show()
    return hist_list
    # return histogram(img)


def split_img(img):
    hist_list = hist_img(img)
    split_imgs = []
    index_gap_list = []
    index_old = 0
    index_current = 0
    for n in range(number_zone_width):
        if hist_list[n] == 255:
            index_current = n
            if 3 < (index_current - index_old) < 9:
                # print (index_old, index_current)
                index_gap_list.append(index_current - index_old)
                split_imgs.append(
                    img.crop((index_old - 1, 0, n + 1, height_gap)))
            index_old = index_current
    image = Image.new('L', (100, height_gap), 255)
    count = len(split_imgs)
    print index_gap_list
    for n in range(count):
        image.paste(split_imgs[n], (n*10+5, 0, n*10+5+index_gap_list[n]+2, height_gap))
    return image


# def img_collect(img):
#     img_sum = Image.create()

if __name__ == '__main__':
    enhance_shot_img = enhance(Image.open("search_filter_img.jpg"))
    enhance_shot_img.save("search_enhance_img.jpg")
    # enhance_shot_img.show()
    number_zone_img = crop_number_zone(enhance_shot_img)
    # img_xy_rotate(number_zone_img).show()
    img_list = get_each_number_img(number_zone_img)
    img = img2string(img_list)[6]
    # for img in img2string(img_list):
    #     img.show()
    # img2string(img_list)[2].show()
    #     text = image_to_string(img)
    #     print '*'*50
    #     print text
    # img = img2string(img_list)[4]
    # img = enhance(img, 5.0)
    # img = twovalue_img_data
    # img.show()
    # print hist_img(img)
    # print len(split_img(img))
    split_imgs = split_img(img)
    # split_imgs.show()
    split_imgs.save('1.tiff')
    # split_imgs = [m.resize((30,150))for m in split_imgs]
    # split_imgs[0].crop((0,5,9,25)).show()
    # for m in split_imgs:
    # m.save(split_imgs.index(m))
    text = image_to_string(split_imgs)
    print '*'*30, text, '*'*30
    # print image_to_string(img)

    # im = Image.open('phototest.tif')
