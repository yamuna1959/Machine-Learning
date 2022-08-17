l1=['good','fine','nice','happy','positive']
l2=['bad','sad','not','negative','frastated']
str1=input('enter your response')
flag=0
encount=0
pcount=0
t=str1.split()
for i in range(len(t)):
    for j in range(len(l1)):
        if t[i]==l1[j]:
            flag=1
            pcount+=1
    for k in range(len(l2)):
        if t[i]==l2[k]:
            flag=1
            encount+=1
if flag==0:
    print('you are in another mood')
elif encount%2==0:
    print('response is positive')
else:
    print('response is negative')                