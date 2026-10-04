def goal_based_agent(state, goal):
    max_items = 10

    if state["items"] > max_items:
        state["done"] = True
        return "Failure"

    elif state["items"] == goal:
        state["done"] = True
        return "Goal Reached"

    else:
        state["step"] += 1
        return "Add Items"


# Initial state
state = {
    "items": 5,
    "done": False,
    "step": 0
}

goal = 10

# 3 iterations
for i in range(3):
    action = goal_based_agent(state, goal)

    print("Iteration:", i + 1)
    print("State:", state)
    print("Action:", action)
    print()