#listOfPositives
seq = input('Enter seq: ')
seq = [int(x) for x in seq.split()]
positives = list(filter(lambda x: x > 0, seq))

print(positives)