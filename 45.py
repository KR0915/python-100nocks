#初乗り料金が1700mまで610円、それ以降は313mごとに80円のタクシーがある。このタクシーに乗った距離をm単位で入力し、料金を計算するプログラムを作成せよ。
import math
a=int(input("距離を入力せよ"))
if a<1700:
    print(610)
else:
    result=math.ceil((a-1700)/313)*80+610
    print(result)