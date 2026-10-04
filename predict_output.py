def agent():
    state = {
        "step": 0,
        "items": 5
    }

    while state["step"] < 2:
        state["items"] += 1
        state["step"] += 1

    return state


result = agent()
print(result)