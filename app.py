#Here I've imported the libraries that I need for this project😁️
import sys
import os
from flask import Flask, render_template, url_for, request, flash, redirect, send_from_directory, Response
import pdftotext
from gtts import gTTS
from werkzeug.utils import secure_filename

#Here I've initialized the path for the upload folder for the user to upload the book in PDF format😉️
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/templates/static/assets/upload/'
ALLOWED_EXTENSIONS = {'pdf'} #Only PDF readable books are allowed😈️

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#The functionality of the app starts from here😋️
#Here I've initialized the flask's function to the variable named app🌟️  
app = Flask(__name__)

#Here I've configured the upload folder and the static folder to allow the app to access the HTML, CSS & JAVASCRIPT files😎️
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app._static_folder = './templates/static'

#This app route helps to open the index.html(home page)😗️
@app.route('/')
def home():
    return render_template('index.html')

#This app route helps to open the project.html(upload page)😗️
@app.route('/upload')
def upload():
    return render_template('upload.html')
    
#This app route helps to open the about.html(about page)😗️
@app.route('/about')  
def about():  
    return render_template("about.html")  

#This app route let's the user to upload the PDF file from the users ⬆️📕️
@app.route('/upload', methods=['GET', 'POST'])
def index():
   b = request.form['a']
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           pdf_1 = file.filename
           pdf_2 = str('gen.pdf')
           pdf_1 = pdf_2
           filename = secure_filename(pdf_1)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
           return redirect(url_for('home_3'))

#In this app route we call the path of the uploaded pdf file and it's file name🔖️
@app.route('/upload')
def process_file(path, filename):
   conversion(path, filename)    

#This  app route is where the magic begins, This peice of code converts the text from the book to audio format 📕️ ➡️ 🔉️
@app.route('/upload', methods=['GET', 'POST'])
def conversion(path, filename):  
        b = int(request.form['a']) 
        c = b-1      
        with open(path, "rb") as f: 
	        pdf = pdftotext.PDF(f) 
	        pdf_text = pdf[c]

        string_of_text = ''
        for text in pdf_text:
   	        string_of_text += text

        language = 'en'
        final_file = gTTS(text=pdf_text, lang=language, tld='ie') 
        final_file.save("./templates/static/assets/voices/gensp.mp3")
        return redirect(url_for('home_3'))

#This approute is for streaming the audio from the voices folder as mentioned in the code 🎚️
@app.route("/audio")
def streamwav():
    def generate():
        with open("./templates/static/assets/voices/gensp.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/mpeg")
    
#This code is used for display the PDF uploaded by the user 📖️
@app.route("/yourPDF")
def pdf_3():
    def pdf_5():
        with open("./templates/static/assets/upload/gen.pdf", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(pdf_5(), mimetype="application/pdf")

#This app route helps to open the tts.html(Text-To-Speech page)😗️
@app.route("/ts")
def home_5():
    return render_template("tts.html")

#This peice of code converts the text that you enter to audio format 🗒️ ➡️ 🔉️
@app.route("/ts", methods=['GET', 'POST'])
def tts():
    c = str(request.form['b'])
    language = 'en'
    tts = gTTS(text=c, lang=language, tld='ie')
    tts.save("./templates/static/assets/ttsf/rec.mp3")
    return redirect(url_for('converted'))

@app.route("/tts")
def converted():
    return render_template("converted.html")

#This app route is for streaming the audio from the voices folder as mentioned in the code 🎚️
@app.route("/mp")
def con_tts():
    def generated():
        with open("./templates/static/assets/ttsf/rec.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generated(), mimetype="audio/mpeg")

#This approute is used to open the audio.html(audio page) for the user to listen to their audiobook and read along 📕️ ➡️ 🎧️
@app.route('/yourbook')
def home_3():
    return render_template('audio.html')


#This peice of code allow flask to run the app in a testing server 🤗️
if __name__ == "__main__":
    app.run()
    
#Created for lazy readers only😇️
#This project is done by yours truly Jared Steven😑️

