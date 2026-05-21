sequence=[1,2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value