import os
from flask import Flask, render_template, request, send_from_directory, abort


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file.filename:
            filename = upload_file.filename
            root = os.path.abspath(app.config['UPLOAD_FOLDER']) + os.sep
            abs_filename = os.path.abspath(os.path.join(root, filename.strip('/')))
            print abs_filename
            if not abs_filename.startswith(root):
                return abort(403)

            upload_file.save(abs_filename)
            return render_template('index.html', filename=os.path.basename(abs_filename))

    return render_template('index.html')


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)