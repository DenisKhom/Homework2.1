x = 38
print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')
#Примеры
a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b <1000):
    print('успех')
if 5 <= b and b < 10:
    print('успех')
# можно сравнивать - числа, строки, списки
if '5634345463' > '56123':
    print('luck')
if '1254' >= '1253':
    print('URA_'*5,'URA')
if [1, 2] > [1, 0]:
    print('OK')
# нельзя сравнивать разные типы
if '6' > 5:
    print('YES')
if [5, 6] > 5:
    print('USPEH')
# Ho
if '6' != 5:
    print('PRAVDA')
