lines = ''

with open('/Users/valentinhuber/Documents/Studium/Semester-5/Network Security/HW1/2.4/shakespeare.txt', 'r') as f:
    lines = bytes(''.join(f.readlines()), 'ascii')


counts = dict.fromkeys(range(256), 0)
for e in lines:
    counts[e] += 1

counts = {k: v/len(lines) for k, v in counts.items()}

print(counts)
