from dark_images import dark_files
from make_dark_images import dark_plot
from multiprocessing import Pool
from make_movie import create_movie

itype = 'NUV'
def run_images(ifile):

    out =dark_plot(ifile,clobber=False,itype=itype,restrict=['EXPTIME:0'])
    
    return out.ofile


darks = dark_files()

nproc = 8

fdark = darks.lev0fil

pool = Pool(processes=nproc)
ofiles = pool.map(run_images,fdark)
pool.close()



#ofiles = run_images(fdark)


imov = create_movie(ofiles,outmov=itype+'_dark_movie.mp4')
imov.create_movie()
