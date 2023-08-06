import os
import socket

from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

requests_counter = Counter("myapp_requests_total", "Total number of requests")


@app.route("/")
def get_host():
    try:
        hostname = socket.gethostname()
        return f"The name of the host server is: {hostname}\n"
    except socket.error as e:
        print(f"Error retrieving hostname: {e}")


@app.route("/metrics")  # this endpoint will prometheus watches
def metrics():
    # Increment the counter metric for each request
    requests_counter.inc()

    # Generate Prometheus metrics output
    return Response(generate_latest(), content_type="text/plain")


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))

    app.run(host=host, port=port)
