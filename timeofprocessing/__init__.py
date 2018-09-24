# coding:utf-8

import time


def counter(func):
    
    def internal_function(*args, **kwargs):
        
        initial = time.perf_counter()
        array = [str(arg) for arg in args]

        if len(array) == 0:
            string = ''
        else:
            string = ', '.join(array)

        result = func(*args, **kwargs)
        fim = time.perf_counter() - initial
        print('Function {}({}) -> {:.6f} s to process.'.format(func.__name__, string, fim))

        return result

    return internal_function
