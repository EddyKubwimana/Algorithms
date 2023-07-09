def minimunCost(N, start, End, cost):
    # right cost
    Newcost = [cost[start-1]]+cost[:start-1]+cost[start:][::-1]
    print(Newcost)
    total_right = 0 
    total_left = 0
    if start<= End:
        for i in range(start-1, End-1):
            total_right += cost[i]

       
    if start>End:
        start = 0
        for i in range(start, End):
            total_right+= Newcost[i]

    if  start <= End and End-len(cost)>=0 and start==0:
         for i in range(End-1, start-1, -1):
            total_left+= cost[i]


    if start <=End:
        End = End-start
        start =0
        
        for i in range(start, End):
            total_left += Newcost[i]
            print(total_left)






    return total_right, total_left


    
N = 4
start = 4
finish = 1
ticket_cost = [1, 2, 2, 4 ]

print(minimunCost(N,start,finish,ticket_cost))

            



