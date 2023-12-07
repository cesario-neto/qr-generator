from flask import Flask, render_template

app = Flask(__file__,
            static_folder='frontend/static',
            template_folder='frontend/templates')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
