from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return("hola mundo")

@app.route("/chau")
def goodbye():
    return("Chau")


app.run()
