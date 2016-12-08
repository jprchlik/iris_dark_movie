from astropy.io import fits
import glob
from datetime import datetime,timedelta
import numpy as np



class dark_data


    def __init__(self,start='2012/01/01',end='3001/01/01',
                 lev1dir='/data/alisdair/IRIS_LEVEL1_DARKS/',
                 lev0dir='data/alisdair/opabina/scratch/joan/iris/newdat/orbit/level0/',
                 typed='simpleB',clobber=False)

        start,end = start.split('/'),end.split('/')

        self.start = datetime(start[0],start[1],start[2])
        self.end   = datetime(end[0],end[1],end[2])

        self.lev1dir = lev1dir
        self.lev0dir = lev0dir
  
        self.typed = typed


    def get_subdirectorys(self):
        yeard = glob.glob(self.lev1dir)
        montd = [glob.glob(i) for i in yeard]

        self.lev1mons = []
        self.lev0mons = []
        self.darktime = []
#create subdirectory list
        for i in monthd:
            self.lev1mons.append(i+'/'+self.typed)
            self.lev0mons.append(i.replace(self.lev1dir,self.lev0dir)+'/'+self.typed))
            self.darktime.append(datetime(int(i.split('/')[-2]),int(i.split('/')[-1]),1))

#Only keep subdirectories in a specific range
    def cut_subdir_range(self):

        keep, = np.where((self.darktime >= self.start) & (self.darktime <= self.end))

        self.darktime = np.array(self.darktime)[keep]
        self.lev1mons = np.array(self.lev1mons)[keep]
        self.lev0mons = np.array(self.lev0mons)[keep]
   
        

#get a list of file to analyze 
    def get_file_list(self):

        self.lev0fil = []
        self.lev1fil = []
        for i,j enumerate(self.lev0mons):
            k = self.lev1mons[i]


