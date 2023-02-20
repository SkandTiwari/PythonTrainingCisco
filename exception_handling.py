"""This tutorial is aboutpython exception handling"""

try:
    number = int(input("Enter your no :"))
    print(f"Number : {number}")

except Exception:
    print(f"Can't resolve : {Exception}")
