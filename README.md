# umdfaces2VOC2007
##Mattzheng 注明

forked from luuuyi，其中test.py内容需要进行修正。

* 新增了图像另存到文件夹:JPEGImages的功能：
```
cv2.imwrite(IMGSTORE+jpg_file,img,[int(cv2.IMWRITE_JPEG_QUALITY),95])
```
* 同时，原作者本来base=3000000这里，如果第二个文件夹开跑就需要另外的起点base，需要注意。

Mattzheng 2017-5-4

## Description
将umdfaces数据库做成VOC2007格式，方便深度学习训练，umdfaces数据库的下载地址为：[umdfaces](http://www.umdfaces.io/)

项目一共包含三个脚本文件：

* tool_csv.py: 封装了csv模块读取文件函数
* tool_lxml.py: 封装了lxml模块用于生成VOC2007格式的xml文档的函数
* test.py: 主函数，用于读取文件路径做初始化

## Dependencies

* Python2.7或者更高版本
* python lxml，numpy，cv2

## Tips
在安装python依赖模块的时候，国内的小伙伴可以使用豆瓣的镜像通过pip下载(root用户)：
```
cd ~ && mkdir .pip && cd .pip
vim pip.conf
```

在其中加上：
```
[global]
index-url = http://pypi.douban.com/simple/
trusted-host = pypi.douban.com
```

之后就可以愉快的下载python模块了

## Contact
* 邮件(21515006#zju.edu.cn, 把#换成@)
* QQ: 435977170
