from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]

total=reduce(lambda a,b: a+b,numbers,20)

print(total)