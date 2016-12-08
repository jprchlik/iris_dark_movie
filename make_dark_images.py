import matplotlib
matplotlib.rc('font',size=24)
matplotlib.use('agg')
from astropy.io import fits
import os
import matplotlib.pyplot as plt
import numpy as np



class dark_plot:

    def __init__(self,ifile,pdir='dark_plots/',scale=1,restrict=['EXPTIME:0'],itype='NUV',ext='png',clobber=False):


        if pdir[-1] != '/': pdir = pdir+'/'


        self.ifile = ifile
        self.pdir = pdir
        self.scale = scale
        self.itype = itype
        self.ext = ext
        self.clobber =clobber

#output file
        fname = ifile.split('/')[-1]
        self.ofile = self.pdir+fname.replace('fits',ext)

        

#Whether to create the image or not
        self.process = False

        self.resdict = {}
        for i in restrict:
            split = i.split(':')
            
            self.resdict[split[0]] = split[1]

        self.fits = fits.open(ifile)[0]

        self.check_restrict()
        

        if self.process:
            self.plot_dark()
        else:
            print "FAILED"


    def check_restrict(self):

        if self.clobber == False:
            if os.path.isfile(self.ofile) == False: self.process = True
        else:
            self.process = True

        if self.process:
       
            for i in self.resdict.keys():
                print self.fits.header[i],float(self.resdict[i])
                if self.fits.header[i] ==  float(self.resdict[i]):
                    self.process = True 
                else:
                    self.process = False
                    continue
    
            

    def plot_dark(self):

        self.create_figure()

        self.ax.imshow(self.fits.data,
                       vmax=self.vmax,vmin=self.vmin,
                       cmap=plt.cm.gray)

        self.save_figure()


    def create_figure(self):

        self.dpi = self.scale*100.
        self.x,self.y = self.fits.header['NAXIS1']/self.dpi,self.fits.header['NAXIS2']/self.dpi
        
        self.fig, self.ax = plt.subplots(figsize=(self.x,self.y),dpi=self.dpi)

        self.vmin,self.vmax = self.fits.header['DATAMEAN']+3.*self.fits.header['DATARMS']*np.array([-1.,1.])

        #set sun to fill entire range
        self.fig.subplots_adjust(left=0,bottom=0,right=1,top=1)
    #Turn off axis
        self.ax.set_axis_off()
        

    def save_figure(self):
        self.fig.savefig(self.ofile)
        self.fig.clear()
        plt.close()

    
