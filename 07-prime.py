print("prime no. indentifications")

num = int(input("enter your no: " ))
if num > 1 :
    for i in range(2, num):
        if num % i == 0:
            print("its is not a prime number")
            break

        else:
            print("its is a prime number")
            break    
        
if num == 1:
    print("1 is neither prime nor composite")