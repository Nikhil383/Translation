# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TranslationModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-small")

    def translate(self, text, src_lang, tgt_lang):
        # Preprocess input text
        input_text = f"translate {src_lang} to {tgt_lang}: {text}"
        inputs = self.tokenizer(input_text, return_tensors="pt")

        # Generate translation
        outputs = self.model.generate(inputs["input_ids"], max_length=100)

        # Postprocess output text
        translation = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return translation