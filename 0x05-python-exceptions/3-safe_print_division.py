#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("{}".format(result))
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:", result)
    return result
