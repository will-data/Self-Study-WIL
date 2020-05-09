import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter -')

mysock.connect((url.split('/')[2], 80))

cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
print(cmd)
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()