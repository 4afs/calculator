with open('formula.txt', encoding='utf8')as f:
    formula = f.read().rstrip()

def parser(formula):
    for num in range(len(formula)):
        if formula[num] == '/':
            print(formula[:num], formula[num + 1:])
            return division(formula[:num], parser(formula[num + 1:]))

        elif formula[num] == '*':
            print(formula[:num], formula[num + 1:])
            return multiplication(formula[:num], parser(formula[num + 1:]))

        elif formula[num] == '-':
            print(formula[:num], formula[num + 1:])
            return subtract(formula[:num], parser(formula[num + 1:]))

        elif formula[num] == '+':
            print(formula[:num], formula[num + 1:])
            return addition(formula[:num], parser(formula[num + 1:]))

        elif num == len(formula) - 1:
            print(formula)
            return addition(formula, 0)

def addition(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiplication (a, b):
    return float(a) * float(b)

def division(a, b):
    return float(a) / float(b)

print('{0}'.format(parser(formula)))
