#!/usr/bin/env python3
"""
This module defines the HBNBCommand class, a custom command interpreter
for managing AirBnB objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter for AirBnB objects.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D).
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of the specified class, save it,
        and print its ID.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance based
        on class name and ID.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and ID.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if obj:
                storage.delete(obj)
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on class name.
        """
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            try:
                print([str(obj) for obj in objs.values()
                       if obj.__class__.__name__ == arg])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance attribute based on class name, ID,
        attribute name, and value.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if not obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            if attr_name in ["id", "created_at", "updated_at"]:
                print("** cannot update id, created_at, or updated_at **")
                return
            setattr(obj, attr_name, attr_value)
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
