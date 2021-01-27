#!/usr/bin/env python3

rolls = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]

sevens = [(d1, d2) for (d1, d2) in rolls if d1 + d2 == 7]

prob7 = len(sevens) / len(rolls)

rolls_by_sum = [ [(d1, d2) for (d1, d2) in rolls if d1 + d2 == s] for s in range(2, 13) ]

prob_by_sum = [ (k, len(rolls_by_sum[k - 2]) / len(rolls)) for k in range(2, 13) ]

for (k, prob) in prob_by_sum:
   print('{0:2d}: {1:8.2f}%'.format(k, 100*prob))
