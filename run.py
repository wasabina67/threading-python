import threading
import time


def func_10():
    f_name = func_10.__name__
    print(f"-- {f_name} begin")
    time.sleep(10)
    print(f"-- {f_name} end")


def func_2():
    f_name = func_2.__name__
    print(f"-- {f_name} begin")
    time.sleep(2)
    print(f"-- {f_name} end")


def main():
    t_10 = threading.Thread(target=func_10, name="t_10")
    t_2 = threading.Thread(target=func_2, name="t_2")

    t_10.start()
    t_2.start()


if __name__ == "__main__":
    main()
