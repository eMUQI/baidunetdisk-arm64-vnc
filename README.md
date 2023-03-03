# [baidunetdisk-arm64-vnc](https://github.com/eMUQI/baidunetdisk-arm64-vnc)

<a href="https://hub.docker.com/r/emuqi/baidunetdisk-arm64-vnc">
<img alt="Docker Pull Count" src="https://img.shields.io/docker/pulls/emuqi/baidunetdisk-arm64-vnc"/>
</a>
<a href="https://github.com/eMUQI/baidunetdisk-arm64-vnc">
<img alt="Github Stars" src="https://img.shields.io/github/stars/emuqi/baidunetdisk-arm64-vnc?style=flat"/>
</a>

---

基于百 度网盘官方Linux-arm版本，安装在docker容器内，支持通过noVNC（网页）或者VNC访问。
支持树莓派4B arm64版本系统，理论上也支持其他arm64的设备。


## 部署方式

**Docker 部署**:
```bash
docker run -d \
       --name baidunetdisk-vnc \
       -p 5800:5800 \
       -p 5900:5900 \
       -v /配置文件位置:/config \
       -v /下载位置:/config/baidunetdiskdownload \
       --restart unless-stopped \
       emuqi/baidunetdisk-arm64-vnc:latest
```
其中需要修改的是`/配置文件位置:/config`和`/下载位置:/config/baidunetdiskdownload`，冒号前的路径修改为你希望储存位置。

如果希望用密码限制访问，在`-p 5900:5900 \`后加上`-e VNC_PASSWORD=password \`，等号后面写你要设置的密码。

运行成功后访问方式见：[使用方式](#使用方式)

**Docker-compose部署**:
```bash
# 创建文件夹用于存放docker-compose配置文件
mkdir baidunetdisk-vnc
# 进入 baidunetdisk-vnc 文件夹
cd baidunetdisk-vnc
# 下载docker-compose配置文件
wget https://raw.githubusercontent.com/eMUQI/baidunetdisk-arm64-vnc/main/docker-compose.yml
# 根据需要修改docker-compose配置文件
nano docker-compose.yml
# 以后台形式运行
docker-compose up -d
```
你可能希望修改`docker-compose.yml`里配置存放的位置`${PWD}/bdnetdisk-config:/config`和下载文件的位置`${PWD}/downloads:/config/baidunetdiskdownload`。修改冒号前的部分。

如果希望用密码限制访问，在`- GROUP_ID=1000 `后加上`- VNC_PASSWORD=password`，等号后面写你要设置的密码。

运行成功后访问方式见：[使用方式](#使用方式)


## 配置

|参数|说明|
|:-|:-|
| `--name=baidunetdisk` |容器名|
| `-p 5800:5800` |Web界面访问端口|
| `-p 5900:5900` |VNC协议访问端口。如果未使用VNC客户端，则为可选|
| `-v /配置文件位置:/config` |baidunetdisk配置文件位置|
| `-v /下载位置:/config/baidunetdiskdownload` |baidunetdisk下载路径|
| `-e VNC_PASSWORD=VNC密码` |VNC密码，默认为无|
| `-e USER_ID=1000` |uid设置，默认为1000|
| `-e GROUP_ID=1000` |gid设置，默认为1000|
| `-e NOVNC_LANGUAGE="zh_Hans"` |(zh_Hans\|en)设定novnc语言，默认为中文|

## 使用方式

有两种方法访问百度网盘客户端：
1. 运行成功可以在浏览器中访问noVNC端口，例如`http://localhost:5800`。
2. 或者通过VNC客户端来访问`vnc://localhost:5900`。

**注意**：如果百度网盘弹出升级提示，请忽略，点击升级按钮并不会执行程序升级而且新版本不一定有适配arm。可以将截图版本号提交到issue，我会根据适配情况维护升级。



## 感谢以下项目:

[https://github.com/jlesage/docker-baseimage-gui](https://github.com/jlesage/docker-baseimage-gui "https://github.com/jlesage/docker-baseimage-gui")    

[https://github.com/gshang2017/docker](https://github.com/gshang2017/docker "https://github.com/gshang2017/docker")