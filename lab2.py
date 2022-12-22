import re
# Приоритет операций-символов
expressions=['+','-','*','/']
def op_prior(o):
    if o == '*':
        return 3
    elif o == '/':
        return 2
    elif o == '+':
        return 1
    elif o == '-':
        return 1


def opn(expr):  # входной параметр -инфиксная строка арифметического выражения
    co = []  # выходная строка
    op_steck = []  # стек операторов
    list_tokens = expr
    print(list_tokens)
    for i in list_tokens:  # цикл по списку- i елемент число,() или знак операции
        if i.isdigit():  # i-число
            co.append(int(i))  # в стек
        elif i in ['*', '/', '%', '+', '-']:  # i -бинарная операция
            token_tmp = ''  # смотрим на вверх стека
            if len(op_steck) > 0:
                token_tmp = op_steck[len(op_steck) - 1]  # смотрим на вверх стека
                while (len(op_steck) > 0 and token_tmp != '('):  # пока стек >0
                    if (op_prior(i) <= op_prior(token_tmp)):  # сравнием приоритет токена в строке и приоритет операци  в стеке операций
                        co.append(op_steck.pop())  # если в стеке операция выше,то выталкиваем его в выходную строку
                    else:  # bиначе выходим из данного цикла
                        break
            op_steck.append(i)  # тогда выйдя из цикла,добавим операцию в стек
        elif i == '(':  # открывающая (
            op_steck.append(i)  # в стек
        elif i == ')':  # закрывающая )
            token_tmp = op_steck[len(op_steck) - 1]  # смотрим на вверх стека
            while (token_tmp != '('):  # пока не всретим открывающию скобку
                co.append(
                    op_steck.pop())  # выталкиваем операторы в выходную строку-раз мы работаем с группированием чисел-со скобками
                token_tmp = op_steck[len(op_steck) - 1]  # смотрим на вверх стека внутри цикла
                if len(op_steck) == 0:
                    raise RuntimeError('V virajenii propushena (')
                if token_tmp == '(':
                    op_steck.pop()

    while (len(op_steck) > 0):  # мы должны вытолкнуть оставшиеся операторы
        token_tmp = op_steck[len(op_steck) - 1]
        co.append(op_steck.pop())
        if token_tmp == '(':
            raise RuntimeError('V virajenii propushena )')
    return co  # вернем постфиксную запись

res=1
expr = input()
co = opn(expr)
i=0
while len(co)>1:
    tmp = co
    if co[i] in expressions:
        if co[i]=='+':
            res = co[i-2] + co[i-1]
        elif co[i]=='-':
            res = co[i-2] - co[i-1]
        elif co[i] == '*':
            res = co[i - 2] * co[i - 1]
        elif co[i] == '/':
            if co[i - 1]!=0:
                res = co[i - 2] / co[i - 1]
            else:
                raise RuntimeError('/0!')
        co = co[0:i-2]
        co.append(res)
        co.extend(tmp[i+1:])
        i=0
    else:
        i+=1
print(co) #2+7*(3/9)-5
