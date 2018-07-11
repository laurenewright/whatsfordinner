import random
dinner_list = []

def show_help():
    print("What's for dinner?")
    print("""
Enter 'DONE' to stop adding items and exit the program.
Enter 'REMOVE to remove an item from the list.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'DINNER' to get a place to go!
""")
def show_list():
    print("Here's your list:")
    
    for item in dinner_list:
        print(item)
 



def add_to_list(new_item):
    dinner_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(dinner_list)))
    
show_help()

def show_random():
    secure_random = random.SystemRandom()
    print(secure_random.choice(dinner_list))
    
    
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        dinner_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


while True:
        new_item = input("> ")
        
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list()
            continue
        elif new_item == 'DINNER':
            show_random()
            continue
        elif new_item.upper() == 'REMOVE':
            remove_from_list()
        else:
            add_to_list(new_item)

