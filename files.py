fileFrom = open("ДЗ.txt", "r")
fileTo = open("path", "w")

line = fileFrom.readline()
countLines = 1
while line != "":
    fileTo.write(str(countLines) + " - " + line)
    line = fileFrom.readline()
    countLines += 1

fileFrom.close()
fileTo.close()