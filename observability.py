def goal_based_agent(state, goal, log):
    max_items = 10

    # Failure condition
    if state["items"] > max_items:
        state["done"] = True
        result = "Failure"

    # Success condition
    elif state["items"] == goal:
        state["done"] = True
        result = "Success"

    # Continue toward goal
    else:
        state["items"] += 1
        state["step"] += 1
        result = "Continue"

    # Log every step
    log.append({
        "step": state["step"],
        "items": state["items"],
        "done": state["done"],
        "result": result
    })

    return result, log


# Initial state
state = {
    "items": 8,
    "done": False,
    "step": 0
}

goal = 10
log = []

# 3 iterations
for i in range(3):
    result, log = goal_based_agent(state, goal, log)

# Return full log
print("Full Log:")
for entry in log:
    print(entry)