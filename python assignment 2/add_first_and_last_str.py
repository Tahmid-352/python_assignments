def string_both_ends(str):
    str = str(input())
    if len(str) < 2:
        return ''
dg
    return str[0:2] + str[-2:]


print(string_both_ends(str))
