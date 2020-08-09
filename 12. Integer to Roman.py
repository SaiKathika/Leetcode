def intToRoman(num):
    values = [
        1000, 900, 500, 400, 
        100, 90, 50, 40, 
        10, 9, 5, 4, 
        1
        ]
    symbols = [
        'M', 'CM', 'D', 'CD', 
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I'
        ]
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman += symbols[i]
            num -= values[i]
        i += 1
    return roman
    
print(intToRoman(1994))
#Best Solution
'''
def intToRoman(self, num: int) -> str:
    m = ['', 'M', 'MM', 'MMM']
    c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return m[num//1000] + c[(num%1000)//100] + x[(num%100)//10] + i[num%10]
'''