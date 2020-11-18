prompt = """Howdy this program is utilized to go through a calendar month and dates.\n
It will also show classes that have been completed. This program is gives all courses taken and\n
courses left to take. 
"""
prompt += "\n Enter your full name. "
name = input(prompt)
print (f"\n Hello, {name}!")


import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m,))
import datetime

from datetime import datetime
print("The current date and time is -->\t", datetime.now())

print("""   __  ___    _     __                         ____            __                                
   /  |/  /   (_)   / /  ___    _____          / __ \  ____    / /_   ____    ____   ___    __  __
  / /|_/ /   / /   / /  / _ \  / ___/         / / / / / __ \  / __ \ / __ \  / __ \ / _ \  / / / /
 / /  / /   / /   / /  /  __/ (__  )         / /_/ / / /_/ / / / / // /_/ / / / / //  __/ / /_/ / 
/_/  /_/   /_/   /_/   \___/ /____/         /_____/  \____/ /_/ /_/ \____/ /_/ /_/ \___/  \__, /  
                                                                                         /____/   """)


print("""
    ____        _    __                           __  __            _                                  _    __          
   / __ \  ___ | |  / /   _____   __  __         / / / /   ____    (_) _   __  ___    _____   _____   (_)  / /_   __  __
  / / / / / _ \| | / /   / ___/  / / / /        / / / /   / __ \  / / | | / / / _ \  / ___/  / ___/  / /  / __/  / / / /
 / /_/ / /  __/| |/ /   / /     / /_/ /        / /_/ /   / / / / / /  | |/ / /  __/ / /     (__  )  / /  / /_   / /_/ / 
/_____/  \___/ |___/   /_/      \__, /         \____/   /_/ /_/ /_/   |___/  \___/ /_/     /____/  /_/   \__/   \__, /  
                               /____/                                                                          /____/ 

""")

print("""
   _____                  _                
  / ___/  ___    ____    (_)  ____    _____
  \__ \  / _ \  / __ \  / /  / __ \  / ___/
 ___/ / /  __/ / / / / / /  / /_/ / / /    
/____/  \___/ /_/ /_/ /_/   \____/ /_/     
                                           
""")
print("""
 
   ___    ____    ___    ____ 
  |__ \  / __ \  |__ \  / __ |
  __/ / / / / /  __/ / / / / /
 / __/ / /_/ /  / __/ / /_/ / 
/____/ \____/  /____/ \____/                         

""")                                               

first_name = "Miles"
last_name = "Dohoney"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print()
print("-" * 100)
print("*" * 100)
print()
print(message)
print()

import datetime
graduation = datetime.datetime(2020, 12, 19) 
now = datetime.datetime.now()
x = graduation - now
print("You are now a senior and graduate in!", x)
print()
print("*" * 100)
print("-" * 100)
print()
print()

#course_left_july = ['July you are taking the following', 'BUSN-412-0 Business Policy', 'SEC-340-0 Business Continuity']
#cousrse_left_september = ['September you are taking the following', 'LAS-432-3 Tech, Society, and Culture', 'BUSN-460-6 Senior Project']
course_left_november = ['November you are taking the following', 'CARD-405-0 Career Development', 'SEC-360-3 Data Privacy and Security']

print()
print("You have the following course's left to take until graduation.")
print()
print("-" * 120)
#print(course_left_july)
#print(cousrse_left_september)
print(course_left_november)
print("-" * 120)

print()
print("*" * 120)
courses_taken = ['July 2019, COLL-148-0 Critical Thinkng & Prob-Solvng:', 'September 2019, SOCS-185-0 Culture and Society, BUSN-115-8 Intro to Business & Technology', 'November 2019, MATH-221-0 Statistics for Decision-Making', 'March 2020, MGMT-303-0 Principles of Management, ENGL-135-3 Advanced Composition', 'May 2020, SEC-310-0 Princpls & Theory of Sec Mgmt, MGMT-404-0 Project Management', 'BUSN-412 Business Policy, SEC-340 Business Continuity']

for courses_taken in courses_taken:
    print(f"Completed: {courses_taken}.")

print("\nThese courses have been completed!")
print()
print("*" * 120)
print()
print("\n")

#print("\n")
#import datetime
#july_term = datetime.datetime(2020, 8, 29) 
#now = datetime.datetime.now()
#x = july_term - now
#print("Senior keep up the tremendous work!\n Knock this term out of the park!\n Your July 2020 session is over in!\n", x)
#print()
#print("*" * 100)
#print("-" * 100)
#print()
#print()

print("\n")
import datetime
september_term = datetime.datetime(2020, 10, 24) 
now = datetime.datetime.now()
x = september_term - now
print("Senior keep up the outstanding work!\n You are so close to finishing!\n Your September 2020 session is over in!\n", x)
print()
print("*" * 100)
print("-" * 100)
print()
print()

print("\n")
import datetime
november_term = datetime.datetime(2020, 12, 19) 
now = datetime.datetime.now()
x = november_term - now
print("Senior keep up the phenomenal work!\n You are so close to finishing!\n This is your last semester, so give it all you got!\n Your November 2020 session is over in!\n", x)
print()
print("*" * 100)
print("-" * 100)
print()
print()

#print()
#print("^" * 100)
#import this
#print(this)
#print()
#print("^" * 100)
#print()
#MILES
# print()




