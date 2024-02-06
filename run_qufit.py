import os



## Type in the full path to <do_QUfit_1D_mnest.py>
qu_fit_path = '/priv/avatar/ykma/my_script/RM-Tools/RMtools_1D/do_QUfit_1D_mnest.py'



os.system('python3 '+qu_fit_path+' J183847-040042.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('python3 '+qu_fit_path+' J183847-040042.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
#os.system('python3 '+qu_fit_path+' J183847-040042.dat -m 11 --sampler nestle --ncores 4 --nlive 128') ## This one can take a very long time
os.system('python3 '+qu_fit_path+' J184432+064257.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('python3 '+qu_fit_path+' J184432+064257.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
#os.system('python3 '+qu_fit_path+' J184432+064257.dat -m 11 --sampler nestle --ncores 4 --nlive 128') ## This one can take a very long time
os.system('python3 '+qu_fit_path+' J190559+000721.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('python3 '+qu_fit_path+' J190559+000721.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
os.system('python3 '+qu_fit_path+' J190559+000721.dat -m 11 --sampler nestle --ncores 4 --nlive 128')







