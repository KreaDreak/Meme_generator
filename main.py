import time
print('Мемо-генератор запущен, готовь мемы))')


top_text = ''
bottom_text = ''


text_type = int(input('Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: '))

if text_type == 1:
    bottom_text = input('Введи нижний текст: ')
else:
    top_text = input('Введи верхний текст: ')
    bottom_text = input('Введи нижний текст: ')

print('Генерация мема', end='')
time.sleep(1)
print('.', end='')

time.sleep(1)
print('.', end='')

time.sleep(1)
print('.')

print(top_text)
print(bottom_text)
