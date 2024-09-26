# soal 1
n1 = 15
for i in range(1, n1+1):
    if (i % 12 == 0):
        print("OKYES", end=" ")
    elif (i % 3 == 0):
        print("OK", end=" ")
    elif (i % 4 == 0):
        print("YES", end=" ")
    else:
        print(i, end=" ")
print() 

# soal 2 a
n2 = 5
for i in range(1, n2+1):
    for _ in range(i):
        print(i, end="")
    print()
    

# soal 2 b
n3 = 5
for i in range(1, n3+1):
    for j in range(i):
        print(i-j, end="")
    print()
    

# soal 2 c

n4 = 5  
for i in range(1, n4+1):
  start = i if i <= 3 else 3
  arah = 1 if i <= 3 else -1
  for j in range(i):
    print(start, end="")
    start += arah
    if start == 6 or start == 1:
      arah *= -1
  print()


# soal 2 d
n5 = 5
for i in range(1, n5+1):
    for j in range(1, n5+1):
        if (j % 2 == 0):
            print(j * n5 - (i-1), end=" ")
        else:
            print((j-1) * n5 + i, end=" ")
    print()
    print()


# soal 3
res = []
n6 = [12, 9, 13, 6, 10, 4, 7, 2]

for val in n6:
    if val % 3:
        res.append(val)

res.sort()
print(res)



