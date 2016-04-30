# crawl 
# knmi thredds.
#
# author: andrej

###

#import netCDF4
#import collections
#from datetime import date

import urlparse
import urllib2
import xml.etree.ElementTree as ET
#import xml.dom.minidom
#import skos_nerc_cf_vocab
def readThredds(cat, cid ,ext):
	print cat+cid+ext
	req = urllib2.urlopen(cat+cid+ext)

	catXml = req.read()

	tree = ET.fromstring(catXml)

	#listLinks = tree.getiterator()
	#root = tree.getroot()
	#dataset = tree.find('/dataset')

	# cycle through data sets.
	dataset = tree.find('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset')
	dataset_id = dataset.get('ID')+"/"
		
	# ignor tcp directory with raw data
	if "storyline_urbanheat" not in dataset_id:
	#print tree.find('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset').tag #get("name")
		for d in tree.iter('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
			link = d.get("{http://www.w3.org/1999/xlink}href")
			d_id = d.get("ID")+"/"

			readThredds( cat, dataset_id ,link)


def listThredds(cat, cid ,ext,links=[]):
	#print cat+cid+ext
	req = urllib2.urlopen(cat+cid+ext)

	catXml = req.read()

	tree = ET.fromstring(catXml)

	# cycle through data sets.
	dataset = tree.find('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset')
	dataset_id = dataset.get('ID')+"/"

	#print dataset_id
	for nc in dataset.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset'):
		nc_file = nc.get("ID")
		#print nc_file
		links.append(nc_file)

	# ignor tcp directory with raw data
	if "storyline_urbanheat" not in dataset_id:
	#print tree.find('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset').tag #get("name")
		for d in tree.iter('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
			link = d.get("{http://www.w3.org/1999/xlink}href")
			d_id = d.get("ID")+"/"

			listThredds( cat, dataset_id ,link,links)

    #print tree.iterall('dataset')
	#print dataset

#readThredds("http://opendap.knmi.nl/knmi/thredds/catalog/","CLIPC/", "catalog.xml")
# netcdf_files = []
# listThredds("http://opendap.knmi.nl/knmi/thredds/catalog/","CLIPC/", "catalog.xml", netcdf_files)

# for n in netcdf_files:
# 	print n
