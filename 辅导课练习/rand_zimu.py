
class GameZimu():

    def a(self):
        for i in range(1,6):
            for k in range(5-i):
                print(' ',end="")

            for j in range(1,i+1):
                if i ==1 or i == 3 or j ==1 or j ==i:
                    print('*',end=" ")
                else:
                    print(' ',end = " ")
            print()

    def b(self):
        for i in range(1,4):
            for j in range(1,4):
                if i ==1 or i ==4 or j==1:
                    if j <3:

                        print('*',end = " ")
                elif j ==3:
                    if i ==2 or i ==3:
                        print('*',end = " ")
                else:
                    print(' ',end=" ")
            print()

        for i in range(1,5):
            for j in range(1,4):
                if i ==1 or i ==4 or j==1:
                    if j <3:

                        print('*',end = " ")
                elif j ==3:
                    if i ==2 or i ==3:
                        print('*',end = " ")
                else:
                    print(' ',end=" ")
            print()


    def d(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print('*', end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print('*', end=" ")
                else:
                    print(' ', end=" ")
            print()


    def c(self):
        for i in range(1,5):
            for j in range(1, 4):
                if j== 1:
                    if i ==2 or i ==3:
                        print('*', end=" ")
                    else:
                        print(' ', end=" ")
                elif i ==1 or i ==4:
                    if j ==1:
                        print(' ', end=" ")
                    else:
                        print('*', end=" ")
                else:
                    print(' ',end = " ")
            print()
    def e(self):
        for m in range(1,8):

            for n in range(1,4):
                if m ==1 or m==4 or m ==7 or n ==1:
                    print('*', end=" ")
                else:
                        print(' ',end=" ")
            print()


    def f(self):
        for m in range(1, 8):

            for n in range(1, 4):
                if m == 1 or m == 4   or n == 1:
                    print('*', end=" ")
                else:
                    print(' ', end=" ")
            print()

    def g(self):
        for m in range(1,6):
            for n in range(1,5):
                if m ==1 or m == 4:
                    if n ==1:
                        print(' ',end=" ")
                    else:
                        print('*',end=" ")
                elif m==2 and n ==1:

                    print("*",end=" ")
                elif m==3:
                    if n ==2:
                        print(' ',end=" ")
                    else:
                        print('*',end=" ")
                else:
                    print(' ',end=" ")

            print()


    def h(self):
        for m in range(1,6):
            for n in range(1,4):
                if m ==3 or n ==1 or n==3:
                    print('*',end=" ")
                else:print(' ',end=" ")
            print()

    def i(self):
        for m in range(1,6):
            for n in range(1,4):
                if m ==1 or m ==5 or n ==2:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    def j(self):
        for m in range(1,6):
            for n in range(1,5):
                if m ==1 or n ==3:
                    if m <5:
                        print('*',end=" ")
                elif m ==5 and n ==2:
                    print('*',end=" ")
                elif m == 4 and n == 1:
                    print('*', end=" ")

                else:
                    print(' ',end=" ")

            print()


    def k(self):
        for m in range(1,3):
            for n in range(m,4):
                if m ==1 and n ==2:
                    print(' ',end=" ")
                else:
                    print('*',end=" ")

            print()
        for m in range(1,4):
            for n in range(m):
                if m ==3 and n ==1:
                    print(' ', end=" ")
                else:
                    print('*',end=" ")
            print()

    def l(self):
        for m in range(1,8):
            for n in range(1,4):
                if  m ==7 or n ==1:
                    print('*',end=" ")

                else:
                    print(' ',end=" ")
            print()


    def m(self):

        for m in range(1,6):
            for n in range(1,6):
                if m ==1 or n == 1 or n ==3 or n==5:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")

            print()

    def n(self):

        for m in range(1,6):
            for n in range(1,4):
                if m == 1 or n ==1 or n ==3:
                    print('*',end=" ")
                else:
                    print(' ', end=" ")

            print()


    '''def zimu_game(self):
        zimu = input('请输入大写字母A-N')
        if 
    '''