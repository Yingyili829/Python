#导入函数
import random
import time
print("---石头剪刀布猜拳游戏开始---")
time.sleep(1)
while True:
    #所有的出拳结果
    all_choice = ['石头', '剪刀', '布',4]
    # 玩家赢的组合结果
    win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
    #电脑出拳
    computer = random.choice(all_choice[0:3])
    print('请按下面的提示出拳：[1]石头/[2]剪刀/[3]布/[4]退出')
    time.sleep(0.5)
    try:
        # 从控制台获取玩家要出的拳
        my_list = int(input("""请输入您的选项: """))
        player = all_choice[my_list - 1]
        # 判断胜负
        if player == 4:
            print("您已退出，游戏结束！")
            break
        else:
            print("你出的是: %s，电脑出的是: %s" % (player, computer))
            ##输出带颜色的信息：\033[3开头的是字体颜色/[4开头的是背景色 [1m ##比;[0m更亮更粗 
            ##30白色 31红色 32黄色 33明黄色 34蓝色 35紫色 36青色
            #平局
            if player == computer:
                print('\033[32;1m平局\033[0m')
            #玩家赢
            elif [player, computer] in win_list:
                print('\033[31;1m你赢了！\033[0m')
            #电脑赢
            else:
                print('\033[34;1m电脑赢了！\033[0m')
    #玩家输入非法时
    except Exception as e:
        print("\033[36;1m输入有误，请输入1-4的整数进行猜拳！\033[0m")
