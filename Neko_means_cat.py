#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:47:24 2020

@author: earthrunner
"""

from playsound import playsound
import pandas as pd
import random

path = "./japanese_sounds.xlsx"

df_japanese_sounds = pd.read_excel(path, header=None)


#print (df_japanese_sounds)


while True:
    print("----------------------------------------------------------------------------")
    random_mp3_index = random.randint(1, 2)
    #print (konsonant)
    #print (vokal)
    random_mp3_asked = (df_japanese_sounds.iat[random_mp3_index, 3])
    #print (random_kana)
    #print (random_mp3)
    #random_kana1 = (data_frame_hiragana.iat[konsonant, 0]).strip()
    #random_kana2 = (data_frame_hiragana.iat[0, vokal]).strip()
    mp3File = random_mp3_asked
    # Input an existing mp3 filename
    #mp3File = input("Enter a mp3 filename: ")
    # Play the mp3 file
    playsound(mp3File)


    random_translation_1 = random.randint(1, 2)
    random_translation_2 = random.randint(1, 2)

    answer_keys = ["1","2","3"]

    print ("Which one of the following translations is true?")
    print(" ")
    correct_answer = (df_japanese_sounds.iat[random_mp3_index, 2])
    possible_answer_2 = (df_japanese_sounds.iat[random_translation_1, 2])
    possible_answer_3 = (df_japanese_sounds.iat[random_translation_2, 2])

    possible_answers = []
    
    possible_answers.append(correct_answer)
    possible_answers.append(possible_answer_2)
    possible_answers.append(possible_answer_3)

    shuffled_answers = possible_answers[:]
    random.shuffle(shuffled_answers)
    #print (answer_keys)
    #print (shuffled_answers)

    dictionary = dict(zip(answer_keys, shuffled_answers))

    
    for kv in dictionary.items():
        print (kv[0],'\t',kv[1])
    user_answer = input("Please select the correct translation (press 1, 2, 3 or r for replay sound): ").strip().lower()
    if user_answer == "end":
        print ("See You soon!  Thanks for learning the hiragana!")
        break
    elif user_answer == "r":
        playsound(mp3File)
        secondtry = input("Type in your answer now: ").strip().lower()
        if dictionary[secondtry] == correct_answer:
            print ("well done...keep on parcticing...")
            print("The next japanese word sounds like this...")
        else:
            print ("Not quite well. Go back to language school")
            print ("The correct translation to is: " + correct_answer)
            print ("Now...continue to become a mighty Neko!!!")
    elif dictionary[user_answer] == correct_answer:
        print ("well done...keep on parcticing...")
        print("The next japanese word sounds like this...")
    else:
        print ("Not quite well. Go back to language school")
        print ("The correct translation to is: " + correct_answer)
        print ("Now...continue to become a mighty Neko!!!")


"""for key in dictionary:
    print (dictionary[key])

given = input("Type your sanswer 1, 2 or 3: ").strip().lower()


if (dictionary[str(given)]) == question:
    print ("Well doen")
else:
    print("go back to school")

"""
"""

while True:
   
    random_kana = "X"
    while random_kana == "X":
        konsonant = random.randint(1, 14)
        vokal = random.randint(1, 4)
        #print (konsonant)
        #print (vokal)
        random_kana = (data_frame_hiragana.iat[konsonant, vokal])
        #print (random_kana)
    
    random_kana1 = (data_frame_hiragana.iat[konsonant, 0]).strip()
    random_kana2 = (data_frame_hiragana.iat[0, vokal]).strip()

    #print("My sound starts with: ... " + random_kana1)
    #print ("My sound ends with: ... " + random_kana2)
    print ((random_kana) + "   I sound like.... ")

    word_given = input("Type your solution: ").strip().lower()
    if word_given == "end":
        print ("See You soon!  Thanks for learning the hiragana!")
        break
    elif random_kana1 + random_kana2 == word_given:
        print ("WELL DONE")
        print ("The next kana is...")
    else:
        print("Try again...please follow the hebrun system!")
        print("The correct answer to the hiragana " + random_kana + " is: " + random_kana1 + random_kana2)             
       


"""
