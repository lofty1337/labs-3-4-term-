str = input('Введите строку: ')
list=[]
wrongStr = 0
for i in str:
    if i == '(' or i == '{' or i == '[':
        list.append(i)
    else:
        if list == []:
            print('Последовательность неверна')
            wrongStr = 1
            break
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
        print('Последовательность верна')
    else:
        print('Последовательность неверна')
