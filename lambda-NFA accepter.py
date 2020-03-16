global v

def matrice(L,n):
    M=[[0]*n for i in range(n)]
    for i in L:
        if M[i[0]][i[2]] == 0:
            M[i[0]][i[2]] = i[1]
        else:
            M[i[0]][i[2]] = [M[i[0]][i[2]]]
            M[i[0]][i[2]].append(i[1])
    return M

def eval(k,w,fin,s,n,M):
    if k==len(w):
        if s in fin:
            v.append(True)
        else:
            exl=False
            for i in range(n):
                if isinstance(M[s][i],list)==False:
                    if M[s][i]=='$':
                        exl=True
                else:
                    if '$' in M[s][i]:
                        exl=True
            if exl==True:
                for i in range(n):
                    if isinstance(M[s][i], list) == False:
                        if M[s][i] == '$':
                            eval(k, w, fin, i, n, M)
                    else:
                        for j in range(len(M[s][i])):
                            if M[s][i][j] == '$':
                                eval(k, w, fin, i, n, M)
            else:
                v.append(False)
    else:
        ex=False
        for i in range(n):
            if isinstance(M[s][i], list) == False:
                if M[s][i] == '$' or M[s][i]==w[k]:
                    ex=True
            else:
                if w[k] in M[s][i] or '$' in M[s][i]:
                    ex=True
        if ex==True:
            for i in range(n):
                if isinstance(M[s][i], list) == False:
                    if M[s][i] == '$':
                        eval(k, w, fin, i, n, M)
                    elif M[s][i] == w[k]:
                        eval(k + 1, w, fin, i, n, M)
                else:
                    for j in range(len(M[s][i])):
                        if M[s][i][j] == '$':
                            eval(k, w, fin, i, n, M)
                        elif M[s][i][j] == w[k]:
                            eval(k + 1, w, fin, i, n, M)
        else:
            v.append(False)




f=open("dateNFA.in")
n=int(f.readline())
m=int(f.readline())
c=f.readline().split()
init=int(f.readline())
k=int(f.readline())
fin=[int(x) for x in f.readline().split()]
l=int(f.readline())

L=[]
for i in range(l):
    lin=f.readline().split()
    L.append([int(lin[0]),lin[1],int(lin[2])])

o=int(f.readline())

cuv=[]
for i in range(o):
    w=f.readline()
    if w[len(w)-1]=='\n':
        w=w[:len(w)-1]
    cuv.append(w)

f.close()

M=matrice(L,n)

for w in cuv:
    v=[]
    eval(0,w,fin,init,n,M)
    if True in v:
        print("TRUE")
    else:
        print("FALSE")



