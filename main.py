# -*- coding: UTF-8 -*-
#Auther Li Mengxing
#descrpition:程序主入口
import time
from transitions import Machine
from surround import surround
from back import back
from land import land
from launch import launch
#from surround import transitions, states

# model = surround()
# model2 = back()
#分别创建四个实例
surrounder = surround()
backer = back()
lander = land()
launcher = launch()

#状态定义
status = ['READY','WAITING','WORKING','DONE']

#设置状态转移
transitions = [
    {'trigger': 'initialed', 'source': 'READY', 'dest': 'WAITING' },
    {'trigger': 'wating_over', 'source': 'WAITING', 'dest': 'WORKING' },
    {'trigger': 'work_done', 'source': 'WORKING', 'dest': 'DONE' },
    {'trigger': 'ready','source':'DONE','dest':'READY'}
]

#分别设置各自的状态机

surrounder_machine =Machine(model = surrounder,states=status,transitions=transitions,initial='READY')
backer_machine =Machine(model = backer,states=status,transitions=transitions,initial='READY')
lander_machine =Machine(model = lander,states=status,transitions=transitions,initial='READY')
launcher_machine =Machine(model = launcher,states=status,transitions=transitions,initial='READY')

#着上与返轨组合体分离
#主要为着陆器与返回器进行工作，之后由轨道器开始工作
def lan_lan_leave_step():
    #首先对两个实例进行检查操作
    time.sleep(0.5)
    lander.initialed()
    if(lander.state=="WAITING"):
        print("着陆器检测完成，等待下一步工作")
    else:
        print("着陆器故障，请检查")
        return 0
    time.sleep(0.5)
    backer.initialed()
    if(backer.state=="WAITING"):
        print("返回器检测完成，等待下一步工作")
    else:
        print("返回器故障，请检查")
        return 0
    #返回器打开与着陆器链接
    backer.wating_over()
    if(backer.state=="WORKING"):
        print("正在打开连接……")
        time.sleep(2)       
    else:
        print("打开失败，请检查")
        return 0
    #完成打开工作,返轨组合体进行绕月操作
    backer.work_done()
    print("返轨组合体准备进行绕月操作>>>>")
    time.sleep(1)
    #完成工作后立刻进入就绪态
    backer.ready()
    #首先对轨道器实例进行检查操作
    surrounder.initialed()
    if(surrounder.state=="WAITING"):
        print("轨道器检测完成，等待下一步工作")
    else:
        print("轨道器故障，请检查")
        return 0
    #着陆器开始准备降落
    surrounder.wating_over()
    time.sleep(1)
    if(surrounder.state=="WORKING"):
        print("轨道器运行，轨道器正在沿着月球运行>>>")
        time.sleep(2)
    else:
        print("无法完成绕行，请检查")
        return 0

    #着陆器离开返回器，开始进行下一步工作
    lander.wating_over()
    if(lander.state=="WORKING"):
        print("着陆器正在离开返回器……")
        time.sleep(2)
    else:
        print("分离失败失败，请检查")
        return 0
    lander.work_done()
    print("成功分离，开始进行降轨变轨")
    time.sleep(1)
    #完成工作后立刻进入就绪态
    lander.ready()

#该函数主要进行降落操作
#主要为着陆器进行工作
def landing():
     #首先对实例进行检查操作
    lander.initialed()
    if(lander.state=="WAITING"):
        print("着陆器检测完成，等待下一步工作")
    else:
        print("着陆器故障，请检查")
        return 0
    #着陆器开始准备降落
    lander.wating_over()
    time.sleep(1)
    if(lander.state=="WORKING"):
        print("着陆器正在降落……")
        time.sleep(2)
    else:
        print("无法完成降落，请检查")
        return 0
    lander.work_done()
    print("完成降落，开始进行采样")
    #完成工作后立刻进入就绪态
    lander.ready()

