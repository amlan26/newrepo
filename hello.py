def fac(n):
 if n == 0:
    return 1
  else 
    return n * fac(n - 1)
    
no = 5
res = fac(no)
print(f"The factorial of {no} is {fac}")
