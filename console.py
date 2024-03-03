#!/usr/bin/python3
'''doc'''
import cmd
# from models.base_model import BaseModel
from models import base_model
from models import classes

from models import storage
import copy
# from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''doc'''
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            my_class = classes.get(arg)
            if my_class:
                my_model = my_class()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) > 1:
            if hasattr(base_model, args[0]):
                storage.reload()
                for key, value in  storage.objects.items():
                    ids = key.split(".")[1]
                    if ids ==  args[1]:
                        print(value)
                        return
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** instance id missing **")
            return

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) > 1:
            if hasattr(base_model, args[0]):
                storage.reload()
                for key, value in  storage.objects.items():
                    ids = key.split(".")[1]
                    if ids ==  args[1]:
                        storage.objects.pop(key)
                        storage.save()
                        return
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** instance id missing **")
            return

    def do_all(self, arg):
        if not arg or hasattr(base_model, arg):
            storage.reload()
            objs = []
            for obj_id in storage.objects.keys():
                obj = storage.objects[obj_id]
                objs.append(obj)
                print(obj)
        elif arg:
            print("** class doesn't exist **")

    def do_update(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if not hasattr(base_model, args[0]):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        storage.reload()
        for key, value in  storage.objects.items():
            ids = key.split(".")[1]
            if ids ==  args[1]:                
                setattr(storage.objects[key], args[2], args[3])
                storage.save()
                return
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
