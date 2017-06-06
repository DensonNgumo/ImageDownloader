import random
import urllib.request

def getRandomTitle():
    randomString='img'
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for n in range(5):
        randomString+=alphabets[random.randrange(0,25)]
    randomString+=str(random.randrange(1,1000))+".jpg"    
    return randomString    
   
def downloadImage(url):
    imageTitle= getRandomTitle()
    urllib.request.urlretrieve(url,imageTitle)
    print("Downloaded")

#Example
downloadImage("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQl5X3hLq__uUkt6uhJVajsP-F2U8IZ-0WumS12BdOIa4he91HcJnW1cA")

