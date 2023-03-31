import statistics

tocke= [5,6,7,9,4,3,1,2,6,1]

print('Aritmetička sredina 10 brojeva', tocke)
statistics.mean(tocke)

m= statistics.mean(tocke)

print('standardna devijacija:', (statistics.stdev(tocke)))