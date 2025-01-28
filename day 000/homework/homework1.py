def find(a,b,c):
    if a % c != 0 or (a % c == 0 and b % c == 0):
        return (b - a) // c
    else:
        return (b - a) // c + 1

print(find(14,20,5))