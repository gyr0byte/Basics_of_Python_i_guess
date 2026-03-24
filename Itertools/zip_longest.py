import itertools

counter = itertools.count() # to make counter start from 5 do .count(start=5) to step .count(start=5, step=5)

data = [100, 200, 300, 400, 500]

daily_data = list(zip(itertools.count(), data))

print(daily_data)
