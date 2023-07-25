import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")  # this endpoint will prometheus watches
def get_host():
    try:
        hostname = socket.gethostname()
        return f"The name of the host server is: {hostname}\n"
    except socket.error as e:
        print(f"Error retrieving hostname: {e}")


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port)
