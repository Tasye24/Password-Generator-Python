# -*- coding: utf-8 -*-
# coding: utf-8
import random
import Languages.worker as Lang
import os


def Language(a):
    return Lang.L(a)

# Letters ? Number ? Caracters ?

types = ["Letter", "Number", "Caracters"]
help = ["", f"""
(1)
    Letter<boolean> 1 or 0
    Number<boolean> 1 or 0
    Caracters<boolean> 1 or 0

    {Language("Help1msg")}: 001
"""]

class Tasye:
    def __init__(self, length, letter, number, caracters):
        self.length = length
        self.letter = letter
        self.number = number
        self.caracters = caracters
    def GeneratePassword(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" if self.letter else ""
        numbers = "0123456789" if self.number else ""
        caracters = "&~é#\"\\'{^}%()[]|è`_ç^@à°=+-ù$£*µ!§:;,?./¤* " if self.caracters else ""
        
        full_def = ""
        full_def += numbers 
        full_def += caracters
        full_def += letters

        i=0
        response = ""
        while i < self.length:
            i= i+1
            response += full_def[random.randrange(0, len(full_def))]
        return response

print(help[1])
input_type = input(f"{Language('ask001')} (1): ")
os.system("cls" if os.name == "nt" else 'clear')

input_type = [int(x) for x in str(input_type)]
print(input_type)

length = int(input(f"{Language('ask002')} :"))

NewPassword = Tasye(length, input_type[0], input_type[1], input_type[2]).GeneratePassword()

print(f"{Language('result')} : {NewPassword}")