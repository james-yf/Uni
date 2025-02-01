#@
# SCRIPT TO HANDLE AUTOMATE MY WAM CALCULATIONS
#@

import sys
import time

############################  CONSTANTS ####################################

MAX_COURSE_COUNT = 20   # is 20 and not 24 since 4 already passed via RPL
                        # and hence don't count to WAM

MIN_COURSE_COUNT = 0

MAX_WAM = 100
MIN_WAM = 0

MAX_COURSE_MARK = 100
MIN_COURSE_MARK = 0

UOC_FOR_COURSES = 6

TIME_BEFORE_MENU_APPEARS = 1
###########################################################################

############################  GLOBAL VARIABLES ###############################

current_wam = 0
current_course_count = 0
wam_calc_numerator = 0
wam_calc_denominator = 1
###########################################################################

def get_curr_wam_and_course_count() -> list:
    know_wam = input("Do you know your current WAM (y/n)?: ")
    
    while know_wam != "y" and know_wam != "n":
        know_wam = input('Invalid input! Must answer (y/n) to: Do you know your current WAM?: ')

    course_count = 0
    current_wam = 0

    if know_wam == "y":
        while True:
            try:
                current_wam = int(input("\nWhat is your current WAM?: "))

                if current_wam > MAX_WAM:
                    print("WAM cannot exceed 100! Please re-enter WAM")
                elif current_wam < MIN_WAM:
                    print("WAM cannot be negative! Please re-enter WAM")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number: ")

        while True:
            try:
                course_count = int(input("\nHow many courses have you taken (# courses contributing to WAM)?: "))

                if course_count > MAX_COURSE_COUNT:
                    print("Course count cannot be greater than 20! Please enter a valid number")
                elif course_count <= MIN_COURSE_COUNT:
                    print("Course count cannot be less than or equal to 0! Please enter a valid number")
                else:
                    break
    
            except ValueError:
                print("Invalid input! Please enter a valid number: ")
    
    elif know_wam == "n":
        marks_list = []
    
        while True:
            mark = input("\nTo calculate your current WAM please enter all your course marks: ")
            
            if not mark:
                print("You must enter at least one mark. Please try again.")
                continue  # Ask for input again if it's empty

            try:
                marks = [int(mark) for mark in mark.split()]

                if len(marks) > MAX_COURSE_COUNT:
                    print("You have entered more than the max # of marks, cannot exceed 20!")
                    print("Please re-enter marks.")
                    continue  # Restart input prompt if too many marks are entered

                # Check for invalid marks
                if any(i < MIN_COURSE_MARK for i in marks):
                    print("Marks cannot be negative! Please re-enter marks.")
                    continue  # Restart input prompt if there are negative marks
                if any(i > MAX_COURSE_MARK for i in marks):
                    print("Marks cannot be greater than 100! Please re-enter marks.")
                    continue  # Restart input prompt if marks exceed 100

                # If all marks are valid, add them to the list
                marks_list.extend(marks)
                break  # Exit loop after successfully adding marks

            except ValueError:
                print("Invalid input! Please enter valid numbers.")


        current_wam = calculate_wam(marks_list)
        course_count = len(marks_list)

    curr_wam_and_course_count = [current_wam, course_count]

    return curr_wam_and_course_count
        

def calculate_wam(marks_list) -> float:
    course_count = len(marks_list)

    for mark in marks_list:
        WAM_CALC_NUMERATOR += (mark * UOC_FOR_COURSES)

    wam_calc_denominator  = (course_count * UOC_FOR_COURSES)

    wam = WAM_CALC_NUMERATOR / WAM_CALC_DENOMINATOR
        
    return wam
      
    
def print_menu():
    print("\n--------------------------------")
    print("| Choose one of the following: |")
    print("--------------------------------")
    print("1. Predict WAM")
    print("2. Desired WAM")
    print("3. Quit\n")
    
    
def main():
    curr_wam_and_course_count = get_curr_wam_and_course_count()

    while True:
        time.sleep(TIME_BEFORE_MENU_APPEARS)
        print_menu()
        menu_choice = 3
        
        while True:
            try:
                menu_choice = int(input(": "))

                if menu_choice != 1 and menu_choice != 2 and menu_choice != 3:
                    print("Must be a number between (1-3)! Please re-enter.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number (1-3).")
        
        if menu_choice == 3:
            print("\nTerminating script...\n")
            sys.exit(1)
        elif menu_choice == 1:
            predicted_marks_list = []

            while True:
                what_if_mark = input("\nTo calculate your predicted WAM please enter all your predicted course marks: ")
                
                if not what_if_mark:
                    print("You must enter at least one mark. Please try again.")
                    continue

                try:
                    what_if_marks = [int(what_if_mark) for what_if_mark in what_if_mark.split()]

                    if len(what_if_marks) > MAX_COURSE_COUNT:
                        print("You have entered more than the max # of marks, cannot exceed 20!")
                        print("Please re-enter marks.")
                        continue

                    # Check for invalid marks
                    if any(i < MIN_COURSE_MARK for i in what_if_marks):
                        print("Marks cannot be negative! Please re-enter marks.")
                        continue
                    if any(i > MAX_COURSE_MARK for i in what_if_marks):
                        print("Marks cannot be greater than 100! Please re-enter marks.")
                        continue

                    
                    predicted_marks_list.extend(what_if_marks)
                    break

                except ValueError:
                    print("Invalid input! Please enter valid numbers.")

            
            if len(predicted_marks_list) == 1:
                    is_single = input("Is " + str(predicted_marks_list[0]) + " a mark for a single course, or is it the mark for all remaining courses? [s - single] [a - all]: ")
                    while is_single != "s" and is_single != "a":
                        is_single = input("Invalid input. Please enter [s - single] [a - all] if the mark is for a single course or for all remaining courses: ")
                    
                    if is_single == "s":
                        print("\nPredicted WAM after getting " + str(predicted_marks_list[0]) + " in 1 course is: " + str(calculate_wam(predicted_marks_list)))
                    else:
                        print("\nPredicted WAM after getting " + str(predicted_marks_list[0]) + " in " + len(predicted_marks_list) + " courses is: " + str(calculate_wam(predicted_marks_list)))
                    continue
            else:
                predicted_mark_pos = 1
                print("\nPredicted WAM after getting: ")
                for predicted_mark in predicted_marks_list:
                    print("Predicted mark  " + str(predicted_mark_pos) + ": " + str(predicted_mark))
                    predicted_mark_pos+=1
                
                print("Predicted WAM is: " + str(calculate_wam(predicted_marks_list)))

        else:
            



if __name__ == "__main__":
    main()

