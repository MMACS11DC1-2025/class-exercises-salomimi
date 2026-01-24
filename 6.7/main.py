# selection sort

import time 

scores = [39, 2, 103, 42, 50, 61]

for i in range(len(scores)):
    smallest_score = scores[i]
    smallest_index = i

    for j in range(i+1, len(scores)):
        if scores[j] < smallest_score:
            smallest_score = scores[j]
            smallest_index = j
    
    scores[smallest_index], scores[i] = scores[i],
        scores[smallest_index]

print(scores)

