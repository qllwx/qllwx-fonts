# qllwx-fonts
## 直接使用 
### 下载TTF
- [qllwx-font1](https://github.com/qllwx/qllwx-fonts/raw/main/fonts/qllwx_font1.ttf)
### 在系统安装字体
- windows [add font](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)

## 制作方法

### 方法一
#### 采用本程序制作手写字体
正在开发中。。。
### 方法二 
#### 北大字体自动生成
- 登录[北京大学计算机科学技术研究所 手写字体自动生成系统](http://www.flexifont.com/flexifont-chn/login/)
- 下载模板 打印模板
- 填写模板  扫描上传
~~~
在扫描后，可用程序实现批量剪切、转置
~~~
- 生成字体  下载安装

##  编码
UTF-8有点类似于Haffman编码，它将Unicode编码为：
0x00-0x7F的字符，用单个字节来表示；
0x80-0x7FF的字符用两个字节表示；
0x800-0xFFFF的字符用3字节表示；
汉字的unicode范围是：0x4E00~0x9FA5
其实这个范围还包括了中，日，韩的字符。
