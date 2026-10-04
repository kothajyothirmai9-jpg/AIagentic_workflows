def goal_based_agent(state, goal):
    max_items = 10

    # Failure condition
    if state["items"] > max_items:
        state["done"] = True
        return "Failure"

    # Success condition
    if state["items"] == goal:
        state["done"] = True
        return "Success"

    # Continue toward goal
    state["items"] += 1
    state["step"] += 1
    return "Continue"


# Initial state
state = {
    "items": 8,
    "done": False,
    "step": 0
}

goal = 10

# 3 iterations
for i in range(3):
    result = goal_based_agent(state, goal)

    print("Iteration:", i + 1)
    print("State:", state)
    print("Result:", result)
    print()