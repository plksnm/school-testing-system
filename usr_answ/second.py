f = open('input.txt','r')
a, b = f.read().split()
f.close()
res = str(int(a)+int(b))
f = open('output.txt','w')
f.write(res)
f.close()

