#  Smart Fleet Monitor with AWS IoT Core

A scalable MQTT-based fleet monitoring system that publishes real-time truck data (speed, engine temperature, fuel level) to AWS IoT Core, stores it in DynamoDB, and sends alerts using SNS.

## Features

-  Simulates real-time sensor data from 5 trucks using Python and Paho MQTT
-  Publishes securely via TLS to AWS IoT Core
-  Subscribes via AWS MQTT Test Client and stores data into DynamoDB via Lambda
-  Triggers SNS alerts when engine temperature exceeds threshold
-  Easily extendable to integrate Node-RED, Grafana, or AWS QuickSight dashboards

## 📁 Project Structure


##  How It Works

1. **Device Simulation**: Publishes JSON data to topic `fleet/<truckId>/data`
2. **IoT Rule**: Captures all data via wildcard topic `fleet/+/data`
3. **Lambda Function**: Parses payload and writes to DynamoDB
4. **SNS**: Sends alert if `engineTemp > 80°C`

##  Technologies

- AWS IoT Core
- AWS Lambda
- Amazon DynamoDB
- Amazon SNS
- Python (paho-mqtt)

##  Sample Payload

```json
{
  "truckId": "truck003",
  "timestamp": 1750924994,
  "speed": 76.92,
  "engineTemp": 83.45,
  "fuelLevel": 55.18
}

