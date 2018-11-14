
from 辅导课练习 import rand_math
from 辅导课练习  import rand_zimu
print('请选择游戏(输入1)\n1.数字游戏\n2.字母游戏')
game = input('输入1或2')
if game == '1':
    game_num = rand_math.GameNum()
    game_num.num_game(0,0)
elif game == '2':
    game_zimu = rand_zimu.GameZimu()
    game_zimu.a()

else:
    print('输入错误')

#可以啦
"""
导入包的时候一定得注意路径
有相对路径和绝对路径
一般写的时候从父目录开始导入
你的父目录要是设置为辅导联系的话可以这样导入 from rand_math import GameNum
或者通过包管理方式添加__init__文件可以直接导入
可能你还没学习到包的管理
ok
"""

