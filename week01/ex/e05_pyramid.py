def pyramid(level,sign,is_reversed=False):
    if not (is_reversed) and level>1 and len(sign)==1:
        row = 1
        while(row<=level):
            print(" "*(level-row),end="")
            print(sign*(row*2-1),end="")
            row+=1
            print()
    elif(is_reversed) and level>1 and len(sign)==1:
        row = 0
        full = level
        i = 1
        while(row<level):
            print(" "*row,end="")
            print(sign*(level*2-i),end="")
            i+=2
            row+=1
            print()            
    else:
        print("Invalid parameters")