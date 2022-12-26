import os


def CreateRuns(A, B, sourceFile, S):

    currFile = A
    file = open(sourceFile, "r")
    array = []
    value = ''
    while True:
        data = file.read(1)
        if not data:
            if value:
                array.append(int(value))
            array.sort()
            array = list(map(str, array))
            with open(currFile, "a+") as f:
                f.write(" ".join(array))
            break
        else:
            if (data != ' '):
                value += data
            else:
                if (S != len(array)):
                    array.append(int(value))
                    value = ''
                elif (S == len(array)):
                    print(array)
                    array.sort()
                    array = list(map(str, array))
                    with open(currFile, "a+") as f:
                        f.write(" ".join(array))
                    if currFile == A:
                        currFile = B
                    else:
                        currFile = A
                    array = []
                    array.append(int(value))
                    value = ''
    f.close()


def PolyPhaseMerge(A, B, C, D, S):

    in1 = A
    in2 = B
    currOutput = C
    size = S

    with open(currOutput, 'wb'):  # Очистка CurrentOutput файла
        pass

    while ((os.stat(in1)).st_size != 0 and (
    os.stat(in2)).st_size != 0):
        f1 = open(in1, "r")
        f2 = open(in2, "r")
        data1 = f1.read(size)
        data2 = f2.read(size)
        readFlag = 1

        while (data1 or data2):
            if readFlag == 0:
                data1 = f1.read(size)
                data2 = f2.read(size)

            data1 = data1.split()
            data1 = list(map(int, data1))
            data2 = data2.split()
            data2 = list(map(int, data2))

            data = Merge(data1, data2)
            data = list(map(str, data))
            readFlag = 0

            with open(currOutput, "a+") as file:
                file.write(" ".join(data) + " ")
            if (currOutput == A):
                currOutput = B
            elif (currOutput == B):
                currOutput = A
            elif (currOutput == C):
                currOutput = D
            else:
                currOutput = C

        f1.close()
        f2.close()
        with open(in1, 'wb'):
            pass
        with open(in2, 'wb'):
            pass

        size *= 2
        if (in1 == A):
            in1 = C
            in1 = D
            currOutput = A
        else:
            in1 = A
            in2 = B
            currOutput = C


def Merge(A, B):
    A = A + B
    A.sort()
    return A


A = 'A.txt'
B = 'B.txt'
C = 'C.txt'
D = 'D.txt'
S = 20
CreateRuns(A, B, C, S)
PolyPhaseMerge(A, B, C, D, S)
