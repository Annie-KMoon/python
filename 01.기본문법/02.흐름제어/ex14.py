# for i in range(5): #0~4 행
#     for j in range(5): #0~4 렬
#         print(f"({i},{j})",end="") #변수 i, j의 조합
#     print()

for i in range(1,6,1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()    