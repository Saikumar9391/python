print("prime number program")

def prime():
    a = int(input("enter a number to check whether it is prime number or not\n"))
    
    print("you entered:", a)
    
    if a <= 1:
        return False
        
    for divisor in range(2, a):
        if a % divisor == 0:
            return False  
    return True 

print("Is it prime?:", prime())