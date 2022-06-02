n = input()

n = n[::-1]
# print(n)
a = str()
cou = 1
for i in n:
    if i not in a:
        a = a + i



print(int(a))
