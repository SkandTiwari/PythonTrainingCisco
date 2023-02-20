"""  Basically, in python there are two ways to process XML data. Those are mainly

1) SAX
and
2) DOM """

import xml.sax

class Bookhandler(xml.sax.ContentHandler):

    
      

    def startElement(self, name, attrs):
        self.current = name
        if name == "book":
            print(f"<-- Book : {attrs['id']}-->")

    def characters(self, content):
        if self.current == "author":
            self.author = content
        
        elif self.current == "title":
            self.title = content

        elif self.current == "genre":
            self.genre = content

    def endElement(self, name):
        if self.current == "author":
            print(f"Author : {self.author}")
        elif self.current == "title":
            print(f"Title : {self.title}")
        elif self.current == "genre":
            print(f"Genre : {self.genre}")

handler = Bookhandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(r"C:\Users\sktiwari\OneDrive - Cisco\Desktop\Python Training\xml_processing\xml_data.xml")