import random

def roll():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    result = (d1, d2)
    return result



while True:
    print(roll())
    choice = input("do you want to continue [Y/N]: ")
    if choice == "Y":
        continue
    else:
        print("thanks for using the dice!!")
        break
    