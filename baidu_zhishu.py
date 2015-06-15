#!/usr/bin/ env python
# coding:utf-8

import urllib
import urllib2
import cookielib
import re
from delorean import *
from BeautifulSoup import *


# s = "你好"  # 整个文件是UTF-8编码，所以这里的字符串也是UTF-8
# u = s.decode("utf-8")  # 将utf-8的str转换为unicode
# g = u.encode('GBK')  # 将unicode转换为str，编码为GBK

web_site = "http://index.baidu.com/?tpl=trend&word=%B1%B1%BE%A9"
staticpage = "https://www.baidu.com/cache/user/html/v3Jump.html"
baiduMainLoginUrl = 'https://passport.baidu.com/v2/api/?login'
baidutoken = "https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true"
d = Delorean()
tt = str(int(d.epoch()))
# baidutoken = "https://passport.baidu.com/v2/api/?getapi&tpl=index&apiver=v3&tt=" + \
    # tt + "&class=login&logintype=basicLogin&callback=bd__cbs__oyfb5r"
baidu_main_site = 'https://www.baidu.com/'
# tokenVal = "51539d037e917539102f5f0878268d2e"
username = "ganggegedahuB"
# password = "Mt6Q2n6kGBeqW%2BPuN9d3FuYq7bNU1LkSbLLKVvgg5By3wZPZp6gZur5dFl6s4W6zSJA5cJIsspi1n0xmhyUEaRrt1cyDF9xSiUXYRzgDZwapo4h9%2BqD%2B4G0%2BKLGCQ49XM7bYheWR0yhK9rqUoDMhXpezJz3ObL0N01fA3RV80aY%3D"

#------------------------------------------------------------------------------
# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#------------------------------------------------------------------------------
# check all cookies in cookiesDict is exist in cookieJar or not


def checkAllCookiesExist(cookieNameList, cookieJar):
    cookiesDict = {}
    for eachCookieName in cookieNameList:
        cookiesDict[eachCookieName] = False

    allCookieFound = True
    for cookie in cookieJar:
        if(cookie.name in cookiesDict):
            cookiesDict[cookie.name] = True

    for eachCookie in cookiesDict.keys():
        if(not cookiesDict[eachCookie]):
            allCookieFound = False
            break

    return allCookieFound


def respon_url(url):
    return urllib2.urlopen(url)


def get_tokenVal():
    token_patten = re.compile(r'"token" : "(?P<token_value>.*)", "cookie"')
    req = urllib2.Request(baidutoken)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0')
    tokenReturn = urllib2.urlopen(req)
    content = tokenReturn.read()
    m = re.findall(r"bdPass.api.params.login_token='(.*?)'", content)
    print m
    return m[0]


#------------------------------------------------------------------------------
# just for print delimiter
def printDelimiter():
    print '-' * 80


def login_baidu_index():

    printDelimiter()
    print '[Step 1] get baidu cookie:'
    req = urllib2.Request(baidu_main_site)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    resp = respon_url(req)
    for index, cookie in enumerate(cj):
        print '[', index, ']', cookie

    printDelimiter()
    print '[Step 2] get baidu cookie UBI for tokenVal:'
    req = urllib2.Request(baiduMainLoginUrl)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    resp = respon_url(req)
    for index, cookie in enumerate(cj):
        print '[', index, ']', cookie

    printDelimiter()
    print '[Step 3] get tokenVal'
    tokenVal = get_tokenVal()
    print 'tokenVal = ', tokenVal

    printDelimiter()
    print '[Step 3] post login'
    # 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    postDict = {
        #'ppui_logintime': "",
        'charset': "UTF-8",
        'apiver': "v3",
        'codestring': "",
        'token': tokenVal,
        'isPhone': "false",
        # 'index'         : "0",
        'u': "https://www.baidu.com/",
        'safeflg': "0",
        # http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html
        'staticpage': staticpage,
        'loginType': "1",
        'tpl': "mn",
        'callback': "parent.bd__pcbs__lzscl8",
        'username': "ganggegedahuB",
        'password': "liu7536308",
        #'verifycode'    : "",
        'mem_pass': "on",
        'tt': str(int(d.epoch()))
    }
    postData = urllib.urlencode(postDict)
    req = urllib2.Request(baiduMainLoginUrl, postData)
    req.add_header('Content-Type', "application/x-www-form-urlencoded")
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    req.add_header('Accept', 'text/html,application/xhtml+xml,*/*')
    req.add_header('Accept-Encoding', 'gzip,deflate')
    req.add_header('Accept-Language', 'zh-CN')
    uu=urllib2.urlopen(req).read()
    with open('web1.html', 'wb') as f:
        f.write(uu)

    printDelimiter()
    print '[Step 4] get back to baidu main web-site'
    req = urllib2.Request("http://index.baidu.com/?tpl=trend&word=%CC%EC%C6%F8")
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    return urllib2.urlopen(req)

# html = login_baidu_index().read().decode("gbk").encode("utf-8")
html = login_baidu_index().read()
# with open('web2.html', 'wb') as f:
    # f.write(html)
f=open('1.jpg', "wb")
f.write(html)
f.flush()
f.close()
# in most case, for do POST request, the content-type, is application/x-www-form-urlencoded
# 发送登录请求
cookiesToCheck = ['BDUSS', 'PTOKEN', 'STOKEN', 'SAVEUSERID']
loginBaiduOK = checkAllCookiesExist(cookiesToCheck, cj)
if(loginBaiduOK):
    print "+++ Emulate login baidu is OK, ^_^"
else:
    print "--- Failed to emulate login baidu !"
