def run_agent():
    state = {
        "step": 0,
        "items": 8
    }

    while state["step"] < 3:
        print("Step:", state["step"])
        print("Items:", state["items"])

        state["items"] += 1
        state["step"] += 1   # Fix: missing increment

    return state


result = run_agent()
print("Final State:", result)