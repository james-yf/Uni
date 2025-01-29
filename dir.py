# SCRIPT TO AUTOMATE DIRECTORY CREATIONS FOR MY COMP COURSES

import os
import sys

def exit_ ():
    print("Terminating script...")
    sys.exit(1)


def continue_creation_prmpt():
    continue_ans = input("\nDo you still want to add directories? (y/n): ")
    while continue_ans != "y" and continue_ans != "n":
        continue_ans = input("\nInvalid input. Please enter (y/n) if you want to continue making directories or exit: ")
    if continue_ans == "n":
        exit_ ()


def create_child_directories(par_name, par_path, child_count):
    if par_name == "labs":
        for i in range(1, child_count + 1) :
            if i < 10:
                child_name = "lab0" + str(i)
            else:
                child_name = "lab10" 
        
            child_path = os.path.join(par_path, child_name)
            os.mkdir(child_path, 0o700)
            print("Created: " + "{" + child_path + "}")
    elif par_name == "ass":
        for i in range(1, child_count + 1) :
            child_name = "ass0" + str(i)
            child_path = os.path.join(par_path, child_name)
            os.mkdir(child_path, 0o700)
            print("Created: " + "{" + child_path + "}")
    else:
        child_name_no_nums = par_name[:-1]        # e.g., if [par_name = tests] => [child_name_no_nums = test]
        for i in range(1, child_count + 1) :
            if i < 10:
                child_name = child_name_no_nums + "0" + str(i)
            elif i == 10:
                child_name = child_name_no_nums + "10"
            elif i > 10 and i < 20:
                child_name = child_name_no_nums + "1" + str(i)
            child_name = child_name_no_nums + str(i)
            child_path = os.path.join(par_path, child_name)
            os.mkdir(child_path, 0o700)
            print("Created: " + "{" + child_path + "}")
            
  
def main():
    course_name = input("What is the name of your course?: ")
    course_name_exists = os.path.isdir(course_name)

    if course_name_exists:
        print("\n{" + course_name + "}" + " already exists.")
        course_name_list_dir = os.listdir(course_name)    
        l = len(course_name_list_dir)      
        if l > 0:
            index = 1
            if l == 1:
                print("There is " + str(l) + " file in " + course_name + " (not including child directories)" + ": ")
            else:
                print("There are " + str(l) + " files in " + course_name + " (not including child directories)" + ": ")
            for i in course_name_list_dir:
                print("file " + str(index) + ": " + i)   
                index += 1
        else:
            print("It is empty.")
    
    else:
        os.mkdir(course_name, 0o700)
        print("Created: " + "{" + course_name + "}")

    dir_creation(course_name)


def dir_creation(course_name):
    continue_creation_prmpt()

    while True:
        par_name = input("\nEnter the name of the dir you want: ")
        par_path = os.path.join(course_name, par_name)
    
        while os.path.isdir(par_path) == True:
            print("\nA directory with name " + "{"+ par_name + "}" + " already exists.")
            continue_creation_prmpt()
            par_name = input("\nEnter a different directory name: ")
            par_path = os.path.join(course_name, par_name)

        os.mkdir(par_path, 0o700)
        print("Created: " + "{" + par_path + "}")

        child_count = int(input("\nHow many child directories for " + "{" + par_name + "}?: "))
        if child_count > 0:
            create_child_directories(par_name, par_path, child_count)
            
        continue_creation_prmpt()


if __name__ == "__main__":
    main()