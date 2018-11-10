#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

print(url.endswith)

while not url.endswith('#'):
    #print('1')
    # Download the page.
    
    print('Downloading page %s...' % url)
    res = requests.get(url)
    #print('2')
    res.raise_for_status()
    #print('3')
    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image.
    #print(soup)
    comicElem = soup.select('#comic img')
    
    print(comicElem)
    #print('4')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:'+comicElem[0].get('src')
        
        # Download the image.
        
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        # Save the image to ./xkcd.
        
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's url.
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
print('Done')