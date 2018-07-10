temperature = float(input('Enter a temperature in Fahrenheit: '))
if temperature <= 32:
    print('The state of water is solid.')
else:
    if temperature >= 33 and temperature <= 211:
        print('The state of water is liquid.')
    else:
        print('The state of water is gas.')