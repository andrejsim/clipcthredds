# crawl local direcory for drs
import netCDF4
from os import walk

# author: Andrej

##
## SKETCH/ VALIDATE AT WRK...

# doc for specs...

def returnDRS(nc):
		nc_fid = netCDF4.Dataset( nc ,'r')
		
		#
		activ = "clipc"
		produ = 'rcm-derived'
		package = nc_fid.getncattr("software")
		domai = nc_fid.getncattr("domain")
		institution = nc_fid.getncattr("institute_id")
		model = nc_fid.getncattr("model")
		exper = nc_fid.getncattr("experiment")
		ensem = nc_fid.getncattr("ensemble")
		frequ = nc_fid.getncattr("frequency")
		varia = nc_fid.getncattr("variable")
		#
		dir_drs =""
		dir_drs.append(activ)
		dir_drs.append(produ)
		dir_drs.append(package)
		dir_drs.append(domai)
		dir_drs.append(institution)
		dir_drs.append(model)
		dir_drs.append(exper)
		dir_drs.append(ensem)
		dir_drs.append(frequ)
		dir_drs.append(varia)
		#
		# <VariableName>_<package>_<institution>_<model>_<CMIP5ExperimentName>_<CMIP5Ensemble
		# Member>[-IndicatorRealisation][_<RCMModelName>_<RCMVersionID>_<domain>]_
		# <Frequency>_<StartTime-EndTime>[--<reference_period>][_tile-nnnnn].nc

		# <VariableName>_<package>_<institution>_<model>_<CMIP5ExperimentName>_<CMIP5EnsembleMember>[-IndicatorRealisation][_<RCMModelName>_<RCMVersionID>_<domain>]_<Frequency>_<StartTime-EndTime>[--<reference_period>][_tile-nnnnn].nc
		file_drs = varia+"_"+package+"_"+institution+"_"+model

		return (dir_drs , file_drs)

# walk local
for direcory , b , ncs in walk(""):
	print directory, " ",b," ",ncs

	for nc in ncs:
		print returnDRS(nc)		