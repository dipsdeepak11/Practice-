# Program to find modulus without using modulus operator

def findModulus(number,oper):
    result=number - (oper * (number // oper))
    return result
    
#Testing above program
num1=133
oper1=23
print("result is %s",findModulus(num1,oper1))
    
num2=21
oper2=32
print("result is %s",findModulus(num2,oper2))
