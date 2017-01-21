from datetime import datetime

d1 = datetime.strptime("2015-08-10 19:33:27", "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime("2015-08-10 19:33:28", "%Y-%m-%d %H:%M:%S")

print(d2 - d1)
