#３つの整数値を入力させ、3つの値のうち2番目に大きい値を表示するプログラムを作成せよ。
a=int(input("最初の数を入力してください"))
b=int(input("二番目の数を入力してください"))
c=int(input("三番目の数を入力してください"))

if a>b and b>c:
    print(b)
elif c>b and b>a:
    print(b)
elif b>a and a>c:
    print(a)
elif c>a and a>b:
    print(a)
elif a>c and c>b:
    print(c)
elif b>c and c>a:
    print(c)