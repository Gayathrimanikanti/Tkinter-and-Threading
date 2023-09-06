#Example 1:Downloading the images concurrently
'''
The threading module uses threads ,the multiprocessing module uses processes:
The difference is that threads run in the same memory space:
'''






#suppose u want to download several images from the internet.using threading ,u can do

import threading
import requests

def download_image(url,filename):
     response = requests.get(url)
     with open (filename,'wb')as f:
         f.write(response.content)
     print(f"{filename}downloaded")

image_urls = [
     "https://www.boredart.com/wp-content/uploads/2018/02/DIY-Filled-Balloons-Decoration-Ideas-12.jpg",
     "https://i0.wp.com/notedlist.com/wp-content/uploads/2015/07/balloon-decoration-ideas/20-balloon-decoration-ideas.jpg",
    "https://images.squarespace-cdn.com/content/v1/5c8eb51aebfc7faf979f7f76/1e8ce49b-7cd7-4788-97a0-6291aff65985/free+balloon+coloring+pages.jpg"
   ] #...add more urls




threads = []
for i,url in enumerate (image_urls):
    filename = f"data/image_{i}.jpg"
    thread = threading.Thread(target=download_image, args =(url,filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All images downloaded")
