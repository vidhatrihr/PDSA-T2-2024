def del_char(s,c):
    if len(c) != 1:
        return s
    
    result = ''
    for char in s:
        if char != c:
            result += char
    return result


s = input()
c = input()
print(del_char(s, c))