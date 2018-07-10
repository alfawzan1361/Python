#dotProduct
seq1 = input('Enter seq1: ')
seq1 = [int(x) for x in seq1.split()]
seq2 = input('Enter seq2: ')
seq2 = [int(y) for y in seq2.split()]

result = sum(x * y for x, y in zip(seq1, seq2))
print(result)