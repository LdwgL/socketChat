from threading import Thread
import socket

def Send(client):
    while True:
        msg = input()
        msg = msg.encode("utf-8")
        client.send(msg)
def Reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        print(requete_client)
        if not requete_client : #Si on perd la connexion
            print("CLOSE")
            break

Host = "127.0.0.1"
Port = 8080

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrête jusqu'a une connexion
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])

envoi.start()
recep.start()

recep.join()

client.close()
socket.close()
