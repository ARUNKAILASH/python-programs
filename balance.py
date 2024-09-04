def valency(c):
    ascii_val = ord(c)
    sum_val = 0
    while ascii_val != 0:
        sum_val += ascii_val % 10
        ascii_val //= 10
    if sum_val >= 10:
        sum_val = sum_val % 10 + sum_val // 10
    return sum_val

def balance_compound(compound, equivalent_point):
    valency1 = valency(compound[0])
    valency2 = valency(compound[1])
    found = False
    for i in range(equivalent_point / valency1, 0, -1):
        for j in range(2,equivalent_point / valency2 ,+ 1):
            if valency1 * i + valency2 * j == equivalent_point:
                print(f'{compound[0]}{i} {compound[1]}{j}')
                found = True
    if not found:
        print("Not Possible")

compound = input()
equivalent_point = int(input())
balance_compound(compound, equivalent_point)
