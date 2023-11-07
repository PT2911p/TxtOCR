import os

os.environ["LRU_CACHE_CAPACITY"] = "1"

BASE_PATH = os.path.dirname(__file__)
MODULE_PATH = os.environ.get("EASYOCR_MODULE_PATH") or \
              os.environ.get("MODULE_PATH") or \
              os.path.expanduser("~/.EasyOCR/")

# detector parameters
detection_models = {
    'craft' : {
        'filename': 'craft_mlt_25k.pth',
        'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip',
        'md5sum': '2f8227d2def4037cdb3b34389dcf9ec1'
    },
    'dbnet18' : {
        'filename': 'pretrained_ic15_res18.pt',
        'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/v1.6.0/pretrained_ic15_res18.zip',
        'md5sum': 'aee04f8ffe5fc5bd5abea73223800425'
    },
    'dbnet50' : {
        'filename': 'pretrained_ic15_res50.pt',
        'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/v1.6.0/pretrained_ic15_res50.zip',
        'md5sum': 'a8e90144c131c2467d1eb7886c2e93a6'
    }
}

# recognizer parameters
latin_lang_list = ['en']
devanagari_lang_list = ['hi']

all_lang_list = latin_lang_list + devanagari_lang_list 
imgH = 64
separator_list = {
    'en': ['\xa4', '\xa5']
}
separator_char = []
for lang, sep in separator_list.items():
    separator_char += sep

recognition_models = {
    'gen1' : {
        'latin_g1':{
            'filename': 'latin.pth',
            'model_script': 'latin',
            'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/latin.zip',
            'md5sum': 'fb91b9abf65aeeac95a172291b4a6176',
            'characters': "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            'symbols': "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
        },
        'devanagari_g1':{
            'filename': 'devanagari.pth',
            'model_script': 'devanagari',
            'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/devanagari.zip',
            'md5sum': 'db6b1f074fae3070f561675db908ac08',
            'symbols': "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ",
            'characters': '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.ँंःअअंअःआइईउऊऋएऐऑओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळवशषसह़ािीुूृॅेैॉोौ्ॐ॒क़ख़ग़ज़ड़ढ़फ़ॠ।०१२३४५६७८९॰'
        },
    },
    'gen2' : {
        'english_g2':{
            'filename': 'english_g2.pth',
            'model_script': 'english',
            'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/english_g2.zip',
            'md5sum': '5864788e1821be9e454ec108d61b887d',
            'symbols': "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ €",
            'characters': "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ €ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        }
    }
}
