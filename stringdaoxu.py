st = input()
l0 = []
st1 = str()
l1 = []
# cou = 0
for i in st:
    if i == ' ':
        l0.append(st1)
        st1 = ''
        # cou += 1
    else:
        st1 += i
l0.append(st1)
st1 = ''
st2 = ''
l0.reverse()
#print(str(l0))
for i in l0:
    st1 = ' ' + i
    st2 += st1
    #print(st1)
    #str += st2
st2 = st2[1::]
#st2.pop()
print(st2)
#print(i + ' 'for i in l0)
#print(st1)

