#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exit from the command interpreter"""
        return True
    def do_EDF(self, arg):
        """EOF to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
