# chang_e_V_simulater
This project is created to simulate(joke) Chang_e_V`s sampling on moon. (Aha)
这个程序是用来模拟嫦娥5号进行月面土壤采样并返回的过程
程序使用Python3.7实现
使用有限状态机来模拟程序运行过程
将探测器分为环绕器，返回器，着陆器和上升器四个实例
程序模拟从探测器完成地月轨道转移开始，到最终返轨组合体进入月地转移轨道为止（流程参照了嫦娥5号全工作流程时间表）
每个实例分为就绪、等待、工作、完成这四个状态（由于未找到故障处理相关资料，故此处不考虑流程中出现故障的情况）
程序入口：main.py
相关依赖：见requirement.txt

***注：程序中出现了中文，在某些环境下会出现中文乱码的问题，可以使用UTF-8格式打开，程序运行使用cmd（windows）或terminal（linux）内直接用python main.py运行***
2020.12.13 By Dylan He
