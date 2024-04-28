#整数値を3つ入力させ、それらの値が小さい順（等しくてもよい）に並んでいるか判定し、小さい順に並んでいる場合はOK、そうなっていない場合はNGと表示するプログラムを作成せよ。
def checker(a,b,c):
    if c>=b>=a:
        print("OK")
    else:
        print("ERROR")
        
num1=int(input("1つめの数字を入力してください"))
num2=int(input("2つ目の数字を入力してください"))
num3=int(input("3つ目の数字を入力してください"))

checker(num1,num2,num3)