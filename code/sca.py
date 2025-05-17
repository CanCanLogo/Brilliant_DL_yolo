import re  # 为了正则表达式
import requests  # 请求网页url
import os  # 操作系统
from time import sleep

num = 0  # 给图片名字加数字
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Cookie': 'winWH=%5E6_1488x742; BDIMGISLOGIN=0; BDqhfp=%E5%A4%A9%E5%B9%B3%20%E5%AE%9E%E9%AA%8C%26%260-10-1undefined%26%260%26%261; BAIDUID_BFESS=80EEDAAA1DFDB969F763A4DBBEE3C633:FG=1; __bid_n=18b7c07c2c043846ba2252; jsdk-uuid=3aae854e-49cb-4edc-a335-085335a9e60a; BAIDU_WISE_UID=wapp_1703407501474_615; BIDUPSID=80EEDAAA1DFDB969F763A4DBBEE3C633; PSTM=1703757891; H_PS_PSSID=39943_39938_39974_39998_40009_40016_40045; BDUSS=DluNElLOGVwa1h-cGpDS0ZXaEdOUklOeU9oRXlDSEx6N2wwMm5vflhpTE4xYlJsRVFBQUFBJCQAAAAAAQAAAAEAAAAK7RhDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM1IjWXNSI1lc; BDUSS_BFESS=DluNElLOGVwa1h-cGpDS0ZXaEdOUklOeU9oRXlDSEx6N2wwMm5vflhpTE4xYlJsRVFBQUFBJCQAAAAAAQAAAAEAAAAK7RhDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM1IjWXNSI1lc; MCITY=-131%3A; wapbaikedeclare=showed; ZFY=pPG3bwzEgam:AiYf0GxzrtubUXFIyIvmR:A3Cfhfafml8:C; RT="z=1&dm=baidu.com&si=c35e3ef0-648d-4062-bb77-3bb88abedd7e&ss=lx44rw7e&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=25b35&ul=22denb&hd=22df04"; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=images.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[A24tJn4Wkd_]=mk3SLVN4HKm; ab_sr=1.0.1_MTMxMjc1OTZkMWE3NmZmYjIzNjhkNTFjZTdmZmYzNjYzMDE1YWIwZjc2OWY0MWFkNTU1ZjhkNmIxNGNiOTkyOGNlMWQwMjEzOTY2OTZkYWZjMzRlNDYwM2FkNTA3MzJhNTczM2MxZmVkZTQ5ZTZhNmQzMDYzNTZiZmU5NDJjNWM4MmJhMmJlOTZlMmE0MTA0NzE0ZmRkZDVmNWFlOTc4Zg==; indexPageSugList=%5B%22%E7%89%A9%E7%90%86%E5%A4%A9%E5%B9%B3%22%2C%22%E5%A4%A9%E5%B9%B3%20%E5%AE%9E%E9%AA%8C%22%2C%22%E5%A4%A9%E5%B9%B3%20%E5%8C%96%E5%AD%A6%E5%AE%9E%E9%AA%8C%22%5D',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }  # 请求头，谷歌浏览器里面有，具体在哪里找到详见我上一条csdn博客
# 图片页面的url
# url = "https://images.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1717940906582_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E7%89%A9%E7%90%86%E5%AE%9E%E9%AA%8C+%E5%A4%A9%E5%B9%B3"
# url = "https://images.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1717941014982_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E6%89%98%E7%9B%98%E5%A4%A9%E5%B9%B3"
url = "https://images.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1717941174098_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E6%89%98%E7%9B%98%E5%A4%A9%E5%B9%B3+%E5%8C%96%E5%AD%A6"


# 通过requests库请求到了页面
html = requests.get(url, headers=header)
# 防止乱码
html.encoding = 'utf8'
# 打印页面出来看看
print(html.text)

html = html.text
pachong_picture_path = r"D:\new_program\pythonProject\pytorchUse\Knowledge\image"
if not os.path.exists(pachong_picture_path):
    os.mkdir(pachong_picture_path)

res = re.findall('"objURL":"(.*?)"', html)  # 正则表达式，筛选出html页面中符合条件的图片源代码地址url
for i in res:  # 遍历
    num = num + 1  # 数字加1，这样图片名字就不会重复了
    picture = requests.get(i)  # 得到每一张图片的大图
    file_name = r"D:\new_program\pythonProject\pytorchUse\Knowledge\image\\" + str(num+60) + ".jpg"  # 给下载下来的图片命名。加数字，是为了名字不重复
    f = open(file_name, "wb")  # 以二进制写入的方式打开图片
    f.write(picture.content)  # 往图片里写入爬下来的图片内容，content是写入内容的意思

    sleep(5)
    print(i)  # 看看有哪些url
f.close()  # 结束f文件操作