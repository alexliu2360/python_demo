# -*- coding: utf-8 -*-

'''
21：用只能以关键字形式指定的参数来确保代码明晰
'''


def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def safe_division_b(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    '''
        这种没有办法保证函数的调用者一定会使用关键字来明确指定这些参数的值
    '''
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def safe_division_c(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    '''
        '*'代表位置参数的就此终结，之后的参数只能以关键字参数来指定
    '''
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def test():
    result = safe_division(1.0, 10 ** 500, True, False)
    print(result)


def test_c():
    result = safe_division(1.0, 10 ** 500, True, False)
    print(result)


if __name__ == '__main__':
    test_c()
