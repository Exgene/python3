fname=input("Enter file name")#put same file name as present in the system
with open(fname,'r') as f:
    nl=nw=nc=0
    l1=[]
    for line in f:
        nl=nl+1
        words=line.split()
        print(words)
        nw=nw+len(words)
        for i in words:
            nc=nc+len(i)

print("Line length:",nl,"Word length:",nw,"Number of chaarcters:",nc)
    
