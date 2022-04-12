
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#when 
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in list:
            position = list.index(char)
            new_position = position + shift_amount
            end_text+= list[new_position]
        else:
            end_text+= char #append the actual char witout any modification
#type in wrong direction        
    if cipher_direction == "decode" or cipher_direction == "encode":
        print(f"The {cipher_direction} test is {end_text}") 
    else: 
        print("\033[31;1mPlease type in encode or decode to execute the process\033[31;0m")

#check if we need to go into the loop
#make it in a loop 
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    #if shift input is over 26
    if shift_input > 26:
        shift= shift_input % 26       
    caesar(start_text=text,shift_amount=shift_input,cipher_direction=direction)

    check_if_need_to_continue = input("Type in 'Yes' for playing again, or type in 'No' \n").lower() 
    if check_if_need_to_continue =='yes':
        should_continue = True
    else: 
        print("\033[31;1mGoodbye\033[31;0m")
        break



    #call the function
    # A parameter is the variable listed inside the parentheses in the function definition.
    # An argument is the value that are sent to the function when it is called.
