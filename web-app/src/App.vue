<template>
  <div>
    <button @click="createConnection">Create connection over mqtt</button>
  </div>
</template>

<script>
import mqtt from 'mqtt'

export default {
  data() {
    return {
      connection: { host: "192.168.0.178", port: 1883 },
      subscription: {
        topic: "temperature",
        qos: 0,
      },
      client: {
        connected: false,
      },
      receiveNews: '',
      subscribeSuccess: false,
    };
  },

  methods: {
    // Setting up the connection
    createConnection() {
      //const { host, port} = this.connection
      //const connectUrl = `mqtt://${host}:${port}`
      try {
        this.client = mqtt.connect('mqtt://192.168.0.178:1883', {})
      } catch (error) {
        console.log('mqtt.connect error', error)
      }
      this.client.on('connect', () => {
        console.log('Connection succeeded!')
      })
      this.client.on('error', error => {
        console.log('Connection failed', error)
      })
      this.client.on('message', (topic, message) => {
        this.receiveNews = this.receiveNews.concat(message)
        console.log(`Received message ${message} from topic ${topic}`)
      })
    },
  },
};
</script>