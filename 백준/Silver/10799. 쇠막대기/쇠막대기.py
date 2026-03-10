def solve(state):
    n = len(state)
    current_bars = 0
    result = 0
    idx = 0

    while idx <= n-1:
        if state[idx] == '(':
            if state[idx+1] == ')':
                result += current_bars
                idx += 1
            elif state[idx+1] == '(':
                current_bars += 1
        elif state[idx] == ')':
            current_bars -= 1
            result += 1
        idx += 1

    return result

state = input()

result = solve(state)

print(result)