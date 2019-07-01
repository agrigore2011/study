user = input('Как вас зовут?')
print('Привет '  + user)
fileName = input('Какой файл выбрать?')

choice = ''
while choice != 'записать' and choice != 'прочитать':
    print('Хотите записать или прочитать файл?')
    choice = input()

if choice == 'записать':
    text = input('Что хотите записать?')
    file = open(fileName, 'w')
    file.write (text)

file.close()





