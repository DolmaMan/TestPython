funcSum = lambda x, y: str(int(x) + int(y))
funcSub = lambda x, y: str(int(x) - int(y))
funcMul = lambda x, y: str(int(x) * int(y))
funcDiv = lambda x, y: str(int(x) / int(y))


def Log(message: str):
    logFile = open("log.log", "a", encoding="UTF-8")
    logFile.write(message + "\n")
    logFile.close()


print("Добро пожаловать в калькулятор")
while True:
    answer = input("Введите ваше выражение: ")
    answer = answer.split(' ')

    if len(answer) == 0:
        ans = input("Вы хотите выйти из программы?(д/н)").lower()
        if ans == "l" or ans == "д" or ans == "y":
            break
        else:
            continue
    try:
        if(answer[1] == "+"):
            msg = answer[0] + ' + ' + answer[2] + ' = ' + funcSum(answer[0], answer[2])
        elif (answer[1] == "-"):
            msg = answer[0] + ' - ' + answer[2] + ' = ' + funcSub(answer[0], answer[2])
        elif (answer[1] == "*"):
            msg = answer[0] + ' * ' + answer[2] + ' = ' + funcMul(answer[0], answer[2])
        elif (answer[1] == "/"):
            msg = answer[0] + ' / ' + answer[2] + ' = ' + funcDiv(answer[0], answer[2])
        else:
            msg = "Ошибка ввода. Выражение: " + " ".join(answer)
    except:
        msg = "Ошибка ввода: необходимо вводить числа и знаки через пробел Выражение: " + " ".join(answer)

    print(msg)
    Log(msg)