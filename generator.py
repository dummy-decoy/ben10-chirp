#!/usr/bin/env python3

import sys
import math
import struct
import wave

samplerate = 48000
framerate = 24
carrier = 15000
symbols = (14000,14500,15500,16000)

def tone(frequency):
    samples = list(math.sin((tone.phase+n*1/samplerate*frequency)*2*math.pi) for n in range(int(1/framerate*samplerate)))
    tone.phase += len(samples)*1/samplerate*frequency
    return samples
tone.phase = 0.0

def generate(code):
    result = list()
    result.extend(tone(carrier))
    for char in code:
        result.extend(tone(symbols[int(char,4)]))
        result.extend(tone(carrier))
    return result

def export(filename, signal, samplerate):
    data = bytes.join(b'', (struct.pack('<h',int(sample*32767)) for sample in signal))
    output = wave.open(filename, 'wb')
    output.setparams((1,2,samplerate,0,'NONE',''))
    output.writeframes(data)
    output.close()

def main():
    code = sys.argv[1]
    print('generating ben10-chirp for code:', code)

    samples = generate(code)
    export(code+'.wav', samples, samplerate)
   

if __name__ == '__main__':
    main()
