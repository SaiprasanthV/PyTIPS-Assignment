import imghdr
import os
import time
from flask import Flask, flash, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename

PATH = 'uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = [
    '.jpg', '.png', '.gif', '.txt', '.pdf', '.jpeg']
app.config['UPLOAD_PATH'] = PATH


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST'])
def upload_files():
    files = os.listdir(app.config['UPLOAD_PATH'])
    if request.form.get('Submit'):
        global uploaded_file
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                # abort(400)
            else:
                uploaded_file.save(os.path.join(
                    app.config['UPLOAD_PATH'], filename))
                flash('File successfully uploaded', category='success')
        return redirect(url_for('index'))

    elif request.form.get('Size'):
        return render_template('index.html', files=files, size=view_size())

    elif request.form.get('Date_Modified'):
        return render_template('index.html', files=files, mdate=view_mdate())

    elif request.form.get('No_of_line'):
        return render_template('index.html', files=files, n_lines=view_nlines())

    return redirect(url_for('index'))


# @app.route('/data', methods=['GET', 'POST'])
# def datas():
#     my_dir = PATH

#     for f in os.listdir(my_dir):
#         print(f)
#         flash(f, category='success')
#         path = os.path.join(my_dir, f)
#         if os.path.isfile(path):
#             print("last modified: %s" % time.ctime(os.path.getmtime(path)))
#             print(os.path.getsize(path), 'bytes')

#     # return redirect(url_for('index'), data='dummy')
#     return render_template('index.html', data='dummy')


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


def view_size():
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        size = str(os.path.getsize(path))
        return(size + 'Bytes')
    else:
        return None


def view_mdate():
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        mdate = str(time.ctime(os.path.getmtime(path)))
        return('Modified date: ' + mdate)
    else:
        return None


def view_nlines():
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        # nlines = len(open(uploaded_file.filename).readlines())
        count = 0
        with (open(path, "r") as reader):
            content = reader.read()
            colist = content.split("\n")

        for lines in colist:
            if lines:
                count += 1
        count = str(count)
        return ("Number of lines: " + count)
        # return('No of lines: ' + str(nlines))
    else:
        return None


if __name__ == '__main__':

    app.run(debug=True)
