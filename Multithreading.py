import time
import threading

def calc_square(number):
    print("Calculating square...")
    for n in number :
        time.sleep(0.2)
        print("Square : ", n*n)

def calc_cube(number):
    print("Calculating Cube...")
    for n in number :
        time.sleep(0.2)
        print("Cube : ", n*n*n)


arr = [1, 4, 6, 8, 9, 10, 12]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target= calc_cube, args=(arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print("Time Taken : ", time.time()-t)



