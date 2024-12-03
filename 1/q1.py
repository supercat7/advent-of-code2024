# pair up smallest number from left list to right list and then figure out the distance, do this over and over again until you find the total distance.

from os.path import dirname
lines = []
with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

lefts = []
rights = []
full_dict = {}
final_count = 0
similarity_score = 0

for element in lines:
    parts = element.split() 
    if len(parts) == 2:
        lefts.append(parts[0])
        rights.append(parts[1])
    else:
        continue

lefts_sorted = sorted(lefts)
rights_sorted = sorted(rights)

for i in lefts_sorted:
    for j in rights_sorted:
        full_dict[i] = j
        rights_sorted.remove(j)
        break

for key, value in full_dict.items():
    distance = 0
    if int(key) > int(value):
        distance = int(key) - int(value)
    elif int(value) > int(key):
        distance = int(value) - int(key)
    final_count += distance

for i in lefts:
    amt = 0
    for j in rights:
        if int(i) == int(j):
            amt += 1
    
    similarity_score += int(i) * amt


print(f"Total distance is: {final_count}")
print(similarity_score)