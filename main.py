from utils.ocr import get_text
from utils.video_processing import make_video
# from utils.mistral_results_processor import generate_and_preprocess
from utils.llama3_llm import generate_and_preprocess
from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os

load_dotenv()
UPLOAD_DIR = 'static/uploads'
VIDEO_DIR = 'static/videos'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_KEY')


@app.route('/')
def front_page():
    return render_template('best_intro.html')

@app.route('/home')
def home_page():
    return render_template('best_home.html')

@app.route('/login')
def login_page():
    return render_template('best_login.html')

@app.route('/register')
def register_page():
    return render_template('best_register.html')

@app.route('/upload',methods=['POST','GET'])
def upload_page():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(file_path)

            text = get_text(file_path)
            os.remove(file_path)
        else:
            text = request.form.get('text')

        try:
            session['video_url'] = make_video(json_obj=generate_and_preprocess(text))
        except:
            return "Either too short text or no text found"
                
        return redirect(url_for('display_image'))
    
    return render_template('best_upload.html')

@app.route('/display')
def display_image():
    video_url = session.get('video_url') 
    if video_url and os.path.exists(video_url):
        session.pop('video_url', None)
        return render_template('output.html', video_url=video_url)
    return "No file to display"

@app.route('/cleanup', methods=['POST'])
def cleanup_video():
    video_url = request.form.get('video_url')  
    if video_url and os.path.exists(video_url):
        os.remove(video_url)
    return "Video cleaned up", 200



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)