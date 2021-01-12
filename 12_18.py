def evaluate(expr):
    expr = expr.strip()
    stack = []
    cval = None
    expr = expr.replace("(", "( ").replace(")", " )")
    tokens = expr.split()
    operator = None
    for token in tokens:
        if token.isdigit():
            if cval is None:
                cval = int(token)
                continue
            if operator == "*":
                cval *= int(token)
            else:
                cval += int(token)
        elif token == "(":
            stack.append((cval, operator))
            cval = None
        elif token == ")":
            nc, nop = stack.pop()
            if nop == "*":
                cval = (nc if nc is not None else 1) * cval
            else:
                cval = (nc if nc is not None else 0) + cval

        else:
            operator = token

    return cval


def day18_1():
    exprs = [x for x in open("num18.txt").read().split("\n") if x]
    return sum(evaluate(x) for x in exprs)


def evaluate2(expr):  # shunting-yard algorithm http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
    ops = {"*": lambda x, y: int(x) * int(y), "+": lambda x, y: int(x) + int(y)}
    prec = {"+": 1, "*": 0}
    expr = expr.strip()
    stack = []
    output = []
    expr = expr.replace("(", "( ").replace(")", " )")
    tokens = expr.split()
    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top = stack[-1] if stack else None
            while top is not None and top != '(':
                operator = stack.pop()
                right = output.pop()
                left = output.pop()
                output.append(ops[operator](left, right))

                top = stack[-1] if stack else None

            stack.pop()
        else:
            top = stack[-1] if stack else None
            while top is not None and top not in "()" and prec.get(top) > prec.get(token):
                operator = stack.pop()
                right = output.pop()
                left = output.pop()
                output.append(ops[operator](left, right))

                top = stack[-1] if stack else None
            stack.append(token)
    while stack:
        operator = stack.pop()
        right = output.pop()
        left = output.pop()
        output.append(ops[operator](left, right))

    return output[0]


def day18_2():
    exprs = [x for x in open("num18.txt").read().split("\n") if x]
    return sum(evaluate2(x) for x in exprs)


print(day18_1())
print(day18_2())
