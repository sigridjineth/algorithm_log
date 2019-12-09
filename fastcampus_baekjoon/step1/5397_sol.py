test_case = int(input())
for _ in range(test_case):
    temp = []
    password = []
    inputpword = list(input())
    for i in range(len(inputpword)):
        if inputpword[i] == "<":
            if password:
                temp.append(password.pop())
        elif inputpword[i] == "-":
            if password:
                password.pop()
        elif inputpword[i] == ">":
            if temp:
                password.append(temp.pop())
        else:
            password.append(inputpword[i])
    #인터넷을 찾아보면 temp에 뭔가가 남아있다는 식으로 말하는데 그게 이해가 안됨. temp에 뭐 남아있을 리가 있나?
    print(''.join(password))