#!/usr/bin/env python3

import struct
import wave

import random
import generator

samplerate = 48000

def main():
    code = '2'+str.join('',random.choices(('0','1','2','3'),k=7))+'1023'
    print('generating ben10-chirp for random code:', code)
    samples = generator.generate(code)

    generator.export(code+'.wav', samples, generator.samplerate)

if __name__ == '__main__':
    main()
