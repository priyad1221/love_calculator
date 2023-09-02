print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combinename=name1+name2
new_combinename=combinename.lower()

t=new_combinename.count("t")
r=new_combinename.count("r")
u=new_combinename.count("u")
e=new_combinename.count("e")


l=new_combinename.count("l")
o=new_combinename.count("o")
v=new_combinename.count("v")
e=new_combinename.count("e")

true = t+r+u+e
love = l+o+v+e

result=int(str(true) + str(love))


if  (result < 10) or (result > 90):
    print(f"Your score is {result}, you go together like coke and mentos.")
elif (result >= 40) or (result <= 50):
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
