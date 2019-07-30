def check_substring(s, length):
    number_of_substrings = len(s) // length
    for i in range(1, number_of_substrings):
        for j in range(0, length):
            prev_char = s[(i - 1) * length + j]
            curr_char = s[i * length + j]
            if prev_char != curr_char:
                return False
    
    return True
        
def solution(s):
    if len(s) <= 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        if check_substring(s, i):
            return len(s) / i
    
    return 1

if __name__ == '__main__':
    print(solution("abcabcabcabc") == 4)
    print(solution("asdfasdf") == 2)

