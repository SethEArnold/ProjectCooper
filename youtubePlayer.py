import pafy
import vlc
import time

def playVideo(url):
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url    
    media = instance.media_new(playurl)
    player.set_media(media)
    player.play()
   
instance = vlc.Instance(['--video-on-top'])    
player = instance.media_player_new()
player.set_fullscreen(True)   
url = "https://www.youtube.com/watch?v=1u4Q6rXkij0"
playVideo(url)
time.sleep(5)
url = "https://www.youtube.com/watch?v=LMph2hAGj7k"
playVideo(url)
time.sleep(5)
while True:
	url = input("enter url ")
	playVideo(url)