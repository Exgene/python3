fname=input("Enter file name")
try:
    with open(fname,"r") as f:
        total=0
        for line in f:
            marks=line.split()
            print(marks)
            for mark in range(0,len(marks)):
                total=total+int(marks[mark])
                avg=total/len(marks)
                print("Total marks=",total,"\n Average Marks=%.3f"%avg)
except:
    print("Invalid file name")
        
