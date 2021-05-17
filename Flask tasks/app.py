import imghdr
import os
import time
from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    send_from_directory,
)
from werkzeug.utils import secure_filename

PATH = "uploads"

app = Flask(__name__)
app.secret_key = "secret key"

# configuring the upload file size limit -> 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

# allowed file formats
app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".gif", ".txt", ".pdf", ".jpeg"]
# configuring the default uploa path
app.config["UPLOAD_PATH"] = PATH


@app.route("/")
def index():
    files = os.listdir(app.config["UPLOAD_PATH"])
    return render_template("index.html", files=files)


@app.route("/", methods=["POST"])
def upload_files():
    files = os.listdir(app.config["UPLOAD_PATH"])
    if request.form.get("Submit"):
        global uploaded_file
        uploaded_file = request.files["file"]
        filename = secure_filename(uploaded_file.filename)
        if filename != "":
            # checking the file format by extecting file extension from file name
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                flash("Allowed file types are txt, pdf, png, jpg, jpeg, gif")
                # abort(400)
            else:
                # saving the file configured Upload path
                uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
                flash("File successfully uploaded", category="success")
        return redirect(url_for("index"))

    elif request.form.get("Size"):
        # displaying the size of uploaded file
        return render_template("index.html", files=files, size=view_size())

    elif request.form.get("Date_Modified"):
        # displaying the modified date of uploaded file
        return render_template("index.html", files=files, mdate=view_mdate())

    elif request.form.get("No_of_line"):
        # displaying the number of line in uploaded file
        return render_template("index.html", files=files, n_lines=view_nlines())

    return redirect(url_for("index"))


@app.route("/uploads/<filename>")
def upload(filename):
    # displaying the uploaded files
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


def view_size():
    # returns the size of particular file
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        size = str(os.path.getsize(path))
        return size + " Bytes"
    else:
        return None


def view_mdate():
    # returns the modified date of particular file
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        mdate = str(time.ctime(os.path.getmtime(path)))
        return "Modified date: " + mdate
    else:
        return None


def view_nlines():
    # return the number of lines in a file
    path = os.path.join(PATH, uploaded_file.filename)
    if os.path.isfile(path):
        nlines = len(open(path).readlines())
        return "Number of lines: " + str(nlines)
    else:
        return None


if __name__ == "__main__":

    app.run(debug=True)
