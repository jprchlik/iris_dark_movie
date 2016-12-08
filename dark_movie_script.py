from dark_images import dark_files
from make_dark_images import dark_plot
from multiprocessing import Pool
from make_movie import create_movie

itype = 'NUV'
def run_images(ifile):

    out =dark_plot(ifile,clobber=True,itype=itype,vmin=90,vmax=125)
    
    if out.process:
        return out.ofile
    else:
        return


darks = dark_files()

nproc = 8

fdark = darks.lev0fil#[-88:]

pool = Pool(processes=nproc)
ofiles = pool.map(run_images,fdark)
pool.close()



#ofiles = run_images(fdark)


imov = create_movie(ofiles,outmov=itype+'_dark_movie.mp4',w0=4144,h0=1096)
imov.create_movie()
