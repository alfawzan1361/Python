# sum and product
seq = input('Enter your list: ')
seq = [int(x) for x in seq.split()]
num = 0
num1 = 1

for sumProd in seq:
    num += sumProd
    num1 *= sumProd
print("The sum is: ", num)
print("The product is: ", num1)