from math import inf

def divide(first, second):
    if second == 0: # если в параметр second записан 0, то...
        return inf # ... возвращает бесконечность
    else:
        return first / second # если в параметр записан не 0, то возвращает результат деления

print(divide(49, 7))
print(divide(15, 0))
