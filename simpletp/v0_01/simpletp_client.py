import socket

ip_server = '127.0.0.1'  #
port_server = 53210
encoding_request = 'utf-8'
encoding_answer = encoding_request
size_package = 1024


def send_request(request, *args):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём сокет
    client_sock.connect((ip_server, port_server))  # Подключаемся к серверу
    client_sock.sendall(request.encode(encoding_request))  # Отправляем запрос в нужной нам кодировке
    data = client_sock.recv(size_package)  # Ждём ответа от сервера
    client_sock.close()  # Закрываем сокет
    print('Received', data.decode(encoding_answer))


send_request('Привет мир!')
