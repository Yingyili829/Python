#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>method 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
password_len = int(input("Enter the length of the password: "))
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
COMBINED_LIST = DIGITS + UPPERCASE + LOWERCASE + SPECIAL
#random.sample() 函数 它将从长度为 password_length 的 COMBINED_LIST 变量中获取随机字符。
#join() ，它将我们生成的密码连接到左侧的空字符串。
password = "".join(random.sample(COMBINED_LIST, password_len))
print(password)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>method 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
random_pwd="".join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%+=-_^&*.?ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',16))
print(random_pwd)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>method 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
def get_random_password():
# 16位的密码
    total = 16
# 2-3位字符，4-5位数字，4-5位大写字母，3-6小写字母
    num = random.randint(2,3)
    num1 = random.randint(4,5)
    num2 = random.randint(4,5)
    num3 = random.randint(total-num-num1-num2,total-num-num1-num2)
    password = random.sample('!~@_=?#$%^&*()-+.',num)
    password1 = random.sample('0123456789',num1)
    password2 = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',num2)
    password3 = random.sample('abcdefghijklmnopqrstuvwxyz',num3)
    
#print('{}:{}\n{}:{}\n{}:{}\n{}:{}'.format(num,password,num1,password1,num2,password2,num3,password3))
    newPasswordList = password + password1 + password2 + password3
    random.shuffle(newPasswordList)
    newPassword = ''.join(newPasswordList)
# print(newPassword)
    return newPassword