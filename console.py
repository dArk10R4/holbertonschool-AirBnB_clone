#!/usr/bin/python3
import cmd, sys
# from turtle import *


class HBNBCommand(cmd.Cmd):
    '''doc'''
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
