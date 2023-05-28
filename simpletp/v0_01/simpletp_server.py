import socket

port_server = 53210
max_connection = 10
encoding_request = 'utf-8'
size_package = 1024


def run():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', port_server))
    serv_sock.listen(max_connection)

    while True:  # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()

        while True:  # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            data = client_sock.recv(size_package)
            if not data:  # Если клиент отключился
                break

            request = {'ip_client': client_addr[0],
                       'port_client': client_addr[1],
                       'body_requests': data.decode(encoding_request)}
            print(request)
            client_sock.sendall(data)

        client_sock.close()


run()
