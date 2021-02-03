from random import randint

with open('names.txt') as f:
    text1 = f.read()

with open('names2.txt') as f2:
    text2 = f2.read()

with open('rus_slovar.txt') as f3:
    text3 = f3.read()

with open('man_1.txt') as f4:
    text4 = f4.read()

individual_words = text1.split()
random_num = randint(0, len(individual_words))

individual_words2 = text2.split()
random_num2 = randint(0, len(individual_words2))

print('                       __ _              ')
print('/\_/\___  _   _ _ __  / _\ |_ ___  _ __ _   _ ')
print('\_ _/ _ \| | | |  __| \ \| __/ _ \|  __| | | |')
print(' / \ (_) | |_| | |    _\ \ || (_) | |  | |_| |')
print(' \_/\___/ \__,_|_|    \__/\__\___/|_|   \__, |')
print('                                        |___/ ')


print('------------')
print('Вас зовут')
print(individual_words[random_num] + ' ' + individual_words2[random_num2])
print('------------')

# генерируем деньги в кармане
random_num3 = randint(0, 1000)

print('У вас в кармане' + ' ' + str(random_num3) + ' ' + '$')

# генерируем то что вдохновляет
individual_words3 = text3.split()
random_num3 = randint(0, len(individual_words3))
print('Вас всегда вдохновляло' + ' ' + '|' + individual_words3[random_num3] + '|')

# генерируем черту характера


individual_words4 = text4.split()
random_num4 = randint(0, len(individual_words4))
print('Черта характера' + ' ' + '|' + individual_words4[random_num4] + '|')
print('------------')
print(' ')
print(' ')
