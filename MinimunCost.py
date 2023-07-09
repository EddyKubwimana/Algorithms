def minimunCost(N, start, End, cost):
    right_cost =0
    for i in range(start-1,End-1):
        right_cost +=  cost[i]





    return right_cost

N = 4
start = 1
finish = 1
ticket_cost = [1, 2, 2, 4 ]
print(ticket_cost[:1]+ticket_cost[1:][::-1])

print(minimunCost(N,start,finish,ticket_cost))

            



