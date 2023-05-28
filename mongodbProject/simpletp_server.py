import socket
from datetime import datetime
from Users_db import *
from Airs_db import *

port_server = 54210
max_connection = 10
dict_request = {}
dict_answer = {}
encoding_request = 'UTF-8'
encoding_answer = encoding_request
size_package = 65536


def run():
    global dict_request, dict_answer

    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', port_server))
    serv_sock.listen(max_connection)

    while True:  # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()

        while True:  # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            base = [Users_database(), Airs_database()]

            request = client_sock.recv(size_package)
            if not request:  # Если клиент отключился
                break

            dict_request = {'ip_client': client_addr[0],
                            'port_client': client_addr[1],
                            'request': eval(request.decode(encoding_request))}

            print(dict_request)
            type_request = dict_request.get("request").get("type_request")

            if type_request == 'authorization':
                typeOfRole = 0
                user = base[typeOfRole].search_authorization(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password"))
                if user != None:
                    dict_answer = bytes(str({'status': 'enter', 'content': user}), encoding=encoding_answer)
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'get_tickets':
                typeOfRole = 1
                user = base[0].search_authorization(base[0].collection,
                                                             dict_request.get("request").get("login"),
                                                             dict_request.get("request").get("password"))
                content = {}
                if user != None:
                    n = base[typeOfRole].countElements(base[typeOfRole].collection)
                    for i in range(n-1):

                        print(base[typeOfRole].returnElement(base[typeOfRole].collection, i))
                        content[str(i)] = base[typeOfRole].returnElement(base[typeOfRole].collection, i)
                    dict_answer = bytes(str({'status': 'enter', 'content': content}), encoding=encoding_answer)
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)


            elif type_request == 'get_my_tickets':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)


            elif type_request == 'buy_ticket':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'return_ticket':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'add_ticket':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'edit_ticket':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'remove_ticket':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'add_account':
                typeOfRole = 0
                if base[typeOfRole].search_authorization(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    if (dict_request.get("request").get("add_login") != None) or (dict_request.get("request").get("add_password") != None) or \
                        (dict_request.get("request").get("add_email") != None) or (dict_request.get("request").get("add_role") != None):
                        print((base[typeOfRole].search_login(base[typeOfRole].collection,
                                                       dict_request.get("request").get("add_login")) == None))
                        print((base[typeOfRole].search_email(base[typeOfRole].collection,
                                                       dict_request.get("request").get("add_email")) == None))
                        if (base[typeOfRole].search_login(base[typeOfRole].collection, dict_request.get("request").get("add_login")) == None) and \
                            (base[typeOfRole].search_email(base[typeOfRole].collection, dict_request.get("request").get("add_email")) == None):
                            id = base[typeOfRole].countElements(base[typeOfRole].collection)
                            user = {"_id": id, "login": dict_request.get("request").get("add_login"),
                                    "password": dict_request.get("request").get("add_password"),
                                    "email": dict_request.get("request").get("add_email"),
                                    "role": dict_request.get("request").get("add_role"),
                                    "date_registration": str(datetime.now().year) + '/' + str(datetime.now().month) + '/' + str(datetime.now().day), "name": None,
                                    "surname": None, "patronymic": None, "virtual_money": 0, "points_mile": 0,
                                    "myticket": {}}
                            base[typeOfRole].add(base[typeOfRole].collection, user)
                            dict_answer = bytes(str({'status': 'enter'}),
                                                encoding=encoding_answer)
                        else:
                            dict_answer = bytes(str({'status': 'error account already exists'}), encoding=encoding_answer)
                    else:
                        dict_answer = bytes(str({'status': 'error nothing textfield'}), encoding=encoding_answer)
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            elif type_request == 'remove_account':
                typeOfRole = 0
                if base[typeOfRole].search(base[typeOfRole].collection, dict_request.get("request").get("login"), dict_request.get("request").get("password")):
                    for i in range(10):
                        pass
                else:
                    dict_answer = bytes(str({'status': 'error authorization'}), encoding=encoding_answer)

            else:
                dict_answer = bytes(str({'status': 'error request'}), encoding=encoding_answer)

            if dict_answer != {}:
                print(dict_answer)
                client_sock.sendall(dict_answer)
                dict_answer = {}

        client_sock.close()


run()