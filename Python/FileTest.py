
ID = 1

def FileRad():
    Info = open("Names.txt", "a")
    while (ID != 0):
        ID = input ('Enter the ID ')
        NME = raw_input('Enter the Name ')
        Info.write(str(ID) + "," + NME + "\n")
    Info.close()


def FileRead():
    Info = open("Names.txt", "r")
    ID = []
    NAME = []
    while (True):
        Line = Info.readline()
        if Line == '':
            break
        ID.append(int(Line.split(",") [0]))
        NAME.append (Line.split(",")[1]) 
    return ID, NAME
        
IDs, Names = FileRead()


print(IDs)
IDs



