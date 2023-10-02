with open('.\\seq4data.txt', 'r') as f:   
    lines = f.readlines()                   

a = lines[::2]
for i in range(len(a)):
    a[i] = a[i][:4]   
print(a)