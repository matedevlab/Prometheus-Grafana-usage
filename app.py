import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_host():
    hostname = socket.gethostname()
    return f"The name of the host server is: {hostname}\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
