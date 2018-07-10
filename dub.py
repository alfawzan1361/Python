#reDub
seq = input('Enter seq: ')
seq = [int(x) for x in seq.split()]
result = [x for p in zip(seq, seq) for x in p]

print(result)