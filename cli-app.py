print("Welcome to the Todo Application")
todolist = []
filepath = 'todolist.txt'

def readfile(todolist, filepath):
    with open(filepath, 'r') as file:
        for line in file:
            todolist.append(line.strip())

#call readfile function so our todolist =[] is updated with latest list from the text file to begin with
readfile(todolist, filepath)
print("Latest updated todolist from db is : " , todolist)

def write2file(todolist, filepath):
    with open(filepath, 'w') as file:
        for item in todolist:
            file.writelines(item + '\n')
    print("latest todolist is saved to the text file.")


while True:
    user_prompt = input("Type the actions you would like to perform: add/edit/delete/show/save/exit! : ")
    match user_prompt:
        case 'add':
           newtodoitem = input("Enter the new todo item : ")
           todolist.append(newtodoitem)
           print(todolist)


        case 'edit':
            print(todolist)
            todoitem2edit = input("Which item you want to edit :")
            # identify the index of the item to be edited
            todoitem2edit_index = todolist.index(todoitem2edit)
            itemafter_edit = input("Enter the todo item after edit :")
            todolist[todoitem2edit_index] = itemafter_edit


        case 'delete':
            print(todolist)
            todoitem2delete = input("Which todo item you want to delete : ")
            # identify the index of the item to be deleted
            todoitem2delete_index = todolist.index(todoitem2delete)
            print(todolist[todoitem2delete_index], " has been deleted successfully!")
            del todolist[todoitem2delete_index]


        case 'show':
            print("current todolist are as follows:")
            print(todolist)

        case 'save':
            write2file(todolist,filepath)

        case 'exit':
            break

        case _:
            print("Invalid command please try again!")