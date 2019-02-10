from flask import Flask, render_template, request
import pafy
import vlc
import time
import youtubePlayer
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		requestForm = request.form.to_dict()
		if("text" in requestForm.keys()):
			print(request.form['text'])
			youtubePlayer.addVidToQueue(request.form['text'])
			return render_template('test1.html')
		else:
			youtubePlayer.SkipCurrent()
			return render_template('test1.html')
	else:
		return render_template('test1.html')