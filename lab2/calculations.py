LIMIT = 100


def next_state(x, i, a, b):
    value = 2 * x + b
    if value > LIMIT:
        return LIMIT
    return value


def state_iterative(n, a, b):
    x = a

    for i in range(1, n + 1):
        x = next_state(x, i, a, b)

    return x


def state_recursive(n, a, b):
    if n == 0:
        return a

    x = state_recursive(n - 1, a, b)
    return next_state(x, n, a, b)
