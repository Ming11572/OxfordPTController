# OxfordPTController
A GUI program for controlling Oxford testralonPT refrigeration. Different device configurations may require appropriate code modifications

Acquire NI 488.2 driver　(ni-488.2XXX offline or other version)
"https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html#575749"

#　install python package
```console
pip install numpy==2.2.4
pip install pyside6==6.8.2.1
pip install matplotlib==3.10.1
pip install pyvisa==1.14.1
```
# 使用
1. 运行 “ pt_controller.py ”文件中的 main函数，正常情况会有如下弹窗：

![image.png](pics/image.png)

2. 单击 **Log Addr** 选择用于存放Log files的文件夹。
3. 输入三个控制器的地址，示例中三个控制器均使用LAN口连接，ips为磁体控制器，itc/he3为插杆的温控仪。
4. 单击 connect，如果是第一次使用，会弹出设置窗口，根据实际情况进行设置(如果已经设置过了，在主窗口中点setting可进行修改。

![img.png](pics/img.png)

如果之前已经设置过 setting，且设备连接正常，会弹出主窗口：

![img_1.png](pics/img_1.png)

5.Warm/Cool按钮可用于一键升降温，单击Abort按钮可中止升/降温。

6.Logs按钮可查看历史温度，加热器功率，磁体等。其他debug信息可在步骤2中选择文件夹中查看。

# API使用 示例
使用API之间需要运行控制程序，并与制冷机建立连接。

```jupyter
from api_for_PT_controller import PTClient
client = PTClient("localhost", 19020)
```

```jupyter
client.get_magnet()
```

```jupyter
client.get_temperature()
```

更多请查看api_for_PT_controller.py文件




