height=3;
width=4;
space=height*width;
m=1;

#tree upper part
for i in range(1,height+1):
    for x in range(m,width+1):
        for y in range(space,x+1,-1):
            print(" ",end="")
        for z in range(1,x+1):
            print("@ ",end="")
        print()
    m=m+2
    width=width+2

#tree lower part
for x in range(1,5):
    for y in range(space-5,0,-1):
        print(" ",end="")
    for z in range(1,5):
        print("@ ",end="")
    print()