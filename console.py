#!/usr/bin/env python3
# console.py

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Quit the command interpreter.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
