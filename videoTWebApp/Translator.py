from googletrans import Translator

translator = Translator()


def translate(fileSource: str, language: str, title: str):
    with open(fileSource, 'r', encoding='utf-8') as file1:
        with open(f"{title}translated.txt", 'w', encoding='utf-8') as file2:
            for i in file1:
                input_text = i
                output = translator.translate(input_text, dest=language)
                file2.write(output.text + '\n')
    file1.close()
    file2.close()

