import sys
sys.path.append('../../sms-tools/software/models/')
import essentia.standard as es
import matplotlib.pyplot as plt
import numpy as np
import os

destinationPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'finalSounds/')
inputPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'inputSounds/')

def func():
        for file in os.listdir("."):
                if file.endswith(".wav"):
                        (fs, x) = wavread(file)
                        print file
                        print fs
		
			filename = file.split('.')[0]
	



func()
