from os import system,listdir
import glob

#пути с тестовыми инпутами и аутпутами
dir_input = './inputs/*.txt'
dir_output = './outputs/*.txt'

#делаем словарь с инпутами и аутпутами (наверное это удобнее, я хз)
test_dict = {}; i = 0
for input in glob.glob(dir_input):
    f_in = open(input,'r'); 
    try:
        f_out = open(glob.glob(dir_output)[i]) #если нет inp outp?
        test_dict.update({f_in.read():f_out.read()}); f_out.close()
    except IndexError:
        pass
    f_in.close()
    i+=1

usr_answ_file = glob.glob('./usr_answ/*.py')[0]
#нужно следить за тем, чтобы всегда в usr_answ был один файл

print(usr_answ_file)
for key in test_dict:
    f = open('input.txt', 'w')
    f.write(key)
    f.close()
    system('python '+usr_answ_file)
    try:
        f = open('output.txt','r')
    except IOError as e:
        print(u'coldnt open file')
    else:
        usr_answ = f.read()
        f.close()
        print('usr answ = ', usr_answ)
        print('test answ = ', test_dict[key])
        if usr_answ == test_dict[key].strip('\n'):
              print('OK')
        else:
              print('NOT OK')
        
