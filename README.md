appium+python+KW 自动化测试框架
====
1.项目概述
-------
python2.7编写，使用目前较为流行的UI自动化测试工具Appium，关键字模型。用excel管理测试用例，并将运行结果写入excel文件中，
init文件管理元素定位，对操作步骤进行封装。支持多线程，可同时在多台设备运行。

2.目录简介
-------
* 2.1 base：存放基础封装，如driver。
* 2.2 config：配置相关，包括测试用例、定位信息和启动命令信息。
* 2.3 jpg：错误截图，用例执行过程中，如果失败会截图保存。
* 2.4 untils： 公共的工具模块。
* 2.5 run_main.py：程序入口


3.效果展示图
-------
整体结构
###
![](https://github.com/hanyguoguo/appiumPythonKW/blob/master/img/KWtree.png)

测试用例
###
![](https://github.com/hanyguoguo/appiumPythonKW/blob/master/img/case.png)

测试结果
###
![](https://github.com/hanyguoguo/appiumPythonPO/blob/master/img/result.png)


4、不足和优化
-------
用例的组织不太灵活，可根据项目实际需要进行组织；异常处理及日志较为简陋，需要进一步优化。等

