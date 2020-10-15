import logging

def add(a, b):
    answer = a + b
    return answer


def subtract(a, b):
    answer = a - b
    return answer


def multiply(a, b):
    answer = a * b
    logging.warning("there is a warning here.")
    return answer


def divide(a, b):
    answer = a/b
    logging.error("there   is an   error.")
    return answer


def main():

    logging.basicConfig(filename="run_log.log",
                        filemode='w',
                        level=logging.DEBUG)
    x = 1
    y = 5
    z = multiply(x, y)
    v = divide(y, x)
    print(z)


if __name__ == '__main__':
    main()
