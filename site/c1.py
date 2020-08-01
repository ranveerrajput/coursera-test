i=0
for _ in range(int(input())):
    s=list(str(input()))
    dot=s.count('.')
    b=s.count('B')
    if(dot>0 and dot<=b):
        i=i+1
        print("Case #"+str(i)+": "+"Y")
    else:
        i=i+1
        print("Case #"+str(i)+": "+"N")
    