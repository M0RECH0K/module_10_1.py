from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    file_ = open(file_name, 'a', encoding='utf_8')
    for i in range(1, word_count + 1):
        file_.write(f'Какое-то слово № {str(i)}\n')
        sleep(0.1)
    file_.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}\n')

time_start = datetime.now()
trd1 = Thread(target=wite_words, args=(10, 'example5.txt'))
trd2 = Thread(target=wite_words, args=(30, 'example6.txt'))
trd3 = Thread(target=wite_words, args=(200, 'example7.txt'))
trd4 = Thread(target=wite_words, args=(100, 'example8.txt'))

trd1.start()
trd2.start()
trd3.start()
trd4.start()

trd1.join()
trd2.join()
trd3.join()
trd4.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
