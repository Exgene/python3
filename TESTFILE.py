f = open('/home/student/OPen FIle')

lines=0
words=0
symbols=0

for line in f:
    lines=lines+1
    words=words+len(line.split())
    symbols=symbols+len(line.split("\n"))

print("Lines:",lines)
print("Words:",words)
print("Symbols:",symbols)
    
