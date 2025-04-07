### Apollo's Command Line Interface
###
from sys import exit

# this is where you add the actions you want your program to have.
# If you put words in these quotation marks, " ", it means those words are for humans.
#   We call those "strings", like a "string of letters and spaces."
#   The computer should not try to treat strings as code.
#
cypher = {
    "a": "z",
    "b": "y",
    "c": "x",
    # "d": "yell!",
    # "e": "spit out chompy pillows",
    # "f": "spit out eaten objects",
    # "g": "break!",
    # "h": "help!",
    "x": "c",
    "y": "b",
    "z": "a",
}

def use_cypher(m):
    return m

def main():
    print ("hello!") 
    message = input("Type your message:  ")
    encoded_message = use_cypher(message)
    print(encoded_message)

    # while True: # this program will keep running until we tell it to stop
    #     # collect commands from the user
    #     if "help".startswith(command): # if the user typed the beginning of "help"
    #         print(help_message())
    #         continue # go on to the next loop
    #     if "exit".startswith(command): # if the user typed the beginning of "exit"
    #         end_program()

    #     # look up action from list
    #     action = commands.get(command)
    #     if action:
    #         # hooray! we found a command in the list!
    #         print(action)
    #     elif command:
    #         # could not find any action for the given command
    #         print("I don't know what \"" + command + "\" means.")
    #     else:
    #         # the user just clicked "return" probably and didn't type anything
    #         print("Hey, please enter a command!")

if __name__ == "__main__":
    main()
