from FileRead import FileRead
from FileWrite import FileWrite
from FileEncrypter import FileEncrypter
from FileDecrypter import FileDecrypter

"""
       Idea:  /n = space 
        
        Syntax: print("Life is like a dream /n but is not always.")
        
        Result: Life is like a dream
        but is not always.
"""


class Writer:

    def writeToFile(self, fileName, stringData):
        try:
            with open(fileName, "w") as writer:
                writer.write(stringData)
        except IOError:
            print("Error 404.")


FileRead = FileRead("TestingFile.txt")
# print("Something")
print(f" There are {FileRead.get_total_number_of_lines()} lines in the file {FileRead.fileName}.")

