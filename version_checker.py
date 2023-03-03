import requests
import time

# 定义需要检测的版本号范围
min_version = [4, 0, 0]
max_version = [4, 18, 0]

# 定义请求延时时间（秒）
request_delay = 0.5

# 格式化网址，用于替换版本号
url_template = 'https://issuepcdn.baidupcs.com/issue/netdisk/LinuxGuanjia/{0}/baidunetdisk_{0}_arm64.deb'


def check_version(version):
    """检测指定版本号是否可用"""
    url = url_template.format('.'.join(str(v) for v in version))
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


def find_latest_version(min_version, max_version):
    """寻找最新版本号"""
    for i in range(max_version[0], min_version[0] - 1, -1):
        for j in range(20, -1, -1):
            if j > max_version[1] and i == max_version[0]:
                continue;
            for k in range(20, -1, -1):
                if k > max_version[2] and j == max_version[1] and i == max_version[0]:
                    continue;
                version = [i, j, k]
                # 检测指定版本号是否可用
                if check_version(version):
                    print('version {0} is available'.format('.'.join(str(v) for v in version)))
                    time.sleep(request_delay)
                    # 判断是否为最新版本
                    if version[0] > min_version[0] or version[1] > min_version[1] or version[2] > min_version[2]:
                        return version
                else:
                    print('version {0} is not available'.format('.'.join(str(v) for v in version)))
                    time.sleep(request_delay)
    # 找不到可用版本号，返回None
    return None


# 寻找最新版本号
latest_version = find_latest_version(min_version, max_version)
if latest_version is not None:
    print('The latest version is {0}'.format('.'.join(str(v) for v in latest_version)))
else:
    print('No available version found')
