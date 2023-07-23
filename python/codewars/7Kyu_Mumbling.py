# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
    # accum("abcd") -> "A-Bb-Ccc-Dddd"
    # accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    # accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# def accum(string):
#     multiplicador = 1
#     string2 = ""
#     for i in string:
#         string2 += (i*multiplicador)
#         string2 += "-"
#         multiplicador += 1
#     return(string2[:-1])

def accum(s):
    result = []
    for i, char in enumerate(s, 1):
        result.append((char*i).title())
    return('-'.join(result))
print(accum("paTata"))