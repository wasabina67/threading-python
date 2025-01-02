import threading
import time


def func_10():
    f_name = func_10.__name__
    print(f"-- {f_name} begin")


def func_2():
    f_name = func_2.__name__
    print(f"-- {f_name} begin")


def main():
    func_10()
    func_2()


if __name__ == "__main__":
    main()
