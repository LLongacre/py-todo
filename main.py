# def list_create(name):
#     return [name]
import sys


def main():
    i = 0
    list_name = ""
    while i == 0:
        my_input = input("Enter todo command:")
        # print("my_input: " + "\""+my_input+"\"")
        if my_input == "exit": 
            exit()
        elif my_input == "create":
           list_name = input("Enter list name:")
        elif my_input == "print_list":
            print("The name of your list is: " + list_name) 
        elif my_input == "delete":
            list_name = ""
        elif my_input == "rename":
            list_name = input("Enter new name")
        elif my_input == "quit":
            i = 1
    print("The name of your list is: " + list_name) 

if __name__ == '__main__':
    sys.exit(main())

