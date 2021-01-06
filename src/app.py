import asyncio

from flask import Flask, jsonify, request, json

from nats.aio.client import Client as NATS
app = Flask(__name__)

async def publish_nats(payload, host, channel):
    nc = NATS()
    await nc.connect(host)
    try:
        print(u'\u2753', end="")
        await nc.publish(channel, str.encode(payload))
    except Exception as e:
        print(str(e))
    await nc.close()
    print(f"Publishing to nats channel {channel}")

@app.route("/")
def hello_gitlab():
    message = "Hello, Healthcheck confirms proxy up and running"
    payload = {"message": message}
    return jsonify(payload)

@app.route("/new", methods=['POST'])
def new():
    data = request.json
    payload = {"message": f"Your message {data['message']} has been published to nats"}
    asyncio.run(publish_nats(json.dumps(request.json), "nats://nats:4222", "foobar"))
    return jsonify(payload)

@app.route("/new2", methods=['POST'])
def new2():
    data = request.json
    payload = {"message": f"Your message {data['message']} has been published to nats"}
    asyncio.run(publish_nats(json.dumps(request.json), "nats://nats:4222", "foobar2"))
    return jsonify(payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)