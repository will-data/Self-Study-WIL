n = int(input())
phone_book = {}
for i in range(n):
    name, phoneNumber = input().split()
    phone_book[name] = phoneNumber

while True:
    # Use try syntax for the not fixed number of inputs
    try:
        name = input()
        if name in phone_book:
            print(name,'=',phone_book[name], sep="")
        else:
            print('Not found')
    except EOFError:
        break