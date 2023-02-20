import xmltodict
 
with open('xml_data.txt') as xml_data:
    xml_parsed = xmltodict.parse(xml_data.read())
 
print(xml_parsed)
print()
print(xml_parsed['root'])
print()
print(xml_parsed['root']['Routers'])
print()
print(xml_parsed['root']['Routers'][0])