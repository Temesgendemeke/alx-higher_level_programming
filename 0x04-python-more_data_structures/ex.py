
n = {"tt":6,"44":55,"ken":99}

best_v = None
best_c = 0

for key, value in n.items():
    if value > best_c:
        best_v = key
        best_c = value

print(best_v)
