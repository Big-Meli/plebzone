class configItem:
    def __init__(item, name, alias):
        item.name = name
        item.alias = alias

configItems = [
    configItem(".InternalError", "$"),
    configItem(".ExternalError", "$$"),
    configItem(".GenericError", "$$$"), # NEW ADD TO WIKI
    configItem(".SyntaxError", "SyntaxError"),
    configItem(".ValueError", "ValueError"),
    configItem(".ReferenceError", "ReferenceError"),
    configItem(".message", "message"),
    configItem(".wait", "wait"),
    configItem(".set", "set"),
    configItem(".goto", "goto"),
    configItem(".loop", "loop"),
    configItem(".stop", "stop"),
    configItem(".location", "location"),
    configItem(".string", "string"),
    configItem(".int", "int"),
    configItem(".float", "float"),
    configItem(".bool", "bool"),
    configItem(".console", "STEW"),
    configItem(".mundaneAlerts", "No") # NEW ADD TO WIKI
]

def findConfig(name):
    global configItems

    foundItem = ""

    for eachItem in configItems:
        if eachItem.name == name:
            foundItem = eachItem.alias

    return foundItem

class variable:
    def __init__(variable, name, value, type, const = False):
        variable.name = name
        variable.type = type
        variable.const = const

        try:
            if type == findConfig(".string") or type == "_s":
                variable.value = str(value)
            elif type == findConfig(".int") or type == "_i":
                variable.value = int(value)
            elif type == findConfig(".float") or type == "_f":
                variable.value = float(value)
            elif type == findConfig(".boolean") or type == "_b":
                variable.value = bool(value)
        except:
            print("{} >> {}{} >> Could not parse variable: {} as {}!".format(
                findConfig(".console"), findConfig(".ExternalError"), findConfig(".ValueError")
            ))
            quit()

variables = [
    variable("_ds", "//", "_s", True),
    variable("_sm", '"', "_s", True),
    variable("_sq", "'", "_s", True),
    variable("_nl", "", "_s", True),
    variable("_:", ":", "_s", True),
    variable("_ar", "shaun", "_s", True),
    variable("_true", "True", "_b", True),
    variable("_false", "False", "_b", True)
]

def compileConfig(filename = "main"):
    global configItems

    try:
        filename += "_conf.stew"

        file = open(filename, "r")
        configLoad = file.read()
        file.close()
    except:
        print("{} >> {}{} >> File: '{}' could not be located! Did you specify the right path? If no path is specified, is it in the same folder as your stew?".format(
            findConfig(".console"), findConfig(".ExternalError"), findConfig(".ReferenceError"), filename
        ))
        quit()
    configChunk = configLoad.split("\n")

    for configBlock in configChunk:
        configBlock = configBlock.split("//")[0]
        if not configBlock.startswith("//") and not len(configBlock) == 0:
            configBlockItems = configBlock.split(" ")
            if configBlockItems[1] == "as":
                for confItem in configItems:
                    if configBlockItems[0] == confItem.name:
                        confItem.alias = " ".join(configBlockItems[2:])
            else:
                print("{} >> {}{} >> Must use 'as' to define an alias in the {} config file!".format(
                    findConfig(".console"),findConfig(".InternalError"),findConfig(".SyntaxError"), filename
                ))
                quit()

compileConfig()

def boilStew(filename):
    global variables
    global configItems

    try:
        file = open((filename+".stew"), "r")
        boiledStew = file.read()
        file.close()
    except:
        print("{} >> {}{} >> Could not open file: '' because it does not exist! Did you specify the correct path? Did you type the correct name (Case Sensitive)?".format(
            findConfig(".console"), findConfig(".ExternalError"), findConfig(".ReferenceError"), filename
        ))
        quit()

    lineNumber = 1
    for eachLine in boiledStew.split("\n"):
        eachLine = eachLine.split("//")[0]
        rawLineArgs = eachLine.split(" ")

        if len(rawLineArgs[0]) != 0:
            if rawLineArgs[0] == findConfig(".message"):
                messageSuffix = ""
                messagePrefix = ""
                eachLineArgs = eachLine.split('"')

                try:
                    messageSuffix = eachLineArgs[1]
                except:
                    print("{} >> {}{}:{} >> Not enough arguments for keyword: '.message' with alias: {}".format(
                    findConfig(".console"), findConfig(".ExternalError"), findConfig(".SyntaxError"), lineNumber
                    ))
                    quit()

                fromHandled = False
                for i in range(len(eachLineArgs)):
                    try:
                        if eachLineArgs[i].startswith(" @from") and fromHandled == False:
                            messagePrefix = eachLineArgs[i+1]
                            fromHandled = True

                        elif fromHandled == False:
                            messagePrefix = findConfig(".console")+" >> "

                    except:
                        print("{} >> {}{}:{} >> Could not parse a 'nullobject' as a real object, not enough arguments!".format(
                        findConfig(".console"), findConfig(".ExternalError"), findConfig(".SyntaxError"), lineNumber
                        ))
                        quit()

                for var in variables:
                    messageSuffix = messageSuffix.replace(("$"+var.name), str(var.value))

                    if findConfig(".mundaneAlerts") != "No":
                        print("{} >> {}{}:{} >> STEW has parsed a value: '{}' as a 'string' so that it can be put in keyword: '{}' placeholder for variable: '{}'!".format(
                            findConfig(".console"), findConfig(".GenericError"), findConfig(".ValueError"), lineNumber, findConfig(".message"), var.name
                        ))

                print(messagePrefix + messageSuffix)

            else:
                print("{} >> {}{} >> Undefined or unrecognised keyword: '{}'!".format(
                    findConfig(".console"), findConfig(".ExternalError"), findConfig(".SyntaxError"), rawLineArgs[0]
                ))

        lineNumber += 1

def stirStew():
    console = input("{} >> What file would you like to open up? >> ".format(
        findConfig(".console")
    ))

    consoleWith = console.split(" ")
    for i in range(len(consoleWith)-1):

        try:
            if consoleWith[i] == "config" and consoleWith[i-1] == "@with":
                compileConfig(consoleWith[i+1])
        except:
            print("{} >> {}{} >> You have written a condition without the require amount of arguments, these conditions look like:")
            print("{} >> What file would you like to open up? >> main @with config main")
            print('{} >> What file would you like to open up? >> main @with config main @with config .ValueError @set as "Incorrect typing error"')
            quit()

    boilStew(console)
    print("\nSTEW >> $Finished >> Finished compiling stew with name '{}'!".format(
        console
    ))
    console = input("STEW >> $Finished >> Press enter to shut down!")

stirStew()
