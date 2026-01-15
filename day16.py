# --- Day 16: 30 Days of python programming ---
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
# print(now)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formated_now_1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(formated_now_1)

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)

# 4. Calculate the time difference between now and new year.
new_year = datetime.strptime("1 January, 2027", "%d %B, %Y")
time_difference = new_year - now
# print(time_difference)

# 5. Calculate the time difference between 1 January 1970 and now.
past_date = datetime.strptime("1 January, 1970", "%d %B, %Y")
new_time_difference = now.year - past_date.year

# print(new_time_difference)

# Think, what can you use the datetime module for?
"""
- Social media: see the time when something was posted
- E-mail service: see when the e-mail was sent,opend... 
"""