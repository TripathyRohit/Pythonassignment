'''
The program to convert temperature in centigrate to Fahrenheit
F = 9/5 *C+32 . Where C is the given temperature in centigrade and F is the temperature in Fahrenheit.
'''

temp = float(input('Enter temperature in centigrate:'))
fahrenheit = (temp*1.8) +32
print ('The converted Value is',fahrenheit, 'fahrenheit')
