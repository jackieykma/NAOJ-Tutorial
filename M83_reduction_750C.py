##################################################
### Data reduction script for M83 (ATCA, 750C) ###
###         by Haruka Sakemi 2024/01/06        ###
##################################################

msfile = 'm83_750C.ms'
prical = '1934-638'
gcal = '1336-260'
refant = 'CA04'



### Examining and Editing the Data ###
importatca(vis=msfile, files=['2018-09-20_2203.C3248', '2018-09-21_0132.C3248', '2018-09-21_0501.C3248', '2018-09-21_0830.C3248'], options='birdie,noac')
listobs(vis=msfile, verbose=False)
listobs(vis=msfile, listfile='m83_750C_listobs.txt')
#plotms(vis=msfile, xaxis='time', yaxis='amp', coloraxis='field', iteraxis='spw', avgtime='1800', gridcols=2, plotfile='plotms_m83_750C_init_amp-time.png')
#plotms(vis=msfile, xaxis='freq', yaxis='amp', coloraxis='field', avgtime='1800', plotfile='plotms_m83_750C_init_amp-freq.png')
flagdata(vis=msfile, mode='manual', field='10', correlation='XY,YX', spw='0:87~137;320;519~639;832', antenna='CA02&CA04; CA02&CA05; CA04&CA05')
flagdata(vis=msfile, mode='manual', field='10', spw='1:1352~1361;1365~1366;1371;1377;1383~1398')
flagdata(vis=msfile, mode='tfcrop', field='0~9', usewindowstats='sum', halfwin=3)
flagdata(vis=msfile, mode='tfcrop', field='0~9', usewindowstats='sum', halfwin=3)
flagdata(vis=msfile, mode='manual', spw='0', antenna='CA04&CA05')
flagdata(vis=msfile, mode='manual', spw='0:80~140;520~640')
#plotms(vis=msfile, xaxis='time', yaxis='amp', coloraxis='field', iteraxis='spw', avgtime='1800', gridcols=2, plotfile='plotms_m83_750C_afterflag_amp-time.png')
#plotms(vis=msfile, xaxis='freq', yaxis='amp', coloraxis='field', avgtime='1800', plotfile='plotms_m83_750C_afterflag_amp-freq.png')



### Calibrating the Data ###
setjy(vis=msfile, field=prical, scalebychan=True, standard='Perley-Butler 2010')
gaincal(vis=msfile, caltable='cal.750C.G0', field=prical, refant=refant, gaintype='G', calmode='p', parang=True, solint='60s')
bandpass(vis=msfile, caltable='cal.750C.B0', field=prical, spw='', refant=refant, solnorm=True, solint='inf', bandtype='B', gaintable=['cal.750C.G0'], parang=True)
gaincal(vis=msfile, caltable='cal.750C.G1', field=prical+','+gcal, refant=refant, spw='*', gaintype='G', calmode='ap', parang=True, solint='60s', gaintable=['cal.750C.B0'])
polcal(vis=msfile, caltable='cal.750C.D0', field=prical, refant=refant, gaintable=['cal.750C.B0','cal.750C.G1'], poltype='D', solint='inf')
fluxscale(vis=msfile, caltable='cal.750C.G1', fluxtable='cal.750C.F0', reference=prical)
applycal(vis=msfile, gaintable=['cal.750C.B0','cal.750C.D0','cal.750C.F0'], gainfield=[prical,prical,gcal], parang=True)



### Produce new MS file with M83 only ###
split(vis=msfile,outputvis="m83_750C_target.ms/",field="1~9")



### Running shallow, interactive CLEAN-ing ###
### Run this during the Tutorial session ###
tclean(vis='m83_750C_target.ms', imagename='m83_750C_shallow_mfs', spw='0:0~512', threshold='1.0mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='I', specmode='mfs', gridder='mosaic', deconvolver='multiscale', scales=[0,4,12], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=True, niter=250, phasecenter='J2000 13h37m00 -29d51m54', usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, growiterations=75, negativethreshold=0.0, verbose=True)
impbcor(imagename='m83_750C_shallow_mfs.image', pbimage='m83_750C_shallow_mfs.pb', outfile='m83_750C_shallow_mfs.pbcor.image', cutoff=0.05)



'''
Commands below may take some time
Can be seen as "homework" to do after tutorial
Consider running this within "screen"
'''

### Imaging: Stokes I MFS for SPW0 (4.5-6.5 GHz) ###
### This will probably take over an hour ###
#tclean(vis='m83_750C_target.ms', imagename='m83_750C_spw0_mfs', spw='0', threshold='0.4mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='I', specmode='mfs', gridder='mosaic', deconvolver='multiscale', scales=[0,4,12,36], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=False, niter=50000, savemodel='modelcolumn', phasecenter='J2000 13h37m00 -29d51m54', usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, growiterations=75, negativethreshold=0.0, verbose=True)
#impbcor(imagename='m83_750C_spw0_mfs.image', pbimage='m83_750C_spw0_mfs.pb', outfile='m83_750C_spw0_mfs.pbcor.image', cutoff=0.05)

### Imaging: IQU cube for SPW0 (4.5-6.5 GHz; 128 MHz channels) ###
### Each Stokes parameter will likely take over an hour ###
#tclean(vis='m83_750C_target.ms', imagename='m83_750C_spw0_cube.I', spw='0', threshold='1.5mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='I', specmode='cube', width=128, gridder='mosaic', deconvolver='multiscale', scales=[0,4,12,36], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=False, niter=50000, phasecenter='J2000 13h37m00 -29d51m54', usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, negativethreshold=0.0, verbose=True)
#impbcor(imagename='m83_750C_spw0_cube.I.image', pbimage='m83_750C_spw0_cube.I.pb', outfile='m83_750C_spw0_cube.I.pbcor.image')

#tclean(vis='m83_750C_target.ms', imagename='m83_750C_spw0_cube.Q', spw='0', threshold='1.5mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='Q', specmode='cube', width=128, gridder='mosaic', deconvolver='multiscale', scales=[0,4,12,36], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=False, niter=50000, phasecenter='J2000 13h37m00 -29d51m54', usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, negativethreshold=0.0, verbose=True)
#impbcor(imagename='m83_750C_spw0_cube.Q.image', pbimage='m83_750C_spw0_cube.Q.pb', outfile='m83_750C_spw0_cube.Q.pbcor.image')

#tclean(vis='m83_750C_target.ms', imagename='m83_750C_spw0_cube.U', spw='0', threshold='1.5mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='U', specmode='cube', width=128, gridder='mosaic', deconvolver='multiscale', scales=[0,4,12,36], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=False, niter=50000, phasecenter='J2000 13h37m00 -29d51m54', usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, negativethreshold=0.0, verbose=True)
#impbcor(imagename='m83_750C_spw0_cube.U.image', pbimage='m83_750C_spw0_cube.U.pb', outfile='m83_750C_spw0_cube.U.pbcor.image')






