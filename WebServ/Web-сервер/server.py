import socket
# from _thread import *
from email.utils import formatdate


# Текущий номер потока

# ThreadCount = 0

def start():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 8080))
    server.listen(5)
    while True:
        print('Working...')
        conn, address = server.accept()
        data = conn.recv(1024).decode('utf-8')
        print(data)
        content = load_page_from_get_request(data)
        print('content' + str(content))
        conn.sendall(content.encode())
        conn.shutdown(socket.SHUT_WR)




def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        # my_file = open('WEB'+path)
        # data = my_file.read()
        # return HDRS + data
        # my_file.close()
        with open('WEB'+path, 'r') as file:
            response = file.read()
        return HDRS + response
    except IOError:
        return HDRS_404 + 'Страница не существует'

if __name__ == '__main__':
    start()

