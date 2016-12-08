from dark_images import dark_files
from make_dark_images import dark_plot

def run_images(ifile):

    dark_plot(ifile,clobber=True)


darks = dark_files()

run_images(darks.lev0fil[-14])
