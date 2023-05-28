import socket
import json

port_server = 53210
max_connection = 10
dict_request = {}
dict_answer = {}
encoding_request = 'UTF-8'
encoding_answer = encoding_request
size_package = 1024


def run():
    global dict_request, dict_answer

    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', port_server))
    serv_sock.listen(max_connection)

    while True:  # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()

        while True:  # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            request = client_sock.recv(size_package)
            if not request:  # Если клиент отключился
                break

            dict_request = {'ip_client': client_addr[0],
                       'port_client': client_addr[1],
                       'request': eval(request.decode(encoding_request))}

            print(dict_request)
            type_request = dict_request.get("request").get("type_request")
            if type_request == 'authorization':
                dict_answer = bytes(str({'status': 'enter'}), encoding=encoding_answer)
            else:
                dict_answer = bytes(str({'status': 'error'}), encoding=encoding_answer)
            if dict_answer != {}:
                client_sock.sendall(dict_answer)
                dict_answer = {}

        client_sock.close()

run()