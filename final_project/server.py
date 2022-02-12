from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

#E2F Endpoint
@app.route("/englishToFrench")
def englishToFrench():
    return translator.englishToFrench(textToTranslate)

#F2E Endpoint
@app.route("/frenchToEnglish")
def frenchToEnglish():
    return translator.englishToFrench(textToTranslate)


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
