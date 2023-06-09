# App app.py is for testing application delivery workflows—see https://www.hashicorp.com/resources/application-delivery-hashicorp.
#
# Consider the following input environment variables.
#
# 1. APP - the name of your app; default: app.
# 2. ENV - the environment for your app; default: unset; example: dev, qa, prod.
# 3. FEATURES - some illustrative list of features; default: unset; example: some,prod,features
# 4. PASSWORD - illustrates some secret password; should be password123 (but again, only for illustration purposes, when you do this for realz, then don't commit your secrets into version control).

import os
import sys

import flask

app = flask.Flask(os.environ.get("APP", "app"))
app.config["APP"] = os.environ.get("APP", app.name)
app.config["ENV"] = os.environ.get("ENV", "unset")
app.config["FEATURES"] = os.environ.get("FEATURES", "unset")
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_SORT_KEYS"] = False

if os.environ.get("PASSWORD", "unset") != "password123":
    sys.stderr.write("app: error: Secret PASSWORD is wrong, set to password123 for illustration purposes.\n")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    return flask.jsonify(
        app=app.config["APP"],
        env=app.config["ENV"],
        features=app.config["FEATURES"],
    )
