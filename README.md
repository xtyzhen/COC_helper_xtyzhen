**简体中文**  |  [English](https://github.com/xtyzhen/COC_helper_xtyzhen/blob/main/README(English).md)  
***
# 介绍  
COC_helper_xtyzhen是一款可以运行于Windows模拟器下部落冲突的自动捐兵辅助程序。使用python编写，基于pyautogui图像识别。  
***
#核心更新内容
1.增加多线程图像识别模块，进一步提高捐兵速度
2.自动发送友谊战功能
3.随APP更新图像
***
# 代码功能
## 1.	自动捐兵  
可自定义捐赠兵种、顺序。  
## 2.	自动造兵  
自动补充已捐赠军队、法术、攻城。  
## 3.	自动采集  
## 4.	多端登录协调  
多设备载入辅助自动暂停15分钟。  
## 5.	断线重连  
网络异常、断线停顿1.5-3.5秒重连。  
## 6.	4小时在线检测  
4小时强制下线后，等待6分钟重连即可恢复30分钟村庄守卫和在线时长，等待15分钟重连可恢复4小时护盾。（默认等待15分钟重连）  
## 7.	支持单设备多账号  
支持单台电脑多开模拟器，自动均衡捐兵。  
***
# 使用方法  
下载并安装Anaconda3-2020.07-Windows-x86_64.exe（[mirror in China](https://mirrors.bfsu.edu.cn/anaconda/archive/Anaconda3-2020.07-Windows-x86_64.exe)）  
Tips:如果需要修改识别兵种和顺序，需要在locate.py第235行修改编号。编号释义在第18行中给出。
~~~
pip install opencv-python pyautogui  
git clone https://github.com/xtyzhen/COC_helper_xtyzhen.git  
cd ./COC_helper_xtyzhen
python locate.py  
~~~
