from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_download', methods=['POST'])
def run_download():
    # download_video.pyを実行
    subprocess.run(['python3', 'src/download_video.py'])
    return redirect(url_for('index'))

@app.route('/run_upload', methods=['POST'])
def run_upload():
    # upload_to_drive.pyを実行
    subprocess.run(['python3', 'src/upload_to_drive.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/run_download', methods=['POST'])
def run_download():
    subprocess.run(['python3', 'src/download_video.py'])
    return redirect(url_for('index'))

@app.route('/run_upload', methods=['POST'])
def run_upload():
    subprocess.run(['python3', 'src/upload_to_drive.py'])
    return redirect(url_for('index'))
