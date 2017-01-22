import time
import webbrowser


times = 2
times_count = 0

while times_count < times:
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=43TvYyqYTTM")
	times_count = times_count + 1
