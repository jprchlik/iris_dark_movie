from astropy.io import fits
import glob
from datetime import datetime,timedelta
import numpy as np



class dark_data:


    def __init__(self,start='2012/01/01',end='3001/01/01',
                 lev1dir='/data/alisdair/IRIS_LEVEL1_DARKS/',
                 lev0dir='/data/alisdair/opabina/scratch/joan/iris/newdat/orbit/level0/',
                 typed='simpleB',clobber=False):


        start,end = start.split('/'),end.split('/')

        self.start = datetime(int(start[0]),int(start[1]),int(start[2]))
        self.end   = datetime(int(end[0]  ),int(end[1]  ),int(end[2]  ))

        self.typed = typed
        self.lev1dir = lev1dir
        self.lev0dir = lev0dir+self.typed+'/'
  

        self.get_subdirectories()
        self.cut_subdir_range()
        self.get_file_list()


    def get_subdirectories(self):
        yeard = glob.glob(self.lev0dir+'*')
        monthd = [glob.glob(i+'/*') for i in yeard]

#make the array 1d
        monthd = np.ravel(monthd)

        self.lev1mons = []
        self.lev0mons = []
        self.darktime = []
#create subdirectory list
        for j in monthd:
            for i in j:
                self.lev1mons.append(i.replace(self.lev0dir,self.lev1dir)+'/'+self.typed)
                self.lev0mons.append(i+'/')
                self.darktime.append(datetime(int(i.split('/')[-2]),int(i.split('/')[-1]),1))

#Only keep subdirectories in a specific range
    def cut_subdir_range(self):

        self.darktime = np.array(self.darktime)
        self.lev1mons = np.array(self.lev1mons)
        self.lev0mons = np.array(self.lev0mons)

        keep, = np.where((self.darktime >= self.start) & (self.darktime <= self.end))

        self.darktime = self.darktime[keep]
        self.lev1mons = self.lev1mons[keep]
        self.lev0mons = self.lev0mons[keep]
   
        

#get a list of file to analyze 
    def get_file_list(self):

        self.lev0fil = []
        self.lev1fil = []
        for i,j in enumerate(self.lev0mons):
            k = self.lev1mons[i]

            for p in glob.glob(j+'/*fits'): self.lev0fil.append(p)
            for p in glob.glob(k+'/*fits'): self.lev1fil.append(p)


