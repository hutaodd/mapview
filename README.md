## 使用指南

### 在线使用

[数据地图标点 · Streamlit (mapview-uek8gr3l3ws.streamlit.app)](https://mapview-uek8gr3l3ws.streamlit.app/)

### 数据说明

本脚本基于streamlit实现地图数据标点

| 任务号码 | Latitude    | Longitude   | 任务标价 | Status |
| -------- | ----------- | ----------- | -------- | ------ |
| A0001    | 22.56614225 | 113.9808368 | 66       | 0      |
| A0002    | 22.68620526 | 113.9405252 | 65.5     | 0      |
| A0003    | 22.57651183 | 113.957198  | 65.5     | 1      |
| A0004    | 22.56484081 | 114.2445711 | 75       | 0      |
| A0005    | 22.55888775 | 113.9507227 | 65.5     | 0      |
| A0006    | 22.55899906 | 114.2413174 | 75       | 0      |
| A0007    | 22.54900371 | 113.9722597 | 65.5     | 1      |
| A0008    | 22.56277351 | 113.9565735 | 65.5     | 0      |

数据表中对应列应如上表所示，分别对应列头有Latitude(纬度) Longitude(经度) Status(状态,0:未完成,1:已完成)

### 环境说明

在安装好python后，在当前文件夹，shift+右键，在当前目录调出命令提示符输入一下命令安装依赖

`pip install -r requirements.txt `

### 运行说明

在安装好运行环境后，继续在当前命令提示符目录下运行以下命令

`streamlit run map.py`

命令运行后将自动打开浏览器，按提示使用即可