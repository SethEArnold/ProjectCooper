import pafy
import vlc
import time
import threading

def playVideo(url):
	global player
	global videoPlaying
	videoPlaying = True
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
   
def addVidToQueue(url):
	q.append(url)
	playNext()	
	
def playNext():
	global videoPlaying
	if not videoPlaying:
		if q:
			playVideo(q.pop(0))

def vidOver():
	global videoPlaying
	videoPlaying = False
	playNext()

def doNothing():
	return

def SkipCurrent():
	global videoPlaying
	global t
	t.cancel
	global player
	player.pause()
	videoPlaying = False
	playNext()	

q = []
instance = vlc.Instance(['--video-on-top'])    
player = instance.media_player_new()
player.set_fullscreen(True)
t= threading.Timer(0,doNothing)
videoPlaying = False