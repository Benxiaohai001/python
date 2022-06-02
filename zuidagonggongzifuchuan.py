st = input().lower()
l = st.split(' ')
st1 = l[0]
st2 = l[1]
st3 = ''
for cou in range(len(st1)):
    if len(st3) > 0:
        break
    for co in range(cou+1):
        if st1[co:len(st1)-cou+co] in st2:
            print(len(st1[co:len(st1)-cou+co]))
            st3 = st1[co:len(st1)-cou+co]
            break


    

