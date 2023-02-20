"""Multiprocessing is quite a bit similar to the multithreading application in python"""

import time
import multiprocessing


def calc_square(num):
    for i in num:
        time.sleep(1)
        print("square : ",i*i)


def calc_cube(num):
    for i in num:
        time.sleep(1)
        print("cube", i*i*i)

if __name__ == "__main__":
    arr = [2, 3, 4, 9, 4 ,7, 12, 19]
    #p1 = multiprocessing.Process(target = calc_square, args = (arr,) )
    p1 = multiprocessing.Process(target = calc_square, args = (arr,))

    p2 = multiprocessing.Process(target = calc_cube, args = (arr,))

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done!")

    print("Time taken : ", time.time())