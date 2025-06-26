import time
import json
import random
import paho.mqtt.client as mqtt

# AWS IoT Core Endpoint (yours looks correct)
ENDPOINT = "a2rtdeqrvgnovt-ats.iot.ap-south-1.amazonaws.com"

# MQTT client setup
client = mqtt.Client(client_id="truck_simulator")
client.tls_set(
    ca_certs="certs/root-CA.crt",
    certfile="certs/device.pem.crt",
    keyfile="certs/private.pem.key"
)

# Connect and start loop
client.connect(ENDPOINT, 8883)
client.loop_start()  # important for async socket handling
print(" Connected to AWS IoT Core broker")

# Truck IDs
truck_ids = ["truck001", "truck002", "truck003", "truck004", "truck005"]

# Publish loop
while True:
    truck_id = random.choice(truck_ids)
    topic = f"fleet/{truck_id}/data"  # dynamic topic (no wildcard here)

    payload = {
        "truckId": truck_id,
        "timestamp": int(time.time()),
        "speed": round(random.uniform(30, 100), 2),
        "engineTemp": round(random.uniform(70, 110), 2),
        "fuelLevel": round(random.uniform(10, 100), 2)
    }

    # Publish
    result = client.publish(topic, json.dumps(payload), qos=1)
    print(f" Published to {topic}: {payload}")

    # Optional: confirm success
    if result.rc != mqtt.MQTT_ERR_SUCCESS:
        print(" Publish failed:", mqtt.error_string(result.rc))

    time.sleep(5)
