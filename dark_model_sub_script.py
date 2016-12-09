from dark_images import dark_files
import glob
from make_dark_images import dark_plot
from multiprocessing import Pool
from make_movie import create_movie

def run_images(ifile):
    
    out =dark_plot(ifile,clobber=True,itype=itype,vmin=-5,vmax=5,pdir='model_sub_plots/')
    if out.process:
        return out.ofile
    else:
        return

itypes = ['NUV','FUV']
ddir = '/Volumes/Pegasus/jprchlik/iris/find_con_darks/calc_trend_darks/fits_files'

nproc = 8

for itype in itypes:
   # darks = dark_files()
    fdark = glob.glob(ddir+'/'+itype+'*.fits')
    
    #fdark = darks.lev0fil#[-88:]
    
    pool = Pool(processes=nproc)
    ofiles = pool.map(run_images,fdark)
    pool.close()
    
    
    
    #ofiles = run_images(fdark)
    
    
    imov = create_movie(ofiles,outmov=itype+'_dark_model_sub_movie.mp4',w0=4144,h0=1096)
    imov.create_movie()
