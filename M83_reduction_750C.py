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
plotms(vis=msfile, xaxis='time', yaxis='amp', coloraxis='field', iteraxis='spw', avgtime='1800', gridcols=2, plotfile='plotms_m83_750C_init_amp-time.png')
flagdata(vis=msfile, mode='manual', field='10', correlation='XY,YX', spw='0:87~137;320;519~639;832', antenna='CA02&CA04; CA02&CA05; CA04&CA05')
flagdata(vis=msfile, mode='manual', field='10', spw='1:1352~1361;1383~1398')
flagdata(vis=msfile, mode='tfcrop', field='0~9', usewindowstats='sum', halfwin=3)
flagdata(vis=msfile, mode='tfcrop', field='0~9', usewindowstats='sum', halfwin=3)
flagdata(vis=msfile, mode='manual', spw='0', antenna='CA04&CA05')
flagdata(vis=msfile, mode='manual', spw='0:80~140;520~640')

### Calibrating the Data ###
msfile_spw = msfile.replace('.ms', '.spw.ms')
mstransform(vis=msfile, outputvis=msfile_spw, datacolumn='data', mode='channel', regridms=True, spw='0,1', nspw=16)
setjy(vis=msfile_spw, field=prical, scalebychan=True, standard='Perley-Butler 2010')
gaincal(vis=msfile_spw, caltable='cal.G0', field=prical, refant=refant, gaintype='G', calmode='p', parang=True, solint='60s')
bandpass(vis=msfile_spw, caltable='cal.B0', field=prical, spw='', refant=refant, solnorm=True, solint='inf', bandtype='B', gaintable=['cal.G0'], parang=True)
gaincal(vis=msfile_spw, caltable='cal.G1', field=prical+','+gcal, refant=refant, spw='*', gaintype='G', calmode='ap', parang=True, solint='60s', gaintable=['cal.B0'])
polcal(vis=msfile_spw, caltable='cal.D0', field=prical, refant=refant, gaintable=['cal.B0','cal.G1'], poltype='D', solint='inf')
fluxscale(vis=msfile_spw, caltable='cal.G1', fluxtable='cal.F0', reference=prical)
applycal(vis=msfile_spw, gaintable=['cal.B0','cal.D0','cal.F0'], gainfield=[prical,prical,gcal], parang=True)


### Imaging ###
split(vis=msfile_spw,outputvis="m83_750C_target.ms/",field="1~9")
tclean(vis='m83_750C_target.ms', imagename='m83_750C_spw0', spw='0', threshold='0.4mJy', gain=0.1, imsize=450, cell='4.0arcsec', stokes='IQUV', specmode='cube', width='64MHz', gridder='mosaic', deconvolver='multiscale', scales=[0,4,12], smallscalebias=0.6, weighting='briggs', robust=0.5, interactive=True, niter=6000, savemodel='modelcolumn', phasecenter='J2000 13h37m00 -29d51m54',
usemask='auto-multithresh', sidelobethreshold=2.0, noisethreshold=4.25, lownoisethreshold=1.5, minbeamfrac=0.3, growiterations=75, negativethreshold=0.0, verbose=True)
#restart=True, calcres=False, calcpsf=False) 

