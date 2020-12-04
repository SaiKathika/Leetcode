def canCompleteCircuit(gas, cost):
    if (sum(gas) - sum(cost) < 0):
        return -1
    
    gas_tank, start_idx = 0, 0

    for i in range(len(gas)):
        gas_tank += gas[i] - cost[i]
        #print(gas_tank)
        if gas_tank < 0:
            start_idx = i + 1
            gas_tank = 0

    return start_idx

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))