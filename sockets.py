import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("195.154.53.62", 1337))


def read_data():
    heh = "="
    response = ""
    answer = ''
    while not heh in response:
        data = s.recv(1024).decode()
        response += data
        print(response)
        if not data:
            break
    pos = response.find(':')
    final = response[pos:][2:].split(' ')
    print(final)
    if final[1] == '*':
        answer = int(final[0])*int(final[2])
    if final[1] == '/':
        answer = int(final[0])//int(final[2]) 
    if final[1] == '-':
        answer = int(final[0])-int(final[2])
    if final[1] == '+':
        answer = int(final[0])+int(final[2])
    if final[1] == '%':
        answer = int(final[0])%int(final[2])
    print(answer)
    s.send(str('{}\n'.format(answer)).encode())
    

if __name__ == '__main__':
    while True:
        read_data()
    


