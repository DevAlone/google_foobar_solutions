def answer(start, length):
    result = 0
    
    for i in range(length):
        result ^= xorOfSequence(
            start, 
            start + length - 1 - 1)
        
        start += length
        
    return result
    
    
# values should be positive 
def xorOfSequence(start, end):
    if start != 0:
        return xorOfSequence(0, start - 1) ^ xorOfSequence(0, end)
    
    # keep 2 bits
    length = end & 3
    # check them 
    if length == 0:
        return end
    elif length == 1:
        return 1
    elif length == 2:
        return end + 1
    return 0
