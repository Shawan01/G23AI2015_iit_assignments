from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello Guys, I am Anup Shaw. This is a dummy Application created for VCC Docker Assignment!!!!"
if __name__ == "__main__":
    app.run()