import math


def sin(deg):
    return math.sin(math.radians(deg))


def cos(deg):
    return math.cos(math.radians(deg))


def tan(deg):
    return math.tan(math.radians(deg))


def cot(deg):
    return 1 / math.tan(math.radians(deg))


def sec(deg):
    return 1 / math.cos(math.radians(deg))


def csc(deg):
    return 1 / math.sin(math.radians(deg))


def cosec(deg):
    return 1 / math.sin(math.radians(deg))


def asin(x):
    return math.degrees(math.asin(x))


def acos(x):
    return math.degrees(math.acos(x))


def atan(x):
    return math.degrees(math.atan(x))


operation_dict = {
    "pi": math.pi,
    "e": math.e,
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "ln": math.log,
    "exp": math.exp,
    "abs": abs,
    "round": round,
    "fact": math.factorial,
    "gamma": math.gamma,
    "sin": lambda deg: math.sin(math.radians(deg)),
    "cos": cos,
    "tan": tan,
    "cot": cot,
    "sec": sec,
    "csc": csc,
    "cosec": cosec,
    "asin": asin,
    "acos": acos,
    "atan": atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
}


def expression_solver(expr):
    try:
        expr = expr.replace("^", "**")
        expr = expr.replace("%", "/100")

        result = eval(expr, {}, operation_dict)
        return result
    except Exception as e:
        return f"Error: {e}"


def main():
    print("============ Scientific Calculator ============ ")
    print("Type 'exit', 'quit', or 'q' to exit")
    print("===============================================")

    while True:
        expr = input("\nExpression you want to solve: ").strip()

        if expr.lower() in ["exit", "quit", "q"]:
            print("Exiting....")
            break

        if not expr:
            continue

        result = expression_solver(expr)

        print(f"Ans: {result}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting....")
