from transformers import T5ForConditionalGeneration, T5Tokenizer

class TranslationModel:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained("t5-base")
        self.tokenizer = T5Tokenizer.from_pretrained("t5-base")

    def translate(self, text, src_lang, tgt_lang):
        # Preprocess input text
        input_text = f"translate {src_lang} to {tgt_lang}: {text}"
        inputs = self.tokenizer(input_text, return_tensors="pt")

        # Generate translation
        outputs = self.model.generate(inputs["input_ids"], max_length=100)

        # Postprocess output text
        translation = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return translation