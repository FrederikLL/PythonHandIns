import requests
import threading

class NotFoundException(Exception):
    
    def __init__(self, *args, **kwargs):
       Exception.__init__(self, *args, **kwargs)

class Ex6: #removed ()
    def __init__(self, url_list):
        self.url_list = url_list
        self.index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index == len(self.url_list):
            raise StopIteration
        return self.url_list[self.index]
    
    def download(self, url,filename):
        try:
            r = requests.get(url)
            with open(filename, 'wb') as fd:
                fd.write(r.content)
                if r.content == "404":
                    raise NotFoundException
        except NotFoundException:
            print("Failure to download error: 404!!")
        except Exception as e:
            print("Failure to download error: {}".format(e))
        else:
            print("File downloaded!")
            return filename
    
    def multi_download(self, url_list):
        filenames = []
        val = 1
        filename = "multibook{}.txt"
        for lst in url_list:
            threading.Thread(target=self.download, args=(lst,filename.format(val))).start()
            filenames.append(filename.format(val))
            val +=1
            
        return filenames
            

    def urlist_generator(self, url_list): #for filenames i guess and not urls?
        for i in url_list:
            yield i
        
    def avg_vowels(self, text):
        vowels = set("AEIOUaeiou") #not sure Y is a vowel read on wiki
        countV = 0
        infile=open(text, "r")
        testtext = infile.read()
        wordz = testtext.count(" ")
        #print(wordz) #data seems right
        for c in testtext:
            if c in vowels:
                countV+=1
                
        
        #print(countV) #data seemsright
        return countV/(wordz+1)
    
    def hardest_read(self):
        return 0

# booksarr = ['http://www.gutenberg.org/cache/epub/2542/pg2542.txt', 
# 'https://www.gutenberg.org/files/1342/1342-0.txt',
# 'https://www.gutenberg.org/files/2701/2701-0.txt']

#classex6 = Ex6(booksarr)

#classex6.download('https://www.gutenberg.org/files/2701/2701-0.txt','booktest.txt')
#classex6.multi_download(classex6.url_list)
#classex6.urlist_generator(classex6.multi_download(classex6.url_list))
#print(classex6.url_list)
# lol = iter(classex6)
# print(next(lol))
# print(next(lol))
# print(next(lol))




#print(classex6.avg_vowels("multibook1.txt"))