def idNoGenrator(name, roll, grade):
    temp = name[1:3].upper()
    rollTemp = roll[2:4]
    gradeTemp = grade.upper() 

    return temp+rollTemp+gradeTemp

def registrationPage():
    
    return idNoGenrator("skand", "123423", "a")

if __name__ == "__main__":
    print(registrationPage())