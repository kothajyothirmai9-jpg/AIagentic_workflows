def rule_based_agent(temp):
    if temp > 100:
        return "Cool"
    else:
        return "Idle"


# 3 iterations
temperatures = [120, 95, 110]

for i in range(3):
    action = rule_based_agent(temperatures[i])
    print("Iteration", i + 1, ": Temperature =", temperatures[i], "->", action)