
a = [2, 3, 4, 5]
b = [4, 5, 7, 9]
c = [2, 3, 4, 8, 5, 4]
result = []
for i in a:
    for j in b:
        for k in c:
            if i == j == k:
                result.append(i)
                break
print(result)
