# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:05:01 2022

@author: BRGUBO
"""
from random import randint
import winsound

import pyfiglet

def screen_title (screen_text):
    title_screen = pyfiglet.figlet_format(screen_text, font = "standard")
    print(title_screen)




screen_title("Multiplication Table")

frequency_correct = 2500  # Set Frequency To 2500 Hertz
duration_correct = 300  # Set Duration To 1000 ms == 1 second
frequency_wrong = 500  # Set Frequency To 2500 Hertz
duration_wrong = 500  # Set Duration To 1000 ms == 1 second
right_counter = 0



trials = 50



for counter in range(trials):   
    
    first_num = randint(0,10)
    second_num = randint(0,10)
    print("======================================================")
    print (f"\n     {first_num} X {second_num} = ? ")
    correct_answer = first_num*second_num
    answer = int(input())
    
    
    if answer == correct_answer:
        winsound.Beep(frequency_correct, duration_correct)
        print (" \n**** GREAT - CORRECT!!!! *****")
        print (f"\n     {first_num} X {second_num} = {correct_answer} ")
        right_counter = right_counter + 1
    else:
        print(f"\n*** WRONG **** - the correct is:  {correct_answer}")
        print (f"\n     {first_num} X {second_num} = {correct_answer} ")
        winsound.Beep(frequency_wrong, duration_wrong)

    counter = counter + 1
    perc_right_answer = right_counter / counter * 100
    print(f"\nPercentage of correct answer is: {round(perc_right_answer,1)} %")
    print(f"Trial number: {counter} of {trials}")

          
print('\n\n - Great that you were here')
print(f"\nPercentage of correct answer is: {round(perc_right_answer,1)} %")
print(f"Trial number: {counter} of {trials}")



if perc_right_answer < 70:
    screen_title("YOU ARE BULLSHIT BAD ")
elif perc_right_answer < 80:
     screen_title("COULD BE BETTER")
elif perc_right_answer < 90:
     screen_title("ALMOST THERE")
elif perc_right_answer < 100:
     screen_title("GREAT JOB")
else:
    screen_title("YOU ARE THE BEST")


print('\n\n ...type something to end program')
a= input()





