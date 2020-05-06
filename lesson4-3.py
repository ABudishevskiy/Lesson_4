# Дается строка - нужно проверить является ли она валидным паролем:
# (1) длина больше 4 символов, (2) содержит только маленькие латинские буквы и цифры,
# (3) число букв должно быть нечетным, а цифр четным.
import random
parol = ''
for i in range(random.randrange(1, 100)):
    parol = parol + '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'[random.randrange(0, 61)]
print(parol)
def Validpassw(a):
    count123 = 0
    countqwe = 0
    if len(a) < 5:
        return False
    for i in a:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            return False
        if i in '1234567890':
            count123 = count123 + 1
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            countqwe = countqwe + 1
    if count123 % 2 != 0:
        return False
    if countqwe % 2 != 1:
        return  False
    return True
print(Validpassw('werty45'))
print(Validpassw(parol))