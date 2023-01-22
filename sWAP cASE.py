def swap_case(s):
    Swap =''
    for char in s:
        if char.upper() != char:
            Swap += char.upper()
        elif char.lower() != char:
            Swap += char.lower()
        else:
            Swap += char
                    
    return Swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
