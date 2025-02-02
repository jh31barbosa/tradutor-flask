from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Configuração da API de tradução (exemplo usando LibreTranslate)
TRANSLATE_API_URL = "https://api.mymemory.translated.net/get"

def translate_text(text, source_lang, target_lang):
    payload = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }
    response = requests.get(TRANSLATE_API_URL, params=payload)
    
    print("API Response:", response.status_code, response.text)
    
    if response.status_code == 200:
        return response.json().get("responseData", {}).get("translatedText", "Erro na tradução")
    return "Erro ao conectar à API"


@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    if request.method == "POST":
        text = request.form.get("text")
        source_lang = request.form.get("source_lang")
        target_lang = request.form.get("target_lang")
        if text and source_lang and target_lang:
            translation = translate_text(text, source_lang, target_lang)
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True, port=5001)