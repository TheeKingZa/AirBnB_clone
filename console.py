#!/usr/bin/env python3
# Console.py

import cmd
import models

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
        Create a new instance of a specified class and save it.
        Usage: create <class_name>
        Example: create BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if not hasattr(models, class_name):
            print("** class doesn't exist **")
            return

        new_instance = getattr(models, class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-5678
        """
        args = line.split()
        if len(args) < 2:
            print("** class name and/or id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if not hasattr(models, class_name):
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 1234-5678
        """
        args = line.split()
        if len(args) < 2:
            print("** class name and/or id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if not hasattr(models, class_name):
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, line):
        """
        Print all string representations of instances.
        Usage: all [class_name]
        Example: all or all BaseModel
        """
        args = line.split()
        if len(args) > 0 and not hasattr(models, args[0]):
            print("** class doesn't exist **")
            return

        if len(args) == 0:
            objects = models.storage.all().values()
        else:
            objects = [obj for obj in models.storage.all().values() if obj.__class__.__name__ == args[0]]

        print([str(obj) for obj in objects])

    def do_update(self, line):
        """
        Update an instance based on the class name and id.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        Example: update BaseModel 1234-5678 name "John"
        """
        args = line.split()
        if len(args) < 4:
            print("** class name, id, attribute name, and/or value missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        if not hasattr(models, class_name):
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            obj = models.storage.all()[key]
            try:
                attribute_value = eval(attribute_value)
            except:
                pass
            setattr(obj, attribute_name, attribute_value)
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
