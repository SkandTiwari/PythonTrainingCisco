import xml.dom.minidom

domtree = xml.dom.minidom.parse(r"C:\Users\sktiwari\OneDrive - Cisco\Desktop\Python Training\xml_processing\xml_data.xml")

group = domtree.documentElement

books = group.getElementsByTagName('book')

for book in books:
    print(f"-- Book : {books.getAttribute('id')}--")