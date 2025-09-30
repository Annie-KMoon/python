no = int(input('학생수>'))

names = []
for i in range(no): #0~no-1
    name = input('이름>')
    names.append(name)

for i in range(len(names)):  #출력방법1
    print(names[i], end=',')
print()

for name in names:   #출력방법2
    print(name, end=',')

print('\n')
    
for i, name in enumerate(names):   #출력방법3(인덱스넘버추가)
    print(i+1,name,end=',')