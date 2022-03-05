#print('hello world')
#better calculator 
customer_input1=float(input('type in a number\n'))
op=input('which operation you would like to do?\n')
customer_input2=float(input('type in another number\n'))
if op=='+':
    print(customer_input1+customer_input2)
elif op=='-':
    print(customer_input1-customer_input2)
elif op=='*':
    print(customer_input1*customer_input2)
elif op=='/':
    print(f"result is {customer_input1/customer_input2}")
else:
    print('not suppotive to this, sorry')