placeholderConstructs = """
adjective:good
adjective:bad
verb:low
verb:moderate
verb:extreme
adverb:low
adverb:moderate
adverb:extreme
noun:location
noun:thing
""".split("\n")[1:]

def importData(filename, split):
    file = open(filename, "r")
    returnVal = file.read().split(split)
    file.close()

    return returnVal

class message:
    def __init__(word, message):
        for eachWord in message.split(" "):
            index = None


def grammarAlgorithm(before, after):
    pass

def constructForMe():
    pass

def constructWithPlaceholders():
    pass

    print("Console >> for a list of placeholders, please see kebab's documentation!")
    print("Console >> Remember to use the correct syntax!!")
    print("Console >> Kebab is a program that uses the grammar of your sentences to choose the next word.")
    print("           If the grammar is off, check your message!!!")

    console = input("Console: 'Input Your Message' >> ")
    message = placeholderAlgorithm(console)


console = ""
while console.lower() not in ["construct for me","construct with placeholders"]:
    print("Console >> Would you like the program to make a message for you or would you like to use placeholders")
    print("Console >> 1.) Construct for me")
    print("Console >> 2.) Construct with placeholders")

    console = input("Console: 'Input Your Choice' >> ")

if console.lower() == "construct for me":
    constructForMe()

else:
    constructWithPlaceholders()
