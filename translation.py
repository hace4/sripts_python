from googletrans import Translator


def txt_translate(text, src, dest):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        
        return translation.text

    except Exception as ex:
        return ex

def main():
    txt = input()
    src = input()
    dest = input()
    print(txt_translate(txt, src, dest))

if __name__ == '__main__':
    main()