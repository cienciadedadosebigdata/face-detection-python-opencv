#       ----------- FUNCTION TO READ THE FILE AND ADD THE NAMES AND IDs IN TO TUPLES
def FileRead():
    Info = open("Names.txt", "r")                       #   Open th text file in readmode
    ID = []                                             #   The tuple to store IDs
    NAME = []                                           #   The tuple to store Names
    while (True):                                       #   Read all the lines in the file and store them in two tuples
        Line = Info.readline()
        if Line == '':
            break
        ID.append(int(Line.split(",") [0]))
        NAME.append (Line.split(",")[1].rstrip())
       
    return ID, NAME                                     #   Return the two tuples
        
IDs, Names = FileRead()                                 #   Run the above Function to get the ID and Names Tuple

                #       ------- FUNCTION TO FIND THE NAME

def ID2Name(ID, conf):
    if ID > 0:
        NameString = "Name: " + Names[IDs.index(ID)] + " Confidence: " + (str(round(conf)) )       #   Find the Name using the index of the ID
    else:
        NameString = ("Name: Unknown Confidence: N/A   ")       #   Find the Name using the index of the ID

    return NameString

#       ------------------- THIS FUNCTION READ THE FILE AND ADD THE NAME TO THE END OF THE FILE

def AddName():
    Name = raw_input('Enter Your Name ')
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + "," + Name + "\n")
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID
