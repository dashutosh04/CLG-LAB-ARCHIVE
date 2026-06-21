import math


def sqrt(num):
    return math.sqrt(num)


def cos(num):
    return math.cos(num)


def sin(num):
    return math.sin(num)


def tan(num):
    return math.tan(num)


def cot(num):
    return 1 / math.tan(num)


def sec(num):
    return 1 / math.cos(num)


def cosec(num):
    return 1 / math.sin(num)


def log(base, num):
    return math.log(num, base)


def additon(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def exponent(num1, num2):
    return num1**num2


def main():
    print("===============Calculator===============")

    while True:
        expression_raw = str(input("Enter the expression. "))

        if "+" in expression_raw:
            num1, num2 = expression_raw.split("+")
            print("Addition - ", additon(float(num1), float(num2)))

        elif "-" in expression_raw:
            num1, num2 = expression_raw.split("-")
            print("Subtraction - ", subtraction(float(num1), float(num2)))

        elif "*" in expression_raw:
            num1, num2 = expression_raw.split("*")
            print("Multiplication - ", multiplication(float(num1), float(num2)))

        elif "/" in expression_raw:
            num1, num2 = expression_raw.split("/")
            print("Division - ", divide(float(num1), float(num2)))

        elif "^" in expression_raw:
            num1, num2 = expression_raw.split("^")
            print("Exponent - ", exponent(float(num1), float(num2)))

        elif "sqrt" in expression_raw:
            parts = expression_raw.split("sqrt")
            print("Square Root - ", sqrt(float(parts[1])))

        elif "cos" in expression_raw:
            parts = expression_raw.split("cos")
            print("Cosine - ", round(cos((math.pi / 180) * float(parts[1])), 5))

        elif "sin" in expression_raw:
            parts = expression_raw.split("sin")
            print("Sine - ", round(sin((math.pi / 180) * float(parts[1])), 5))
        elif "tan" in expression_raw:
            parts = expression_raw.split("tan")
            print("Tangent - ", round(tan((math.pi / 180) * float(parts[1])), 5))

        elif "cot" in expression_raw:
            parts = expression_raw.split("cot")
            print("Cotangent - ", round(cot((math.pi / 180) * float(parts[1])), 5))

        elif "cosec" in expression_raw:
            parts = expression_raw.split("cosec")
            print("Cosecant - ", round(cosec((math.pi / 180) * float(parts[1])), 5))

        elif "sec" in expression_raw:
            parts = expression_raw.split("sec")
            print("Secant - ", round(sec((math.pi / 180) * float(parts[1])), 5))

        elif "log" in expression_raw:
            parts = expression_raw.split("log")
            base = 10
            num = float(parts[1])

            print("log - ", round(log(base, num), 5))

        elif "ln" in expression_raw:
            parts = expression_raw.split("ln")
            base = math.e
            num = float(parts[1])

            print("log - ", round(log(base, num), 5))

        elif expression_raw.lower() == "exit":
            print("Exiting............")
            break


if __name__ == "__main__":

    main()
