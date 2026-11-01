#Read one message from a TCP client. 
# Validate the whole message format username:alice, password: secret123. 
# Allow whitespace around separators. 
# Print username/password on separate lines, or Fail.

import socket, re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 8080))
s.listen()

con, addr = s.accept()

reply = con.recv(1024).decode()

match = re.fullmatch(r'username:\s*(\w+),\s*password:\s*(\w+)',
                     reply
)

if match:
    print(match.group(1))
    print(match.group(2))
else:
    print('Fail')

con.close()
s.close()

