from flask import Flask, render_template, request, redirect, url_for
from models.translation_model import TranslationModel

app = Flask(__name__)

# Initialize translation model
model = TranslationModel()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        src_lang = request.form["src_lang"]
        tgt_lang = request.form["tgt_lang"]
        translation = model.translate(text, src_lang, tgt_lang)
        return redirect(url_for("result", translation=translation))
    return render_template("index.html")

@app.route("/result/<translation>")
def result(translation):
    return render_template("result.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)