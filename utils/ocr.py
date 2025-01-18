import pytesseract
import PIL

def get_text(image_path:str):
    myconfig = '--psm 6 --oem 3'

    text = pytesseract.image_to_string(PIL.Image.open(image_path),config=myconfig)
    return text

if __name__ == "__main__":
    print(get_text("utils/text.jpg"))

