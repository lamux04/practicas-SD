import time
import paho.mqtt.client as mqtt
client = mqtt.Client('Suscriptor 1')
def mostrar_msg(client, userdata, message):
    print('Evento recibido: {}'.format(str(message.payload.decode('utf-8'))))
    print('Tema: {}'.format(message.topic))
client.on_message = mostrar_msg
client.connect("localhost", 1883, 60)
client.loop_start()
client.subscribe('testtopic/sd2324')
client.subscribe('testtopic/poo2324')
time.sleep(120)
client.loop_stop()
client.disconnect()