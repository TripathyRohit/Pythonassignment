# python program to check armstrong number

def armstrong (num):
    l = len (str(num)) #claculate how many digits are there in given num
    a = num #num is copied to 'a' coz it ll reducted to 0 for performing func
    sum = 0
    while a > 0:
        rem = a%10 
        a = a//10
        sum  += rem**l #every time previous sum is added to new remainder
    if sum == num:
        return True
    else :
        return False
    
num =  int(input('Enter the positive integer :'))
print (armstrong (num))
