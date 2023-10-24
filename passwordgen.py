import random
uppercase_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
loweecase_letter="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="()[]{,.-/\_@!#$%^&*()?}"
upper,lower,nums,syms=True,True,True,True
all=""

if upper:
    all+=uppercase_letter
if lower:
    all+=loweecase_letter
if nums:
    all+=digits
if syms:
    all+=symbols
    
length=20
amount=10


for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)
    
   
