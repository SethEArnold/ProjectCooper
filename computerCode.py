import pafy
import vlc
import time
import threading
#import youtubePlayer
import requests

def playVideo(url):
	global player
	global videoPlaying
	videoPlaying = True
	if url:
		try:
			print("url is: " + url)
			video = pafy.new(url)
			best = video.getbest()
			playurl = best.url    
			media = instance.media_new(playurl)
			player.set_media(media)
			vidTime = video.length
			player.play()
			global t
			t = threading.Timer(vidTime, vidOver) 
			t.start()
		except:
			print("error with url")
	
def playNext():
	global q
	myPage = requests.get(url + "myurl")
	q = myPage.text.split(" ")	
	q = list(filter(bool, q))
	if q:		
		print(q)
		global videoPlaying
		if not videoPlaying:
			playVideo(q.pop(0))
	else:
		player.stop()

def vidOver():
	print("vidover")
	global videoPlaying
	videoPlaying = False
	print(requests.get(url + "vidover"))
	time.sleep(0.5)
	playNext()

def doNothing():
	return

def SkipCurrent():
	global videoPlaying
	global t
	t.cancel()
	global player
	player.pause()
	print("vidover")
	global videoPlaying
	videoPlaying = False
	playNext()
	
		
def trySkipCurrent():
	if videoPlaying:
		SkipCurrent()

		
url = "https://project-cooper.appspot.com/"
q = []
instance = vlc.Instance()    
player = instance.media_player_new()
player.set_fullscreen(True)
t= threading.Timer(0,doNothing)
videoPlaying = False
while(True):
	myPage = requests.get(url + "skip")
	if "yes" in myPage.text:
		trySkipCurrent()
	myPage = requests.get(url + "myurl")
	if "youtube" in myPage.text:
		playNext()
	time.sleep(1)	
		
	

