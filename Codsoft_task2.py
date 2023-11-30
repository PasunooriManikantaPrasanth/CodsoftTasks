a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))

operator=input("Enter the operator:")

if operator=='+':
    print(a,'+',b,'=',a+b)
    
elif operator=='-':
    print(a,'-',b,'=',a-b)
    
elif operator=='*':
    print(a,'*',b,'=',a*b)
    
elif operator=='/':
    print(a,'/',b,'=',a/b)
    
elif operator=='%':
    print(a,'%',b,'=',a%b)
    
else:
    print("Invalid operator")
