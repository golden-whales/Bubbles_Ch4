scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
.33, .31, .25, .29, .27, .22,
.31, .25, .25, .33, .21, .25,
.25, .25, .28, .25, .24, .22,
.20, .25, .30, .25, .24, .25,
.25, .25, .27, .25, .26, .29]

high_score = 0
best_solutions = [] #[11, 18]

length_scores = len(scores)
for i in range(length_scores):
    print('Bubble solution #' + str(i), 'scores:', scores[i], 'bubbles')
    if scores[i] > high_score:
        high_score = scores[i]
print('Bubbles tests:', length_scores)
print('Highest bubble score:', high_score)


for i in range(length_scores):
    if scores[i] == high_score:
        best_solutions.append(i)
print('Tests with highest bubble score:', best_solutions)

cost = 100.0
most_effective = 0

for i in range(len(best_solutions)):
    index = best_solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]
print('Solution', most_effective, 'is the most efftive with a cost of', costs[most_effective])

#lowest_cost = 100 

#for k in range(len(best_solutions)):      #k is index of best_solutions
  #  i = best_solutions[k]
    #if costs[i] < lowest_cost:
    #    lowest_cost = costs[i]
      #  print('Most effective solution is:', i, 'with a cost of', costs[i])


#lowest_cost = 100 #cost
#cheapest_solution = 0 #most_effective
        
#for i in range(length_scores):
   # if scores[i] == high_score and costs[i] < lowest_cost:
       # cheapest_solution = i
       # lowest_cost = costs[i]
        
#print('Most effective solution is solution', cheapest_solution)




