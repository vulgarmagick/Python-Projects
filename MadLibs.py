#Practice 1:  Mad Libs Generator
"""
(Mad libs Generator)
(----------------------)
"""

#loop back to this spot
loop = 1

while (loop < 10):

#Questions and Answers
    noun = input("Choose a noun: ")

    P_noun = input("Choose a plural noun: ")

    noun2 = input("Choose a noun: ")

    place = input("Choose a place: ")

    adj = input("Choose a descriptive word (adjective): ")

    noun3 = input("Choose a noun: ")

#Displays the Story based on User inputs

    print("-----------------------")

    print("Be kind to your",noun,"- footed", P_noun)

    print("For a duck may be somebody's",noun2,",")

    print("Be kind to your", P_noun, "in", place)

    print("Where the weather is always",adj,".")

    print()

    print("You may think that is this the", noun3, ",")

    print("Well it is.")

    print("------------------------")

#loop back to "loop = 1"
loop = loop + 1
