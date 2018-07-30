import subprocess,os,sys,ctypes,requests,click,getpass,apscheduler.schedulers.blocking
from bs4 import BeautifulSoup as bs4
from pprint import pprint
import flickrapi as api
flickr_api_key = #
flickr_api_secret = #
flickr = api.FlickrAPI(flickr_api_key,flickr_api_secret,format = 'parsed-json')
photos = []
def downloadFlickrImage(width,height,url):
    [os.remove(f) for f in os.listdir(".") if f.endswith(".jpg")] #deletes old photo
    res = requests.get(url)
    parse = bs4(res.content,'html.parser')
    url = ''
    for p in parse.select('img'):
        if 'staticflickr' in p['src']: #this should only be true once
            url = p['src']
            res = requests.get(p['src'])
    os.chdir(r'C:\Users' +"\\"+ str(getpass.getuser()) + r'\Pictures\Wallpapers')
    output = open('flickrpicture.jpg','wb')
    output.write(res.content)
    output.close()
    return url
def downloadUnsplashImage(url):
    res = requests.get(url)
    parse = bs4(res.content,'html.parser')
    output = open('unsplashpicture.jpg','wb')
    output.write(res.content)
    output.close()
def set_desktop_background(file):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file , 0)
def unsplash_calls(tag='animals',dimensions=(1920,1080)):
    os.chdir(r'C:\Users\tmoye\Pictures\Wallpapers')
    downloadUnsplashImage('https://source.unsplash.com/' + str(dimensions[0]) +
    'x' + str(dimensions[1]) + '/?' + tag)
    path = str(os.getcwd()) + '/unsplashpicture.jpg'
    set_desktop_background(path)
def flickr_calls(query='animals',pSize='k'):
    global photos
    if len(photos)<=5:
        photos = flickr.photos.search(tags=query,per_page=500,content_type=1,sort='interestingness-desc')['photos']['photo']
    current = photos.pop(0)
    os.chdir(r'C:\Users\tmoye\Pictures\Wallpapers')
    url = r'https://www.flickr.com/photos/' + str(current['owner']) + '/' + str(current['id']) + '/sizes/' + str(pSize)
    imageUrl = 'abc' #placeholder
    while '_' + str(pSize)+'.jpg' not in imageUrl:
        if(len(photos)==0):
            photos = flickr.photos.search(tags=query,per_page=500,content_type=1,sort='interestingness-desc')['photos']['photo']
            current =  photos.pop(0)
        else:
            current = photos.pop(0)
        url = r'https://www.flickr.com/photos/' + str(current['owner']) + '/' + str(current['id']) + '/sizes/'+str(pSize)
        imageUrl = downloadFlickrImage(1920, 1080,url)
    path = str(os.getcwd()) + '/flickrpicture.jpg'
    set_desktop_background(path)

@click.command()
@click.option('--tag','-tg',help='tag to search (goat by default because they are objectively dope)')
@click.option('--size','-s',help='size of image \n possible values: k(2048 * 1152), h(1600x900),l(1024x576)')
@click.option('--time','-t',help= 'enter interval (minutes between update/60) at which background should be updated')
def main(tag,size,time):
    """
    CLI interface to automatically change you dekstop background by fetching images from flickr
    In order to run it in the background, you must call it with pythonw (if you want it to stop, then you must terminate pythonw.exe in taskmanager)
    example: pythonw wallpaper.py cars
    If you only want it to run while CMD is open, then simply call it with python (will automatically stop running when you close CMD)
    example: python wallpaper.py Japan
    """
    if tag == None:
        tag = 'animals'
    if size == None:
        size = 'k'
    if time == None:
        time = '.5/60'
    scheduler = apscheduler.schedulers.blocking.BlockingScheduler()
    scheduler.add_job(unsplash_calls,'interval',[tag,(1920,1080)],hours = eval(time),max_instances = 10)
    #scheduler.add_job(flickr_calls,'interval',[tag,size],hours = eval(time),max_instances = 10)
    scheduler.start()

if __name__ == '__main__':
    main()
