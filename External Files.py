conversation_cards = open("newfile.txt", "w")
conversation_cards.write("I AM A FISH\n")
conversation_cards.close()

# import docx
#
# document = docx.Document()
# heading = document.add_heading('This is a test')
# paragraph = document.add_paragraph('hello there')
# document.save('file.docx')

from Classes import *

student1 = Student("Bob", 19, "Biochemistry", 56, True)
student2 = Graduate("Jeremy", 22, "Physics", 78, False, True)
print(student2.whatdegree())