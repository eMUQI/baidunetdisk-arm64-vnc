# baidunetdisk-arm64-vnc

基于百度网盘官方Linux版本，安装在docker容器内，支持通过noVNC或者VNC访问。
支持 树莓派4B arm64版本系统，理论上也支持其他arm64的设备。

## 版本

|名称|版本|说明|
|:-|:-|:-|
|baidunetdisk|4.14.6|arm64|

## Docker 用例

1. 下载镜像

       docker pull emuqi/baidunetdisk-arm64-vnc:latest
   

2. 创建baidunetdisk容器

       docker create \
              --name=baidunetdisk-vnc \
              -p 5800:5800 \
              -p 5900:5900 \
              -v /配置文件位置:/config \
              -v /下载位置:/config/baidunetdiskdownload \
              --restart unless-stopped \
              emuqi/baidunetdisk-arm64-vnc:latest

3. 运行

       docker start baidunetdisk-vnc

4. 停止

       docker stop baidunetdisk-vnc

5. 删除容器

       docker rm baidunetdisk-vnc

6. 删除镜像

       docker image rm baidunetdisk-arm64-vnc:latest

7. 通过浏览器5800端口访问，或者通过VNC在5900访问。


## 感谢以下项目:

[https://github.com/jlesage/docker-baseimage-gui](https://github.com/jlesage/docker-baseimage-gui "https://github.com/jlesage/docker-baseimage-gui")    

[https://github.com/gshang2017/docker](https://github.com/gshang2017/docker "https://github.com/gshang2017/docker")