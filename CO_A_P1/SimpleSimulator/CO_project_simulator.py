#Functions definition
def todecimal(n,bit):
    va=0
    for i in range(0,bit):
        a=int(n[bit-1-i])
        va=va+a*(2**i)
    return va
def todecimalf(n,bit):
    va=0
    dp=bit
    for i in range(len(n)):
        if n[i]=='.':
            dp=i
            break
    for i in range(dp):
        va=va+int(n[dp-i-1])*(2**i)
    for i in range(dp+1,len(n)):
        va=va+int(n[i])*(2**(-1*(i-dp)))
    return va
def tobinary(n,bit):
    if n==0:
        return '0'*bit
    temp_lst=[]
    while n>0:
        q=n//2
        r=n%2
        temp_lst.append(r)
        n=q
    va=0
    for tt in range(0,len(temp_lst)):
        va=va+temp_lst[tt]*(10**(tt))
    x=bit-len(temp_lst)
    va=str(va)
    va='0'*x+va
    return va
def tobinaryf_(n):
    n0=int(n)
    n1=n-int(n)
    temp_lst=[]
    if n0==0:
        va='0'
    else:
        while n0>0:
            q=n0//2
            r=n0%2
            temp_lst.append(r)
            n0=q
        c=len(temp_lst)
        va=str(temp_lst[-1])
        for tt in range(1,c):
            va=va+str(temp_lst[c-tt-1])
    temp_lst=[]
    if n1==0:
        vb='0'
    else:
        while n1!=0:
            m=n1*2
            m0=int(m)
            m1=m-int(m)
            temp_lst.append(m0)
            n1=m1
        c=len(temp_lst)
        vb=str(temp_lst[0])
        for tt in range(1,c):
            vb=vb+str(temp_lst[tt])
    v=va+'.'+vb
    return v
def tobinary_f(n,bit):
    n0=int(n)
    n1=n-int(n)
    temp_lst=[]
    if n0==0:
        va='0'
    else:
        while n0>0:
            q=n0//2
            r=n0%2
            temp_lst.append(r)
            n0=q
        c=len(temp_lst)
        va=str(temp_lst[-1])
        for tt in range(1,c):
            va=va+str(temp_lst[c-tt-1])
    temp_lst=[]
    if n1==0:
        vb='0'
    else:
        while n1!=0:
            m=n1*2
            m0=int(m)
            m1=m-int(m)
            temp_lst.append(m0)
            n1=m1
        c=len(temp_lst)
        vb=str(temp_lst[0])
        for tt in range(1,c):
            vb=vb+str(temp_lst[tt])
    v=va+'.'+vb
    return '0'*(bit-len(v))+v
def reg_add(inpp):
    if inpp=='R0':
        return '000'
    elif inpp=='R1':
        return '001'
    elif inpp=='R2':
        return '010'
    elif inpp=='R3':
        return '011'
    elif inpp=='R4':
        return '100'
    elif inpp=='R5':
        return '101'
    elif inpp=='R6':
        return '110'
    elif inpp=='FLAGS':
        return '111'
def checkins(ins):
    lst=['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt','addf','subf','movf']
    if ins[1] in lst:
        return True
    else:
        return False
def checkregister(a):
    lst=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
    if a in lst:
        return True
    else:
        return False
def checktype(ins):
    if len(ins)<2:
        return None
    lst=['add','sub','mul','xor','or','and','addf','subf']
    if ins[1] in lst:
        return 'A'
    lst=['ld','st']
    if ins[1] in lst:
        return 'D'
    lst=['jmp','jlt','jgt','je']
    if ins[1] in lst:
        return 'E'
    lst=['hlt']
    if ins[1] in lst:
        return 'F'
    lst=['rs','ls',]
    if ins[1] in lst:
        return 'B'
    lst=['movf']
    if ins[1] in lst:
        return 'B0'
    lst=['div','not','cmp']
    if ins[1] in lst:
        return 'C'
    if ins[1]=='mov':
        if checkregister(ins[3])==True:
            return 'C'
    if ins[1]=='mov':
        if checkregister(ins[3])==False:
            return 'B'
    return None
def islabel(a):
    if a[-1]==':' and a[-2]!=' ':
        return True
    else:
        return False