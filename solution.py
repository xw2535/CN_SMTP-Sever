from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailServer ='127.0.0.1'
    mailPort=1025
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    
    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailServer, mailPort))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = '<mail@mail.com>\r\n'
    clientSocket.send(mailfromCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print(' mail 250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = '<myemail@gmail.com>\r\n'
    clientSocket.send(rcpttoCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('rcpt 250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'Data'
    print(dataCommand)
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('data 250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    message = input('Enter Message Here: ')
    # Fill in end
    # Message ends with a single period.
    # Fill in start
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('msg 250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    print(quitCommand)
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('quit 250 reply not received from server.')


        pass
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
