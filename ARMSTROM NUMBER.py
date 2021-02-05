#  PROGRAM FOR VERIFY GIVEN NUMBER IS Armstrom Number OR NOT

num = int(input("ENTER THE NUMBER :"))
sum = 0
temp = num
while temp >0:
    digit = temp%10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num ,"is an Aromstron number")

else :
    print(num ,"is not Armstong number")
