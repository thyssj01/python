num = int(input("출력하고 싶은 단을 입력하세요(2~9):"))

for i in range(1, 10):
     if (num<2) or (num>9):
        print("단을 잘 못 입력하셨습니다.")
        break
     print(num,"*",i,"=",(num*i))