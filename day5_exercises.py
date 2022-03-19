
#For Loop
#for number in range(a,b) --- a-(b-1)
###print(number)

# range(1,20)
# range(1,20,3) - 3 is interval 


#calculate all the even numbers

from ast import Break

#method1 - range(a.b.interval)
total = 0
for number in range(2,101,2):
    total+= number
print(total)

#method2 - %2
total2 = 0
for number in range(1,101):
    if number %2==0:
        total2+= number
print(total2)

#FizzBuzz game
# %3==0 - fizz
# %5==0 - buzz
# %3==0 and %5==0 - fizzBuzz
#move up /down for the excusetion 

for number in range(1,101):
    if  number %3==0 and number %5==0:
        print('FizzBuzz')
    elif number %5==0:
        print('Buzz')
    elif number %3==0:
        print('Fizz')
    else:
        print(number)