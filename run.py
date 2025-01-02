import threading
import time


def func_10():
    f_name = func_10.__name__
    print(f"-- {f_name} begin")
    time.sleep(10)
    print(f"-- {f_name} end")


def func_2(t_10):
    f_name = func_2.__name__
    print(f"-- {f_name} begin")
    time.sleep(2)
    t_10.join()
    print(f"-- {f_name} end")


def main():
    t_10 = threading.Thread(target=func_10, name="t_10")
    t_2 = threading.Thread(target=func_2, args=(t_10,), name="t_2")

    t_10.start()
    t_2.start()

    t_10.join()
    t_2.join()

if __name__ == "__main__":
    main()
