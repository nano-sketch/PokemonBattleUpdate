import csv
import random
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())

# Random Pokemon ID
numID = random.randint(1, 898)
numID2 = random.randint(1, 898)
# username
pName = input("Enter your name: ")

# Open the CSV file for pokemon ID
with open("pokemon.csv", mode='r') as file:
    reader = csv.DictReader(file)
    found = False
    for row in reader:
        # find pokemon number from numID
        if row["number"] == str(numID):
            p1_name = row["name"]
            p1_type1 = row["type1"]
            p1_type2 = row["type2"]
            p1_total = row["total"]
            p1_hp = row["hp"]
            p1_attack = row["attack"]
            p1_defense = row["defense"]
            p1_sp_attack = row["sp_attack"]
            p1_sp_defense = row["sp_defense"]
            p1_speed = row["speed"]
            p1_generation = row["generation"]
            p1_legendary = row["legendary"]
            found = True
            break
            
    if not found:
        print("error pokemon id1 not found!")
        

with open("pokemon.csv", mode='r') as file:
    reader = csv.DictReader(file)
    found = False
    for row in reader:
        # find pokemon number from numID
        if row["number"] == str(numID2):
            p2_name = row["name"]
            p2_type1 = row["type1"]
            p2_type2 = row["type2"]
            p2_total = row["total"]
            p2_hp = row["hp"]
            p2_attack = row["attack"]
            p2_defense = row["defense"]
            p2_sp_attack = row["sp_attack"]
            p2_sp_defense = row["sp_defense"]
            p2_speed = row["speed"]
            p2_generation = row["generation"]
            p2_legendary = row["legendary"]
            found = True
            break
            
    if not found:
        print("error pokemon id2 not found!")

##Main##
print("your pokemon is:",p1_name)
print("Your enemies pokemon is:",p2_name)
input("wait")
