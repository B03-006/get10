import pathlib //подсоседилась alryt
import shutil
import os
import requests

path = str(pathlib.Path().absolute())+'\\temperatures'
print(path)

try:
    shutil.rmtree(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print("Successfully deleted the directory %s" % path)

try: 
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else: 
    print("Successfully created the directory %s" % path)

#https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/0902/AQUA_MODIS.20200902.L3m.DAY.SST.sst.4km.NRT.nc.png
#https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/0902/AQUA_MODIS.20200902.L3m.DAY.SST.sst.9km.NRT.nc
#https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/year/date/AQUA_MODIS.yeardate.L3m.DAY.SST.sst.razr.NRT.nc.png

iconSize = {'4km': '4km', '9km': '9km'}
iconYear = '2020'
iconDate = [
    '0902',
    '0903',
    '0904',
    '0905',
    '0906',
    '0907',
    '0908',
    '0909',
    '0910',
    '0911',
    '0912',
    '0913',
    '0914',
    '0915'
]

    

for key in iconSize:
    sizePath = path + '\\' + key

    
    try: 
        os.mkdir(sizePath)
    except OSError:
        print("Creation of the directoty %s failed" % sizePath)
    else:
        print("Successfully created the directory %s " % sizePath)
    
    for n in iconDate:
        name = n
        #url = 'https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/' + iconYear + '/' + str(name) + '/AQUA_MODIS.' + iconYear + str(name) + '.L3m.DAY.SST.sst.' + iconSize[key] + '.NRT.nc.png'
        #print(url)
        r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/' + iconYear + '/' + str(name) + '/AQUA_MODIS.' + iconYear + str(name) + '.L3m.DAY.SST.sst.' + iconSize[key] + '.NRT.nc.png', allow_redirects=True)
        open(sizePath + '/' + str(name) + '.png', 'wb').write(r.content) 
        
