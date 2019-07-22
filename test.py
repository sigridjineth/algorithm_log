dwarfheight = []
for i in range(9):
    dwarfheight.append(int(input())) #아홉 줄에 걸쳐 난쟁이의 키가 주어진다
dwarfheight.sort() #오름차순으로 정렬한다
sumheight=sum(dwarfheight) #합을 만든다

for i in range(9):
    for j in range(i+1, 9):
        if sumheight - dwarfheight[i] - dwarfheight[j] == 100:
            for k in range(9):
                if k == i or k == j:
										continue
                else:
                    print (dwarfheight[k])
            exit()
