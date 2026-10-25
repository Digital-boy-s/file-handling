# Exercise 1
def write_shopping_list(items,filename):
    file=open(filename, "w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n") 
        c+=1
    file.close()

# Exercise 2
def read_names(filename):
    file=open(filename, "r")
    lines=file.readlines()
    file.close()
    names=[]
    for line in lines:
        hooson=line.strip()
        if hooson!="":
            names.append(hooson)
    return names

# Exercise 3
def append_entry(filename, text):
    file=open(filename, "a")
    file.write(text + "\n")
    file.close()
    file=open(filename, "r")
    lines=file.readlines()
    file.close()
    return len(lines)

# Exercise 4
def search_file(filename, word):
    file=open(filename,"r")
    lines=file.readlines()
    file.close()
    matches=[]
    line_number=1
    word_lower=word.lower()
    for line in lines:
        if word_lower in line.lower():
            matches.append(line_number)
        line_number+=1
    return matches

# Exercise 5
def number_the_lines(source, destination):
    file=open(source,"r")
    lines=file.readlines()
    file.close()
    file=open(destination,"w")
    line_number=1
    for line in lines:
        clean_line=line.strip()
        file.write(f"{line_number}: {clean_line}\n")
        line_number+=1
    file.close()
    return len(lines)


# Exercise 6

#AI ashiglaj bichulsn
# def notes_program():
#     while True:
#         print("--- My Notes ---\n1. Add a note\n2. View all notes\n3. Search notes\n4. Quit")
#         choice=input("Choose 1-4: ")
#         if choice=="1":
#             text=input("Write your note: ")
#             file=open("notes.txt","a")
#             file.write(text+"\n")
#             file.close()
#             print("Note saved.")
#         elif choice=="2" or choice=="3":
#             file=open("notes.txt","a")
#             file.close()
#             file=open("notes.txt","r")
#             lines=file.readlines()
#             file.close()
#             search=input("Search for: ").lower() if choice=="3" else ""
#             found=0
#             for i,line in enumerate(lines,1):
#                 if choice=="2" or search in line.lower():
#                     print(f"{i}. {line.strip()}")
#                     found+=1
#             if choice=="3":
#                 print(f"Found {found} note(s).")
#         elif choice=="4":
#             break
#         else:
#             print("Invalid option, please choose between 1 and 4.")
