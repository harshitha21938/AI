def water_jug(jug1_capacity, jug2_capacity, target):
    jug1, jug2 = 0, 0 
    steps = [] 
    while jug1 != target and jug2 != target:
        if jug1 == 0:
            jug1 = jug1_capacity
            steps.append(f"Fill Jug1: ({jug1}, {jug2})")
        # If jug2 is full, empty it
        elif jug2 == jug2_capacity:
            jug2 = 0
            steps.append(f"Empty Jug2: ({jug1}, {jug2})")
        else:
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
            steps.append(f"Transfer Jug1 to Jug2: ({jug1}, {jug2})")
        if jug1 == target or jug2 == target:
            break
    steps.append(f"Target reached: ({jug1}, {jug2})")
    return steps
jug1_capacity = 4 
jug2_capacity = 3  
target = 2       
solution = water_jug(jug1_capacity, jug2_capacity, target)
for step in solution:
    print(step)