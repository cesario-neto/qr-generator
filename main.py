from flask import Flask, render_template, request
import qrcode
import string as s
from random import choices
from pathlib import Path

BASE_DIR = Path(__file__).parent
MEDIA_ROOT = BASE_DIR / 'frontend' / 'static' / 'assets' / 'media'

app = Flask(__file__,
            static_folder='frontend/static',
            template_folder='frontend/templates')


@app.route('/')
def index():
    context = {}
    return render_template('index.html', context=context)


@app.route('/qr-generator', methods=['POST'])
def qr_genarator():
    characters = list(s.ascii_letters + s.digits)
    file_name = ''.join(choices(characters, k=30)) + '.jpg'

    qr_form = request.form.get('qr_name')
    qr_img = qrcode.make(qr_form)
    qr_img.save(str(Path(MEDIA_ROOT / file_name).resolve()))

    context = {
        'have_qr': True,
        'qr_code': f'assets/media/{file_name}',
    }

    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
