from os import *
#процедура для адекватного чтения значений из тестовых файлов 
def reading_file(s, lines = []):
    while s.find('\\n',0,len(s))!=-1:
        lines.append(s[:s.find('\\n',0,len(s))])
        s = s[s.find('\\n',0,len(s))+2:]

#работа с файлом входных значений
f = open('input_test.txt', O_RDONLY)
input_tests = str(read(f,300))[2:]; tests = []
reading_file(input_tests, tests)
close(f)
#print(tests)

#работа с файлом выходных значений
f = open('output_test.txt', O_RDONLY)
right_answ = str(read(f,300))[2:]
close(f)
tests_answs = []; reading_file(right_answ, tests_answs)
#print(tests_answs)

#создаем словарь из входных и выходных значений
test_dict = dict.fromkeys(tests); i = 0 
for key in test_dict:
    test_dict[key] = tests_answs[i]
    i+=1
#print(test_dict)

for key in test_dict:
    f = open('input.txt', O_RDWR|O_CREAT)
    ret = write(f, (key+'\n').encode()) #ya ne ponyala nahuja eto, v posledovatelnost byte peregnali
    close(f)
    system('python second.py')
    try:
        f = open('output.txt', O_RDONLY)
    except IOError as e:
        print(u'couldnt open file')
    else:
        usr_answ = str(read(f, 300))
        usr_answ = usr_answ[2:(len(usr_answ)-1)]
        close(f)
        print('usr said :', usr_answ)
        print('test answ said: ', test_dict[key])

        if usr_answ == test_dict[key]:
            print('OK')
        else:
            print('NOT OK')

