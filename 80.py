#2つの正の整数値を入力させ、互いに素であるか判定するプログラムを作成せよ。なお、2つの正の整数が互いに素とは、1以外に共通公約数を持たない関係のことである。
a=int(input("最初の数を入力してください"))
b=int(input("二つ目の数を入力してください"))

coprime=True

if a>b:
    for c in range(2,a+1):
        if a%c==0 and b%c==0:
            print('互いに素ではない')
            coprime=False
            break
else:
    for c in range(2,b+1):
        if a%c==0 and b%c==0:
            print('互いに素ではない')
            coprime=False
            break
            
if coprime==True:
    print("互いに素である")