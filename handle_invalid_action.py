def goal_based_agent(state, goal, action, log):
    max_items = 10

    # Handle invalid action
    valid_actions = ["add", "check"]

    if action not in valid_actions:
        error = {
            "status": "error",
            "error": "Invalid action",
            "action": action
        }
        log.append(error)
        return error, log

    # Add item action
    if action == "add":
        if state["items"] >= max_items:
            state["done"] = True
            result = {
                "status": "error",
                "error": "Maximum items exceeded"
            }
        else:
            state["items"] += 1
            state["step"] += 1
            result = {
                "status": "success",
                "result": "Item added"
            }

    # Check goal action
    elif action == "check":
        if state["items"] == goal:
            state["done"] = True
            result = {
                "status": "success",
                "result": "Goal reached"
            }
        else:
            result = {
                "status": "continue",
                "result": "Goal not reached"
            }

    log.append(result)
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
actions = ["add", "wrong_action", "check"]

for action in actions:
    result, log = goal_based_agent(state, goal, action, log)
    print(result)

print("\nFull Log:")
for entry in log:
    print(entry)