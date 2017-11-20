f = open('input.txt')
N = int(f.readline())
res = 0
for line in f.readlines():
	p_res = map(int, line.split())
	res +=sum(p_res)
f.close()
f = open('output.txt', 'w')
f.write(str(res))
f.close()