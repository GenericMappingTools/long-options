"""
Construct a DataFrame that contains long-options information for each module.
"""
import string
import pandas as pd

# Setup arrays for modules, options, and common options
modules = ['basemap','batch','begin','blockmean','blockmedian','blockmode',
    'clear','clip','coast','colorbar','contour','dimfilter','docs','end',
    'events','figure','filter1d','fitcircle','gmt2kml','gmtbinstats',
    'gmtconnect','gmtconvert','gmtdefaults','gmtget','gmtinfo','gmtlogo',
    'gmtmath','gmtregress','gmtselect','gmtset','gmtsimplify','gmtspatial',
    'gmtsplit','gmtvector','gmtwhich','grd2cpt','grd2kml','grd2xyz','grdblend',
    'grdclip','grdcontour','grdconvert','grdcut','grdedit','grdfft','grdfill',
    'grdfilter','grdgdal','grdgradient','grdhisteq','grdimage','grdinfo',
    'grdinterpolate','grdlandmask','grdmask','grdmath','grdmix','grdpaste',
    'grdproject','grdsample','grdtrack','grdtrend','grdvector','grdview',
    'grdvolume','greenspline','histogram','image','inset','kml2gmt','legend',
    'makecpt','mapproject','mask','movie','nearneighbor','plot','plot3d',
    'project','psconvert','rose','sample1d','solar','spectrum1d','sph2grd',
    'sphdistance','sphinterpolate','sphtriangulate','subplot','surface',
    'ternary','text','trend1d','trend2d','triangulate','wiggle','xyz2grd',
    'earthtide','gpsgridder','gshhg','velo','img2grd','mgd77convert',
    'mgd77header','mgd77info','mgd77list','mgd77magref','mgd77manage',
    'mgd77path','mgd77sniffer','mgd77track','gmtflexure','gmtgravmag3d',
    'gravfft','grdflexure','grdgravmag3d','grdredpol','grdseamount','talwani2d',
    'talwani3d','segyz','segy','segy2grd','coupe','meca','polar','sac',
    'backtracker','gmtpmodeler','grdpmodeler','grdrotater','grdspotter',
    'hotspotter','originater','polespotter','rotconverter','rotsmoother',
    'x2sys_binlist','x2sys_cross','x2sys_datalist','x2sys_get','x2sys_init',
    'x2sys_list','x2sys_merge','x2sys_put','x2sys_report','x2sys_solve',
]
options = ['module_options','module_needs','module_common','module_other'] + list(string.ascii_uppercase) + list(string.ascii_lowercase) + ['bi','bp','Tm','Td']
common_options = ['B','J','R','U','V','X','Y','a','b','c','d','e','f','g','h','i','k','l','n','o','p','q','r','s','t','w','x']
option_info = ['long-option','directives','modifiers','modules']

# Construct a DataFrame with long-option information for each common option
common_df = pd.DataFrame()
for option in common_options:
    if option.islower() and option.upper() in common_options:
        continue
    file =  'common-options/' + option.lower() + '.json'
    common_df = common_df.append(pd.read_json(file, orient='index'))

# Construct a DataFrame with long-option information for each GMT modules
module_df = pd.DataFrame(columns=options)
for module in modules:
    file = 'modules/' + module + '.json'
    module_df = module_df.append(pd.read_json(file, orient='index'))