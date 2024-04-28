def fiftyseven():
    n=int(input("受験者数を入力せよ"))
    english_total=0
    math_total=0
    japanese_total=0
    for a in range(n):
        english,math,japanese=map(int,input().split())
        