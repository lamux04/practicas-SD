import paho.mqtt.client as mqtt
import time
client = mqtt.Client('Publicador POO')
client.connect("localhost", 1883, 60)
client.loop_start()
c = 0
while True:
    c += 1
    topic = 'testtopic/poo2324'
    mensaje = f'Publicacion POO {c}'
    client.publish(topic, mensaje)
    time.sleep(5)
client.disconnect()