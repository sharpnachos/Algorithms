rankedbadwords = []

def main():
    f = open("bad.txt","r")
    f1 = f.read()
    global rankedbadwords
    badwords = []
    temp = ''
    count = 0
    for letter in f1:
        if letter != ' ':
            temp = temp + letter
        else:
            if temp in badwords:
                for item in rankedbadwords:
                    if item[0] == temp:
                        item[1] = item[1] + 1
            else:
                rankedbadwords.append([temp, 1])
                badwords.append(temp)
            temp = ''
    f.close()
    f = open("badwords.txt","w")
    rankedbadwords.sort(key = lambda x: x[1])
    temp = ''
    for item in rankedbadwords:
        temp = item[0]
        f.write(temp + " " + str(item[1]) + "\n")
    print("Done!")

main()
