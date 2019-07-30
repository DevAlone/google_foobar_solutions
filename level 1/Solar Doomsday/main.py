import math
import sys


def answer(n):
    result = []
    while n > 0:
        part = int(math.sqrt(n))
        part *= part
        
        if part:
            result.append(part)
        else:
            result.append([1] * part)
            break
        
        n -= part
        
    return result
    

if __name__ == '__main__':
    print(answer(int(sys.argv[1])))
