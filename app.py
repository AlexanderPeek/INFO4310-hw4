from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root="static/",
    prefix="static/",
    index_file="index.html",
    autorefresh=True,
)


@app.route("/", methods=["GET"])
def server():
    return make_response("go to the route /static/")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
