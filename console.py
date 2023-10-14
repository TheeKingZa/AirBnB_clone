#!/usr/bin/env python3
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

    def do_create(self, line):
        """
        Create a new instance of a BaseModel and save it.
        Usage: create <class_name>
        Example: create BaseModel
        """
        pass

    def do_show(self, line):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-5678
        """
        pass

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 1234-5678
        """
        pass

    def do_all(self, line):
        """
        Print all string representations of instances.
        Usage: all [class_name]
        Example: all or all BaseModel
        """
        pass

    def do_update(self, line):
        """
        Update an instance based on the class name and id.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        Example: update BaseModel 1234-5678 name "John"
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
