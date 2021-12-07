depths = [int(line.strip()) for line in open('input.txt')]

prev = depths[0]
total = 0 
for d in depths:
    if d > prev:
        total += 1
    prev = d
print(total)