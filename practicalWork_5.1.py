import socket

url = input("Please enter a URL you wish to access: ")
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        # Splits the given URL and extracts the host name of the address
        if (url.startswith("http")):
            parts = url.split("/")
            hostName = parts[2]
            index = url.find("/")
            address = url[(index + 2):]
        else:
            parts = url.split("/")
            hostName = parts[0]
            address = url    
        mySocket.connect((hostName, 80))
        cmd = 'GET http://address HTTP/1.0\r\n\r\n'.encode(encoding="UTF-8", errors="strict")
        mySocket.send(cmd)
        data = mySocket.recv(512)
        if (len(data) > 0):
            break
    except:
        print("Error! Please enter valid URL.")
        url = input("Please enter a URL you wish to access: ")
count = 0
text = ""
while True:
    data = mySocket.recv(512)
    string_data = data.decode(encoding="UTF-8", errors="strict")
    # Counts the characters in the given website
    for char in string_data:
        count = count + 1
        text = text + char
        if count == 1800:
            break
    # Program stops when the limit of 1800 characters have been reached and prints out the content.
    if count == 1800:
        print(text)
        break
mySocket.close()