from ast import List
from re import search
from getch import getch
import os

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}

command_list = ["p", "s", "l", "a", "d", "m", "as"]


def clear_screen():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For macOS and Linux
    else:
        _ = os.system("clear")


def print_functional():
    print("User menu:")
    print("p.\tPeople")
    print("s.\tShelf")
    print("l.\tList")
    print("a.\tAdd")
    print("d.\tDelete")
    print("m.\tMove")
    print("as.\tAdd shelf")


def get_people():
    doc_number = str(input("Введите номер документа:"))
    found_status = False
    for i in documents:
        if doc_number == i["number"]:
            print(f"{i['name']} is author of {i['number']}")
            found_status = True
    if not found_status:
        print("Author not found")


def get_shelf():
    doc_number = str(input("Введите номер документа:"))
    found_status = False
    for i, j in directories.items():
        if doc_number in j:
            print(f"{doc_number} is on the {i}rd shelf")
            found_status = True
    if not found_status:
        print("Document not found in the closet")


def get_list():
    for i in documents:
        print(f"{i['type']} {i['number']} {i['name']}")


def add_doc(documents, directories):
    type = str(input("Input type of document:"))
    name = str(input("Input name of document:"))
    number = str(input("Input number of document:"))
    shelf_number = str(input("Input shelf numember"))
    if shelf_number not in directories.keys():
        print("Directory not found")
    else:
        documents.append({"type": type, "number": number, "name": name})
        directories[shelf_number].append(number)
    print(directories)
    print(documents)
    return documents, directories


def delete_doc():
    doc_number = str(input("Input document number for delete:"))
    doc_list = []
    for doc in documents:
        doc_list.append(doc["number"])
    if doc_number in doc_list:
        for dir in directories.values():
            for item in dir:
                if item == doc_number:
                    dir.remove(doc_number)
        for doc in documents:
            if doc_number == doc["number"]:
                documents.remove(doc)
    else:
        print("Document not found!")
    print(documents)
    print(directories)


def move():
    search_status = False
    document = str(input("Input document number:"))
    move_dir = str(input("Input shelf number:"))
    for doc in documents:
        if doc["number"] == document:
            print("Doc was found")
            for dir in directories.keys():
                if dir == move_dir:
                    search_status = True
                    print("Dir was found")
    if search_status:
        for dir in directories.values():
            if document in dir:
                dir.remove(document)
        directories[move_dir].append(document)
        print(directories)
        print(documents)


def add_shelf():
    shelf_number = str(input("Input number of new shelf:"))
    if shelf_number in directories.keys():
        print("The shelf is already exist!")
    else:
        directories.update({shelf_number: []})
        print("Shelf added")
    print(directories)


def command_call(user_input):
    global documents
    global directories
    match user_input:
        case "p":
            get_people()
        case "s":
            get_shelf()
        case "l":
            get_list()
        case "a":
            documents, directories = add_doc(documents, directories)
        case "d":
            delete_doc()
        case "m":
            move()
        case "as":
            add_shelf()


def menu():
    while True:
        print_functional()
        try:
            command = str(input("Input command: ")).lower()
            if command not in command_list:
                raise Exception("Command not found!")
        except Exception as e:
            print(f"Error:{e}")
            print("Press any key to continue...")
            _ = getch()
            clear_screen()
            continue
        command_call(command)
        print("Press any key to continue...")
        _ = getch()
        clear_screen()


if __name__ == "__main__":
    menu()
