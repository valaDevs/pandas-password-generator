import random
import pandas
import os

chars = "abcdefghijklmnopABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password = "".join(random.sample(chars, 12))
passwords_list = []
passwords_list.append(password)
data = pandas.DataFrame(passwords_list)
data.to_csv("passwords.csv",index=None, mode="a", header=not os.path.isfile("passwords.csv"))
print(passwords_list)
not (os.path.isfile("passwords.csv") and os.stat("passwords.csv").st_size != 0)

