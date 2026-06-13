from datetime import datetime

now = datetime.now()
# day = now.day
# date = now.date()
# current_timestamp = now.timestamp()
# print(current_timestamp)
# print(day)
# print(date)



# date = now.strftime('%d/%m/%y')#or
date = now.strftime('%D')
print(date)

time = now.strftime(f'{"%I"} vajun {"%M"} minute zale aahe.. how funny')
print(time)


