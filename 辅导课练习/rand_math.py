import random
import math

'''
输入一个三位数 与程序数随机数比较大小
如果大于程序数 分别输出这个三位数的个位十位百位

如果等于随机数 则提示中奖 记1000fen
如果小于随机数 则将120个字符输入到文本文件中（规则是每一个字符串长度为12，单独占一行，并且前四个是字母，后八个 是数字）

'''

class GameNum():
    def line(self):
        str_num =''
        for i in range(4):
            num = random.randrange(97,123)
            str_s = chr(num)
            str_num = str_num+str_s
            #print(str_num)
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num+str(num)
        #print(str_num)
        return str_num



    def num_game(self):
        source = 0

        total = 0

        while 1:

            num = input("请输入一个三位数，shuru-1结束:")
            if num =='-1':
                break
            random_num =random.randrange(100,1000)

            if num.isdigit() and 100<=int(num)<=999:
                total += 1
                print('输入%d次'%total)
                num = int(num)
                random_num = int(random_num)
                if num > random_num:

                    bai = int(num)//100
                    shi = num%100//10
                    ge = num%10
                    print('你输入的 数  比程序随机数大，程序随机数是',random_num)
                    print('这个数的百位是{},十位是{},个位是{}'.format(bai,shi,ge))

                if num == random_num:
                    source = source +100
                    print('你中奖了，目前分数为',source)
                    print('你中奖的概率是多少',source/total)
                if num < random_num:
                    print('你输入的数比程序随机数小，程序随机数是', random_num)
                    for i in range(10):
                        str_line = GameNum.line(0)
                        print(str_line)
                    '''with open('str_num.txt','a') as f:
                            f.write(str_line+'\n')
                    '''

            else:
                print('请按规定输入')


if __name__ == '__main__':
    source = 0

    total = 0
   #GameNum.num_game(0)
    game = GameNum()
    game.num_game()
