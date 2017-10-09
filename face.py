from tkinter import Tk, Label, Button, Listbox, filedialog
from os import system,listdir, path, chdir, getcwd
import glob
#global fname 
#fname = '1'
def Get(event):
	l = event.widget
	sel = l.curselection()
	global dir_input
	global dir_output
	if sel[0] == 0:
		task_show.config(text = "Найти сумму двух чисел")
		dir_input = './task_1/inputs/*.txt'
		dir_output = './task_1/outputs/*.txt'
	elif sel[0] == 1:
		task_show.config(text = "Найти сумму элементов квадратной матрицы")
		dir_input = './task_2/inputs/*.txt'
		dir_output = './task_2/outputs/*.txt'
	file_open_btn.config(state = "normal")


def FileOpen():
	global fname
	fname = filedialog.askopenfilename(filetypes=(("Python files", "*.py"), ("All files", "*.*") ))
	file_open_text.config(text = fname)
	test_btn.config(state = "normal")

def Testing():
	test_dict = {}; i = 0
	for input in glob.glob(dir_input):
		f_in = open(input,'r')
		try:
			f_out = open(glob.glob(dir_output)[i])
			test_dict.update({f_in.read().strip('\n'):f_out.read().strip('\n')}); f_out.close()
		except IndexError:
			pass
		f_in.close()
		i+=1

	global fname
	txt = ''; i = 1
	for key in test_dict:
		input_file = fname[:fname.rfind('/')]+'/input.txt'
		chdir(fname[:fname.rfind('/')+1])
		print(getcwd())
		f = open(input_file, 'w')
		f.write(key)
		f.close()
		system('python '+ fname)
		try:
			output_file = fname[:fname.rfind('/')]+'/output.txt'
			f = open(output_file,'r')
		except IOError as e:
			print(u'coldnt open file')
		else:
			usr_answ = f.read()
			f.close()
			print('usr answ=', usr_answ)
			print('test answ=', test_dict[key])
			if usr_answ == test_dict[key].strip('\n'):
				txt +=str(i)+' TEST IS OK\n'
				test_answ_lbl.config(text = txt)
			else:
				txt +=str(i)+' TEST IS NOT OK\n'
				test_answ_lbl.config(text = txt)
			i+=1		




root = Tk()
task = Label(root, text = 'Условие задачи')
task.pack()
task_list = Listbox(root, height = 2)
task_list.insert(0, "Задача 1","Задача 2")
task_list.pack()
task_show = Label(root)
task_show.pack()
task_list.bind("<<ListboxSelect>>", Get)
file_open_btn = Button(root, text = "Открыть файл", command = FileOpen, state = "disabled")
file_open_btn.pack()
file_open_text = Label(root)
file_open_text.pack()
test_btn = Button(root,text = "Проверить", command = Testing, state = "disabled")
test_btn.pack()
test_answ_lbl = Label(root)
test_answ_lbl.pack()
root.mainloop()