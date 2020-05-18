# Wallpaper-Changer
<b>CLI to automatically change desktop background using Flickr/Unsplash API on Windows</b>

CLI interface to automatically change you dekstop background by fetching images from flickr/unsplash

optional arguments: `-t` update interval in hours (minutes between update/60), -tg (tag to search flickr with, 'goat' by default)

In order to run it in the background, you must call it with pythonw 

(if you want it to stop, then you must terminate pythonw.exe in taskmanager)

example: `pythonw wallpaper.py -tg cars -t .5/60 (this updates wallpaper every 30 seconds)`

If you only want it to run while CMD is open, then simply call it with python (will automatically stop running when you close CMD)

example: `python wallpaper.py -tg Japan -t 3/60  (this updates wallpaper every 3 minutes)`
