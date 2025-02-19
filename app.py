from flask import Flask, render_template, request
from models.translation_model import TranslationModel

app = Flask(__name__)

# Initialize translation model
model = TranslationModel()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    src_lang = request.form["src_lang"]
    tgt_lang = request.form["tgt_lang"]
    translation = model.translate(text, src_lang, tgt_lang)
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)