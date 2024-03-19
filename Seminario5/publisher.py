import paho.mqtt.client as mqtt
import time
client = mqtt.Client('Publicador SD')
client.connect("localhost", 1883, 60)
client.loop_start()
c = 0
while True:
    c += 1
    topic = 'testtopic/sd2324'
    mensaje = f'Publicacion SD {c}'
    client.publish(topic, mensaje)
    time.sleep(1)
client.disconnect()