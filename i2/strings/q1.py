# 1 min

string1 = input()
string2 = input()


for i in range(len(string1)):
    if string1[i] == string2[i]:
        print(string1[i], end="")
