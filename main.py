from flask import Flask
import requests

app = Flask(__name__)
print("App initilized")


@app.route("/")
def home():
    return "Hello Mostafa Arshadi. from heroku"

@app.route("/hi")
def home():
    return requests.get("https://google.com").text




if __name__ == "__main__":
    import os
    PORT =os.getenv("PORT",5000)
    app.run("0.0.0.0",PORT)