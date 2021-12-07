depths = [int(line.strip()) for line in open('input.txt')]
windowed_depths = [sum([depths[i], depths[i+1], depths[i+2]]) for i in range(0, len(depths) - 2)]

prev = windowed_depths[0]
total = 0 
for d in windowed_depths:
    if d > prev:
        total += 1
    prev = d
print(total)