import multiprocessing
import time

res = []

def calc_square(num):
    global res
    for i in num:
        time.sleep(1)
        res.append(i*i)
    print("Inside Process : ", res)


if __name__ == "__main__":
    arr = [1, 3, 4, 6]

    p1 = multiprocessing.Process(target=calc_square, args = (arr, ))
    print("Multiprocessing is about to start")
    p1.start()
    p1.join()
    print("Multiprocessing Ended!")

    print("Outside process : ", res)