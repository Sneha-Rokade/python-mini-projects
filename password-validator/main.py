# 1. password should contain 8 characters length should be 8

# str1 = "Heelo"

# def passwd(p):
#     if str1 == p:
#         return "Valid password"
#     else:
#         return "Invalid password"

# print(passwd("Heelo"))


# password = "Lo123"
enter_password = input("Enter password : ")
len_password = "########"
password_len = len(len_password)
upper_found = False
lower_found = False

passwd_len = len(enter_password)

for ch in enter_password:
    if ch.isupper():
        upper_found = True
    if ch.islower():
        lower_found = True

if passwd_len > password_len:
    print("Strong password")
elif passwd_len == password_len:
    print("Good Password")
else:
    print("Weak password")

if upper_found and lower_found:
    print("Valid password has one uppercase/lowercase letter")
else:
     print("InValid password Should contain atleast one uppercase/lowercase letter")
# upper_letter = input("Enter password: " )

# if one_uppercase_letter in upper_letter:
#     print("Password contain one Uppercase letter")
# else:
#     print("Password must contain atleast one Uppercase letter")

# password = "hello123"

# password_len = len(password)

# enter_password = input("Enter password : ")

# enter_password_len = len(enter_password)

# if password_len < enter_password_len:
#     print("Strong password")
# elif password_len == enter_password_len:
#     print("Good password")
# else:
#     print("Weak password")

# p = input("Enter password ")

# if password == p:
#     print("Valid Password")
# else:
#    print("Invalid Password")