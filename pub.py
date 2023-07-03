import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT")
    else:
        print("Échec de la connexion. Code de retour =", rc)

client = mqtt.Client()

# Spécifiez ici l'adresse IP ou le nom d'hôte de votre broker MQTT
broker_address = "127.0.0.1"

# Connexion au broker MQTT

client.connect(broker_address)

client.loop_start()

while True:
    
    message ="Welcome to ATALOU MICROSYSTEM " # Le message à publier
    topic = "mytopic" # Le topic ou adresse qui delivrera le message
    
    # Publication du message
    client.publish(topic, message)
    print("Le message publié...")
    
    time.sleep(10)

client.loop_stop()
client.disconnect()
