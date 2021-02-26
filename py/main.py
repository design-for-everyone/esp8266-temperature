def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  sleep_ms(10000)
  machine.reset()

print("started in main.py")

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

from machine import Pin
import dht

led = Pin(2,Pin.OUT)
sensor = dht.DHT11(Pin(14))

counter = 0

while True and counter < 10:
    counter = counter + 1;
    led.value(1)
    print("ready to measure")
    sensor.measure()
    led.value(0)
    print("measured")
    temp = sensor.temperature()
    hum = sensor.humidity()
    client.publish(b'weather/temperature',str(temp))
    client.publish(b'weather/humidity',str(hum))
    sleep_ms(5000)
#     sleep_ms(1500)
#     msg = "I say hello"
#     client.publish(topic_pub, msg)
#     print(topic_pub);
#     print("message was send");


print("done sending")
# while True:
#   try:
#     client.check_msg()
#     if (time.time() - last_message) > message_interval:
#       msg = b'Hello #%d' % counter
#       
#       last_message = time.time()
#       counter += 1
#   except OSError as e:
#     restart_and_reconnect()