skills = ["Football", "Tennis", "Gaming", "Cooking"]
# print (skills)
name = input("Enter your Name: ")
age = input ("Enter you Age: ")
experience = input("Enter your Years of experience: ")


cv = {
    "name" : name,
    "age" : age,
    "experience" : experience,
    "skills" : [], 
}
# print(cv)

counter = 0
while counter<len(skills):
    print(counter+1, ". ", skills[counter])
    counter+=1

skill1 = input("Choose a skill from above by entering its number: ")
if skill1.isdigit():
    cv['skills'].append(skills[int(skill1)-1])
else:
    skill1 = input("not a number try again: ")

skill2 = input("Choose another skill from above by entering its number: ")
if skill2.isdigit():
    cv['skills'].append(skills[int(skill2)-1])
else:
    skill2 = input("not a number try again: ")

# if skill1 == 1:
#     cv["First skill"] = skill[0]
# elif skill1 == 2:
#     cv["First skill"] = skill[1]
# elif skill1 == 3:
#     cv["First skill"] = skill[2]   
# elif skill1 == 4:
#     cv["First skill"] = skill[3]
# else: print ("false")

# if skill2 == 1:
#     cv["Second skill"] = skill[0]
# elif skill2 == 2:
#     cv["Second skill"] = skill[1]
# elif skill2 == 3:
#     cv["Second skill"] = skill[2]   
# elif skill2 == 4:
#     cv["Second skill"] = skill[3]
# else: print ("false")

print(cv)

if int(age) >=25 and int(age) <40 and int(experience) >3 and skills  == Football:
    print ("Congrats")
else:
    print ("Sorry you are not good enough")