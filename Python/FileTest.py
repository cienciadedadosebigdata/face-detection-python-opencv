

def AddName():
    Name = raw_input('Enter Your Name ')
    Info = open("Names.txt", "r+")    
    Info.write(str((sum(1 for line in Info))+1) + "," + Name + "\n")
    print ("Name Stored...")
    Info.close()

        #ID = input ('Enter the ID ')
        #NME = 

AddName()

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
        

#       ------- FUNCTION TO FIND THE NAME

def ID2Name(ID, conf ):
    Name = "Name: " + Names[IDs.index(ID)] + " Conf: " + str(round(conf))

    return Name






