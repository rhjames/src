import xml.etree.cElementTree as ET
import urllib2

tree = ET.parse("country_data.xml")
root = tree.getroot()


#for country in root.findall('country'):
#	rank = country.find('rank').text
#	name = country.get('name')
#	gdp = country.find('gdppc').text
#	print(name, rank, gdp)

for i in range(3):
	tree = ET.ElementTree(file=urllib2.urlopen('http://stackoverflow.com/questions/21483959/how-can-get-usdjpycurrency-rates-with-pandas-and-yahoo-finance'))

	root = tree.getroot()
	root.tag, root.attrib