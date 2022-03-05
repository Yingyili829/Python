
secret_num=77
guess=None #storage for user input

#only 3 guess and all the requirement
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num !=guess and not(out_of_limit):
    guess_count+=1
    if guess_count<=guess_limit:
        guess=int(input("what number you would like make a guess "))
        if guess > secret_num:
            min_larger=secret_num-10
            max_larger=guess
            print(f"the range is {min_larger} to {max_larger}")
        elif guess < secret_num:
            print('larger')
        else: print("congrats")
    else: 
            out_of_limit = True
    
    if out_of_limit ==True: print('Sorry, out of guess limit, you lost')

