# CoolQ-couplet

## 酷Q用对对联机器人

## 该插件调用：https://ai.binwang.me/couplet/

## 使用的Python SDK：http://git.oschina.net/muxiaofei/cq_python_sdk ，所以需要环境VC++ 2010

因为这是个开源项目，所以其实我很想自己搭，而不是这样调用原作者的网站。

原作者：用1080ti跑了四天

我：GG。965M，强行跑得半个月。。。

## 使用方法：

1.酷Q开启开发模式（在插件管理界面疯狂点右下角的版本号）

2.文件夹、dll、json扔app文件夹里去，再把exe扔跟目录下。应该需要已经安装好Chrome浏览器

3.重启酷Q，启动插件

4.看到黑框跳出来，等到他码了一堆东西之后，基本就能用了

5.%对对联问天下头颅几许 答：看老夫手段如何

### 其实就是模拟开了个Chrome，然后输入上联，按按钮，得到下联。所以黑框要一直开着


## PS:这个Python的SDK不支持多线程，而且实践表明，不能同时使用一个以上的该SDK编写的插件。所以如果有的话，多合一吧

移植的时候注意python2.7文件夹里的lib文件夹，里面有需要的第三方库
