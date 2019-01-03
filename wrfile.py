#############################################
#                 Functions                 #
#############################################

def write():
    test = open("ReadMe.txt", "w")

    test.write("This is a test")
    test.close()
def read():
    readfile = open("ReadMe.txt", "r")
    print(readfile.read())
    readfile.close

###########################################
#              Main Code                  #
###########################################
write()
read()

