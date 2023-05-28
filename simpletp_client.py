import socket

ip_server = '127.0.0.1'  #
port_server = 54210
encoding_request = 'utf-8'
encoding_answer = encoding_request
size_package = 65536
answer = {}


def send_request(request, *args):
    request = str(request)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём сокет
    client_sock.connect((ip_server, port_server))  # Подключаемся к серверу
    client_sock.sendall(request.encode(encoding_request))  # Отправляем запрос в нужной нам кодировке
    data = client_sock.recv(size_package)  # Ждём ответа от сервера
    client_sock.close()  # Закрываем сокет
    answer = eval(data.decode(encoding_answer))
    return answer

# request = {"type_request": "authorization", "login": "admin", "password": "admin"}
# send_request(request)
