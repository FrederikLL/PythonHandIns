import bs4
import requests

r = requests.get("https://www.dr.dk/nyheder/tema/coronavirus")

r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

elems = soup.select('div a span span')

for elem in elems:
    print (elem.getText())

print("Number of articles {ele}".format(ele = len(elems)))
#print(len(elems))

#print(soup.prettify())
#print('1: return type of select()',type(elems))
#print('2: length of the returned list',len(elems))
#print('3: type of elements in the list',type(elems[0]))
#print('4: get text from the element',elems[0].getText()[:40])
#print('5: string representation of an element: ',str(elems[0]))
#print('6: the attributes of the element: ',elems[0].attrs)

#print(str(elems))
#print(elems.get('id'))
#print('4: get text from the element',elems[0].getText()[:40])
#print(span_elem.get('some_nonexistent_addr') == None)
#print(elems.attrs)