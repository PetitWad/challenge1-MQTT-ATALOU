import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT")
    else:
        print("Échec de la connexion. Code de retour =", rc)

def on_message(client, userdata, msg):
    print("Message reçu:", str(msg.payload.decode("utf-8")))

client = mqtt.Client()

# Spécifiez ici l'adresse IP ou le nom d'hôte de votre broker MQTT
broker_address = "127.0.0.1"

# Connexion au broker MQTT
client.connect(broker_address)

# Abonnement au topic
topic = "mytopic"
client.subscribe(topic)

client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
