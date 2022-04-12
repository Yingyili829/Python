
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for letter in start_text:
        position = list.index(letter)
        new_position = position + shift_amount
        end_text+= list[new_position]
        
    if cipher_direction == "decode" or cipher_direction == "encode":
        print(f"The {cipher_direction} test is {end_text}") 
    else: 
        print("\033[31;1mPlease type in encode or decode to execute the process\033[31;0m")
        

#call the function
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.

caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

