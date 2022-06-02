st1 = input().lower()
st2 = input().lower()
st3 = ''
for cou in range(len(st1)):
    if len(st3) > 0:
        break
    for co in range(cou+1):
        if st1[co:len(st1)-1-co] in st2:
            print(len(st1[co:len(st1)-1-co]))
            st3 = st1[co:len(st1)-1-co]
            break
