import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT")
    else:
        print("Échec de la connexion. Code de retour =", rc)

client = mqtt.Client()

broker_address = "127.0.0.1" # Spécifiez ici l'adresse IP ou le nom d'hôte de votre broker MQTT
topic = "mytopic" # Le topic ou adresse qui delivrera le message
message ="Welcome to ATALOU MICROSYSTEM " # Le message à publier

# Connexion au broker MQTT
client.connect(broker_address)
client.loop_start()

while True:
    
    client.publish(topic, message) # Publication du message
    print("Le message publié...")
    
    time.sleep(10)

client.loop_stop()
client.disconnect()
