#!/usr/bin/env python3

import random
import generator

samplerate = 48000

def main():
    random.seed()
    code = '2'+str.join('',random.choices(('0','1','2','3'),k=7))+'1023'
    print('generating ben10-chirp for random code:', code)

    samples = generator.generate(code)
    data = generator.wavefile(samples, samplerate)
    generator.save(data.getbuffer(), code+'.wav')
    data.close()

if __name__ == '__main__':
    main()
