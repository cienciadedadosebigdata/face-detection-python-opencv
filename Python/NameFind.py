#       ----------- FUNCTION TO READ THE FILE AND ADD THE NAMES AND IDs IN TO TUPLES

import cv2
WHITE = [255, 255, 255]

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

#       ------------------- FUNCTION TO FIND THE NAME  -----------------------------------------------------------

def ID2Name(ID, conf):
    if ID > 0:
        NameString = "Name: " + Names[IDs.index(ID)] + " Distance: " + (str(round(conf)) )                                #   Find the Name using the index of the ID
    else:
        NameString = (" Face Not Recognised ")                                                                   #   Find the Name using the index of the ID

    return NameString

#       ------------------- THIS FUNCTION READ THE FILE AND ADD THE NAME TO THE END OF THE FILE  -----------------

def AddName():
    Name = raw_input('Enter Your Name ')
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + "," + Name + "\n")
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID

#       ------------------- DRAW THE BOX AROUND THE FACE, ID and CONFIDENCE  -------------------------------------
def DispID(x, y, w, h, NAME, Image):

#  --------------------------------- THE POSITION OF THE ID BOX  -------------------------------------------------        

    Name_y_pos = y - 10
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------
    #cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)     #   Draw a rectangle arround the face
    cv2.line(Image, (x, y), (x + (w/5) ,y), WHITE, 1)
    cv2.line(Image, (x+((w/5)*4), y), (x+w, y), WHITE, 1)
    cv2.line(Image, (x, y), (x, y+(h/5)), WHITE, 1)
    cv2.line(Image, (x+w, y), (x+w, y+(h/5)), WHITE, 1)
    cv2.line(Image, (x, (y+(h/5*4))), (x, y+h), WHITE, 1)
    cv2.line(Image, (x, (y+h)), (x + (w/5) ,y+h), WHITE, 1)
    cv2.line(Image, (x+((w/5)*4), y+h), (x + w, y + h), WHITE, 1)
    cv2.line(Image, (x+w, (y+(h/5*4))), (x+w, y+h), WHITE, 1)
    
                  
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           #   Draw a Black Rectangle over the face frame
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         #   Print the name of the ID

# ---------------     SECOND ID BOX      ----------------------
def DispID2(x, y, w, h, NAME, Image):

#  --------------------------------- THE POSITION OF THE ID BOX  -------------------------------------------------        

    Name_y_pos = y - 40
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           #   Draw a Black Rectangle over the face frame
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         #   Print the name of the ID


# ---------------     THIRD ID BOX      ----------------------
def DispID3(x, y, w, h, NAME, Image):

#  --------------------------------- THE POSITION OF THE ID BOX  -------------------------------------------------        

    Name_y_pos = y - 70
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           #   Draw a Black Rectangle over the face frame
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         #   Print the name of the ID