#该函数主要进行土壤采集和封装
#主要为着陆器和上升器进行工作
def sampling():
     #首先对实例进行检查操作
    lander.initialed()
    if(lander.state=="WAITING"):
        print("着陆器检测完成，等待下一步工作")
    else:
        print("着陆器故障，请检查")
        return 0
    #着陆器开始准备采样
    lander.wating_over()
    time.sleep(1)
    if(lander.state=="WORKING"):
        print("着陆器正在进行采样与封装……")
        time.sleep(2)
    else:
        print("无法完成采样，请检查")
        return 0
    lander.work_done()
    print("完成采样封装")
    #完成工作后立刻进入就绪态
    lander.ready()
    #上升器开始工作
    launcher.initialed()
    if(launcher.state=="WAITING"):
        print("上升器检测完成，等待下一步工作")
    else:
        print("上升器故障，请检查")
        return 0
    #上升器接收采样
    launcher.wating_over()
    time.sleep(1)
    if(launcher.state=="WORKING"):
        print("上升器接收采样中……")
        time.sleep(2)
    else:
        print("无法完成起飞，请检查")
        return 0
    launcher.work_done()
    print("上升器已接收采样")
    #完成工作后立刻进入就绪态
    launcher.ready()


#该函数用于模拟上升器返回轨道的过程
#主要的工作实例为上升器
def launching():
     #首先对实例进行检查操作
    launcher.initialed()
    if(launcher.state=="WAITING"):
        print("上升检测完成，等待下一步工作")
    else:
        print("上升器故障，请检查")
        return 0
    #上升器开始准备起飞
    launcher.wating_over()
    time.sleep(1)
    if(launcher.state=="WORKING"):
        print("上升器正在起飞")
        time.sleep(2)
    else:
        print("无法完成起飞，请检查")
        return 0
    launcher.work_done()
    print("上升器正在向轨道运行器接近>>>>")
    #完成工作后立刻进入就绪态
    launcher.ready()

#该函数用于模拟上升器将月球地面样本传递给轨返组合体的过程
#主要的工作实例为上升器和返回器
def get_sample():
    #首先对两个实例进行检查操作
    time.sleep(0.5)
    launcher.initialed()
    if(launcher.state=="WAITING"):
        print("上升器检测完成，等待下一步工作")
    else:
        print("上升器故障，请检查")
        return 0
    time.sleep(0.5)
    backer.initialed()
    if(backer.state=="WAITING"):
        print("返回器检测完成，等待下一步工作")
    else:
        print("返回器故障，请检查")
        return 0
    #返回器接收样本，
    backer.wating_over()
    if(backer.state=="WORKING"):
        print("正在接收样本……")
        time.sleep(2)       
    else:
        print("打开失败，请检查")
        return 0
    #接收到样本，开始抛弃上升仓和对接舱
    #上升器离开返回器，被抛弃
    launcher.wating_over()
    if(launcher.state=="WORKING"):
        print("上升器正在离开返回器……")
        time.sleep(2)
    else:
        print("分离失败失败，请检查")
        return 0
    launcher.work_done()
    print("成功分离，上升器被抛弃")
    time.sleep(1)
    #完成工作后立刻进入就绪态
    launcher.ready()
    backer.work_done()
    print("返轨组合体开始返回地球>>>>")
    time.sleep(1)
    #完成工作后立刻进入就绪态
    backer.ready()
    
#该函数用于封装程序的主入口
#用于模拟一次完整运行的效果
#用户可以在其中调用各个实例的states，以观察在程序运行过程中不同部分的运行状态
def main():
    print("模拟开始")
    print("|********************************|")
    time.sleep(1)
    print("嫦娥5号接近月球，开始进行分离操作")
    #调用函数模拟分离操作
    lan_lan_leave_step()
    time.sleep(5)
    print("准备降落……")
    #调用函数模拟降落操作
    landing()
    time.sleep(5)
    print("成功到达月球")
    #调用函数模拟采样与封装操作
    sampling()
    time.sleep(5)
    print("完成采样，开始返回")
    #调用函数模拟上升器返回操作
    launching()
    time.sleep(5)
    print("将样本传递给返轨组合体")
    调用函数模拟返轨综合体接收样本并返回的过程
    get_sample()
    time.sleep(5)
    print("样本开始返回地球")
    print("|********************************|")
    print("模拟结束")


if  __name__ == "__main__":
    main()
    

    
    
    

