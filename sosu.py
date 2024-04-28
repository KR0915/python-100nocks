def sosu(n):
    if n<1:
        print("素数ではない")
        return 
    
    for a in range(2,n):
        if n%a==0:
            print("素数ではない")
            return
    
    print("素数")
            
            
num1=int(input("数値を入力してください"))
sosu(num1)