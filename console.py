#!/usr/bin/env python3
"""
This module defines a command-line interpreter for the AirBnB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()
                obj_key = args[0] + '.' + args[1]
                if obj_key in objects:
                    print(objects[obj_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()
                obj_key = args[0] + '.' + args[1]
                if obj_key in objects:
                    del objects[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances based on class name or all."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                if arg in globals():
                    print([str(obj) for key, obj in objects.items() if key.startswith(arg + '.')])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attributes."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            obj_key = args[0] + '.' + args[1]
            if obj_key not in objects:
                print("** no instance found **")
            else:
                obj = objects[obj_key]
                attribute_name = args[2]
                attribute_value = args[3]
                if hasattr(obj, attribute_name):
                    attribute_type = type(getattr(obj, attribute_name))
                    setattr(obj, attribute_name, attribute_type(attribute_value))
                    obj.save()
                else:
                    print("** attribute name doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
