
ID = 1

def FileRad():
    Info = open("Names.txt", "a")
    while (ID != 0):
        ID = input ('Enter the ID ')
        NME = raw_input('Enter the Name ')
        Info.write(str(ID) + "," + NME + "\n")
    Info.close()

#       ----------- FUNCTION TO READ THE FILE AND ADD THE NAMES AND IDs IN TO TUPLES
def FileRead():
    Info = open("Names.txt", "r")
    ID = []
    NAME = []
    while (True):
        Line = Info.readline()
        if Line == '':
            break
        ID.append(int(Line.split(",") [0]))
        NAME.append (Line.split(",")[1].rstrip())
       
    return ID, NAME
        
IDs, Names = FileRead()

#       ------- FUNCTION TO FIND THE NAME

def ID2Name(ID, conf ):
    Name = "Name: " + Names[IDs.index(ID)] + " Conf: " + str(round(conf))

    return Name

print (ID2Name(1, 2002))





