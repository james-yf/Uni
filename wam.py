#@
# SCRIPT TO HANDLE MY WAM CALCULATIONS
#@

import sys
import time
import math

############################  CONSTANTS ####################################

MAX_COURSE_COUNT = 20   # is 20 and not 24 since 4 already passed via RPL
                        # and hence don't count to WAM

MIN_COURSE_COUNT = 0

MAX_WAM = 100
MIN_WAM = 0

MAX_COURSE_MARK = 100
MIN_COURSE_MARK = 0

UOC_FOR_COURSES = 6

TIME_BEFORE_MENU_APPEARS = 2
###########################################################################

############################  GLOBAL VARIABLES ###############################

current_wam = 0
current_course_count = 0    # of course that contribute to the current wam
wam_calc_numerator = 0
wam_calc_denominator = 0
###########################################################################

def get_curr_wam_and_course_count():
    global current_wam
    global current_course_count
    global wam_calc_numerator
    global wam_calc_denominator

    know_wam = input("Do you know your current WAM (y/n)?: ")
    
    while know_wam != "y" and know_wam != "n":
        know_wam = input('Invalid input! Must answer (y/n) to: Do you know your current WAM?: ')

    if know_wam == "y":
        while True:
            try:
                current_wam = float(input("\nWhat is your current WAM?: "))

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
                current_course_count = int(input("\nHow many courses have you taken (# courses contributing to WAM, includes WAM affecting fails)?: "))

                if current_course_count > MAX_COURSE_COUNT:
                    print("Course count cannot be greater than 20! Please enter a valid number")
                elif current_course_count <= MIN_COURSE_COUNT:
                    print("Course count cannot be less than or equal to 0! Please enter a valid number")
                else:
                    break
    
            except ValueError:
                print("Invalid input! Please enter a valid number: ")

        wam_calc_numerator = current_wam * (current_course_count * UOC_FOR_COURSES)
        wam_calc_denominator = (current_course_count * UOC_FOR_COURSES)
    
    elif know_wam == "n":
        current_marks_list = []
    
        while True:
            current_mark = input("\nTo calculate your current WAM please enter all your course marks: ")
            
            if not current_mark:
                print("You must enter at least one mark. Please try again.")
                continue  # Ask for input again if it's empty

            try:
                current_marks = [int(current_mark) for current_mark in current_mark.split()]

                if len(current_marks) > MAX_COURSE_COUNT:
                    print("You have entered more than the max # of marks, cannot exceed 20!")
                    print("Please re-enter marks.")
                    continue  # Restart input prompt if too many marks are entered

                # Check for invalid marks
                if any(i < MIN_COURSE_MARK for i in current_marks):
                    print("Marks cannot be negative! Please re-enter marks.")
                    continue  # Restart input prompt if there are negative marks
                if any(i > MAX_COURSE_MARK for i in current_marks):
                    print("Marks cannot be greater than 100! Please re-enter marks.")
                    continue  # Restart input prompt if marks exceed 100

                # If all marks are valid, add them to the list
                current_marks_list.extend(current_marks)
                break  # Exit loop after successfully adding marks

            except ValueError:
                print("Invalid input! Please enter valid numbers.")

        current_wam = calculate_wam(current_marks_list)
        current_course_count = len(current_marks_list)


def calculate_wam(marks_list) -> float:
    course_count = len(marks_list)
   
    global wam_calc_numerator 
    for mark in marks_list:
        wam_calc_numerator += (mark * UOC_FOR_COURSES)
    
    global wam_calc_denominator 
    wam_calc_denominator += (course_count * UOC_FOR_COURSES)

    wam = (wam_calc_numerator / wam_calc_denominator)

    rounded_wam = round(wam, 2)
        
    return rounded_wam


# @ Formula used:
# required average mark = (desired WAM * total units - current WAM * taken units)/(total units - taken units)
# @
def calculate_required_avg(desired_wam) -> int:
    required_avg = (desired_wam * MAX_COURSE_COUNT - current_wam * current_course_count) / (MAX_COURSE_COUNT - current_course_count) 
    return required_avg
      
    
