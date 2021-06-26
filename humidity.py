import Adafruit_DHT

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "bkIYNQyvKtdruwtD66-YrpHLid3vWtQGzc_nOlZiJAg7JMScKL3al7Z2cGHy_xPCjAOC7poiWpVz-mHJfeViwQ=="
org = "jimboylabs"
bucket = "jimboylabs"

client = InfluxDBClient(url="http://192.168.8.146:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
	sequence = ["mem,host=host1 humidity={0:0.1f}".format(humidity), "mem,host=host1 temperature={0:0.1f}".format(temperature)]
	write_api.write(bucket, org, sequence)
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(30)

