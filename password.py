import random  
import os
import termcolor
from termcolor import colored

os.system("clear")

list1=["white","green","yellow","blue","cyan","magenta"]

colors=random.choice(list1)

list2=["yellow","white","magenta","cyan", "blue" ,"green"]

colors2=random.choice(list1)

Title=colored("""
  ____                                
 / ___| ___ _ __  _ __   __ _ ___ ___ 
| |  _ / _ \ '_ \| '_ \ / _` / __/ __|
| |_| |  __/ | | | |_) | (_| \__ \__ \"
 \____|\___|_| |_| .__/ \__,_|___/___/
                 |_|                  

      
                        by Mal4D
""",colors)

print(Title)

lower=("abcdefghijklmnopqrstuvwxyz" )
 
uper=("ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
 
nums=("0123456789" )
 
symbols=("""&é#{[|`\^@]}(-_à)""" )
 
all= (lower + uper+ nums + symbols)

length = int(input ('Enter the number of your pass length (use numbers!!!) : ' ) )
 
password=colored("".join(random.sample(all,length)),"yellow") #or you can use colors2
 
print("The Password You Generated is: " , (password))
                                                    