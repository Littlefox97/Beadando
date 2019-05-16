eld=input("string: ")
szam=0
nagybetu=0
kisbetu=0
karakter=0
for i in eld:
    if i.isnumeric():
        szam+=1
    elif i.isupper():
        nagybetu+=1
    elif i.islower():
        kisbetu+=1
    else:
        karakter+=1

print("Az {0} stringben {1}db szam, {2}db nagybetu, {3}db kisbetu es {4}db egyeb karakter van van.".format(eld,szam,nagybetu,kisbetu,karakter))