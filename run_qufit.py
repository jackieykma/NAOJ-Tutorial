import os



'''
Running for source 1: NVSS J183847-040042
'''
os.system('qufit J183847-040042.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('qufit J183847-040042.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
#os.system('qufit J183847-040042.dat -m 11 --sampler nestle --ncores 4 --nlive 128') ## This one can take a very long time; skipping

'''
Running for source 2: NVSS J184432+064257
'''
os.system('qufit J184432+064257.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('qufit J184432+064257.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
#os.system('qufit J184432+064257.dat -m 11 --sampler nestle --ncores 4 --nlive 128') ## This one can take a very long time; skipping

'''
Running for source 3: NVSS J190559+000721
'''
os.system('qufit J190559+000721.dat -m 1 --sampler nestle --ncores 4 --nlive 128')
os.system('qufit J190559+000721.dat -m 2 --sampler nestle --ncores 4 --nlive 128')
os.system('qufit J190559+000721.dat -m 11 --sampler nestle --ncores 4 --nlive 128')







