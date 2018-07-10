#reDub
seq = input('Enter seq: ')
seq = [int(x) for x in seq.split()]
result = list(set(seq))

print(result)
