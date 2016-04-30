import thredds

netcdf_files = []
server = "http://opendap.knmi.nl/knmi/thredds/catalog/"
thredds.listThredds(server ,"CLIPC/cerfacs/", "catalog.xml", netcdf_files)

for n in netcdf_files:
	print server+n
