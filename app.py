from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

from models.translation_model import TranslationModel

# Initialize translation model
model = TranslationModel()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['text'] = request.form["text"]
        session['src_lang'] = request.form["src_lang"]
        session['tgt_lang'] = request.form["tgt_lang"]
        
        try:
            translation = model.translate(session['text'], session['src_lang'], session['tgt_lang'])
            session['translation'] = translation
            return render_template("result.html")
        except Exception as e:
            session['translation'] = str(e)
            return render_template("result.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)