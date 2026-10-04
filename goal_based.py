def goal_based_agent(temp, goal):
    if temp > goal:
        return "Cool"
    elif temp < goal:
        return "Heat"
    else:
        return "Goal Reached"


# 3 iterations
temperatures = [120, 90, 100]
goal = 100

for i in range(3):
    action = goal_based_agent(temperatures[i], goal)
    print("Iteration", i + 1, ": Temperature =", temperatures[i], "->", action)