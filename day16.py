# --- Day 16: 30 Days of python programming ---
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
# print(now)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formated_now_1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated_now_1)