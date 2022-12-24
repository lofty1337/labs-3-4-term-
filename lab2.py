def op_prior(o):
    if o == '*':
        return 2
    elif o == '/':
        return 2
    elif o == '+':
        return 1
    elif o == '-':
        return 1
    elif o == '(':
        return 0


def rpn(s):
    lex = parse(s)
    s2 = []
    r = []
    oper = ["+", "-", "*", "/", "(", ")"]
    for a in lex:
        if a == "(":
            s2 = [a] + s2
        elif a in oper:
            if s2 == []:
                s2 = [a]
            elif a == ")":
                while (True):
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    r += [q]
            elif op_prior(s2[0]) < op_prior(a):
                s2 = [a] + s2
            else:
                while (True):
                    if s2 == []:
                        break
                    q = s2[0]
                    if op_prior(q) < op_prior(a):
                        break
                    r += [q]
                    s2 = s2[1:]
                s2 = [a] + s2
        else:
            r += [a]
    while (s2 != []):
        q = s2[0]
        r += [q]
        s2 = s2[1:]
    print(r)
    return r


def parse(s):
    delims = ["+", "-", "*", "/", "(", ")"]
    lex = []
    tmp = ""
    for a in s:
        if a != " ":
            if a in delims:
                if tmp != "":
                    lex += [tmp]
                lex += [a]
                tmp = ""
            else:
                tmp += a
    if tmp != "":
        lex += [tmp]
    return lex


def calc(formula):
    s = []
    for lex in formula:
        if lex[0].isdigit():
            s.append(float(lex))
        else:
            a2 = s.pop()
            a1 = s.pop()
            if lex == '+':
                s.append(a1 + a2)
            if lex == '-':
                s.append(a1 - a2)
            if lex == '*':
                s.append(a1 * a2)
            if lex == '/':
                if a2 == 0:
                    raise RuntimeError('/0!')
                else:
                    s.append(a1 / a2)
    return s.pop()


def bracket_check(s):
    str=''
    for i in s:
        if i=='(' or i==')':
            str+=i
    list = []
    wrongStr = 0
    for i in str:
        if i == '(' or i == '{' or i == '[':
            list.append(i)
        else:
            if list == []:
                return 0
            else:
                if i == ']':
                    if list[-1] == '[':
                        list.pop()
                elif i == ')':
                    if list[-1] == '(':
                        list.pop()
                elif i == '}':
                    if list[-1] == '{':
                        list.pop()
    if wrongStr == 0:
        if list == []:
            return 1
        else:
            return 0
expression = input()
if bracket_check(expression):
    print(calc(rpn(expression)))
else:
    print("Неверная скобочная последовательность")
