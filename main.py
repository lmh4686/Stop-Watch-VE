import datetime
a = 0
b = 0
while a != "":
    a = input("Hit enter if you are ready.")
    c = datetime.datetime.now()
while b != "":
    b = input("Hit enter if you think you are on 10.00' after first prompt")
    d = datetime.datetime.now()
print(d - c)