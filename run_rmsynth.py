import os



'''
Running for source 1: NVSS J183847-040042
'''
os.system('rmsynth1d J183847-040042.dat -l 1000 -d 5 -S')
os.system('rmclean1d J183847-040042.dat -c -6 -n 1000 -g 0.1 -S')



'''
Running for source 2: NVSS J184432+064257
'''
os.system('rmsynth1d J184432+064257.dat -l 1000 -d 5 -S')
os.system('rmclean1d J184432+064257.dat -c -6 -n 1000 -g 0.1 -S')



'''
Running for source 3: NVSS J190559+000721
'''
os.system('rmsynth1d J190559+000721.dat -l 1000 -d 5 -S')
os.system('rmclean1d J190559+000721.dat -c -6 -n 1000 -g 0.1 -S')






