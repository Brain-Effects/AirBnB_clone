#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        if sys.stdin.isatty():
            print()
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_help(self, arg):
        """
        Help command
        """
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
