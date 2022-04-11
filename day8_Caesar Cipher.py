
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = list.index(letter)
        new_position = position + shift_amount
        new_letter = list[new_position]
        cipher_text+= new_letter
    print(f"The encoded test is {cipher_text}")



def decrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = list.index(letter)
        new_position = position - shift_amount
        new_letter = list[new_position]
        cipher_text+= new_letter
    print(f"The decoded test is {cipher_text}")


#call the function
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.
if direction == "encode" :
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text,shift_amount=shift)
else: 
    print("please type in encode or decode to execute the process")

