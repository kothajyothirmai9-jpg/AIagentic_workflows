def goal_based_agent(items, goal):
    max_items = 10

    if items > max_items:
        return "Failure"
    elif items < goal:
        return "Add Items"
    elif items == goal:
        return "Goal Reached"
    else:
        return "Remove Items"


# 3 iterations
items_list = [5, 10, 12]
goal = 10

for i in range(3):
    action = goal_based_agent(items_list[i], goal)
    print("Iteration", i + 1, ": Items =", items_list[i], "->", action)