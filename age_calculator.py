from datetime import datetime
year = int(input("Enter Year of Birth: "))
month = int(input("Enter Month of Birth: "))
day = int(input("Enter Day of Birth: "))
def check_birthdate (year, month, day):
    today = datetime(2020,1,26)
    birthdate = datetime(year, month, day)
    if today > birthdate:
        return True
    return False

# print (check_birthdate(1995,1,29))
# print (check_birthdate(2995,1,29))
# year = input("Enter Year of Birth: ")
# month = input("Enter Month of Birth: ")
# day = input("Enter Day of Birth: ")


def calculate_age (year,month,day):
    today = datetime(2020,1,26)
    birthdate = datetime(year, month, day)
    calculate = int((today-birthdate).days / 365)
    print ("You are %s years old" % (calculate))

if check_birthdate (year, month, day) == True:
    print(calculate_age (year, month, day))
else:
    print("Invalid birthdate")