def print_menu():
    print("\n--------------------------------")
    print("| Choose one of the following: |")
    print("--------------------------------")
    print("1. Predict WAM")
    print("2. Desired WAM")
    print("3. Quit\n")
    
    
def main():
    get_curr_wam_and_course_count()

    while True:
        time.sleep(TIME_BEFORE_MENU_APPEARS)
        print_menu()
        
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
        
        print("\nCurrent WAM is: " + str(current_wam))
        print("Current course count is: " + str(current_course_count))

        if menu_choice == 1:
            predicted_marks_list = []

            while True:
                predicted_mark = input("\nTo calculate your predicted WAM please enter all your predicted course marks: ")
                
                if not predicted_mark:
                    print("You must enter at least one mark. Please try again.")
                    continue

                try:
                    predicted_marks = [int(predicted_mark) for predicted_mark in predicted_mark.split()]

                    leftover_course_count = (MAX_COURSE_COUNT - current_course_count)
                    if len(predicted_marks) > leftover_course_count:
                        print("You have entered more marks than remaining courses. Cannot exceed: " + leftover_course_count)
                        print("Please re-enter marks.")
                        continue

                    # Check for invalid marks
                    if any(i < MIN_COURSE_MARK for i in predicted_marks):
                        print("Marks cannot be negative! Please re-enter marks.")
                        continue
                    if any(i > MAX_COURSE_MARK for i in predicted_marks):
                        print("Marks cannot be greater than 100! Please re-enter marks.")
                        continue

                    predicted_marks_list.extend(predicted_marks)
                    break

                except ValueError:
                    print("Invalid input! Please enter valid numbers.")

            
            if len(predicted_marks_list) == 1:
                    is_single = input("\nIs " + str(predicted_marks_list[0]) + " a mark for a single course, or is it the mark for all remaining courses? [s - single] [a - all]: ")
                    while is_single != "s" and is_single != "a":
                        is_single = input("Invalid input. Please enter [s - single] [a - all] if the mark is for a single course or for all remaining courses: ")
                    
                    if is_single == "s":
                        print("\nPredicted WAM after getting " + str(predicted_marks_list[0]) + " in 1 course is: " + str(calculate_wam(predicted_marks_list)))
                    else:
                        remaining_course_count = (MAX_COURSE_COUNT - current_course_count)
                        for i in range (1, remaining_course_count):
                            predicted_marks_list.append(predicted_marks_list[0])
                        print("\nPredicted WAM after getting " + str(predicted_marks_list[0]) + " in " + str(MAX_COURSE_COUNT - current_course_count) + " remaining courses is: " + str(calculate_wam(predicted_marks_list)))
                    continue
            else:
                predicted_mark_pos = 1
                print("\nPredicted WAM after getting: ")
                for predicted_mark in predicted_marks_list:
                    print("Predicted mark  " + str(predicted_mark_pos) + ": " + str(predicted_mark))
                    predicted_mark_pos+=1
                
                print("is: " + str(calculate_wam(predicted_marks_list)))

        else:
            while True:
                try:
                    desired_wam = int(input("\nWhat is your desired WAM?: "))

                    if desired_wam > MAX_WAM:
                        print("WAM cannot exceed 100! Please re-enter WAM")
                    elif desired_wam < MIN_WAM:
                        print("WAM cannot be negative! Please re-enter WAM")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number: ")

            required_avg = calculate_required_avg(desired_wam)

            #take ceiling of avg to account for float course marks which are not given,
            #marks are always an int
            required_avg = math.ceil(required_avg)

            print("\nYour required average course mark to get " + str(desired_wam)+ " WAM is: " +  str(required_avg))

            if required_avg > 100:
                print("It is mathematically impossible for you to get " + str(desired_wam) + " WAM")
            else:
                print("For each course you get below " + str(required_avg) +  " you will increase the average you need to get for the rest.")
                print("For each course you get above " + str(required_avg) + " you will decrease the average you need to get for the rest.")


if __name__ == "__main__":
    main()

