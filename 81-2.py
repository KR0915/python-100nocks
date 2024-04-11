a = int(input("最初の数を入力してください: "))
b = int(input("二番目の数を入力してください: "))
c = int(input("三番目の数を入力してください: "))

# 3つの数をリストにしてソートし、2番目に大きい数を出力する
numbers = [a, b, c]
numbers.sort()
print("2番目に大きい数は:", numbers[1])
