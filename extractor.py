#!/usr/bin/env python3

import sys
import math
import struct
import wave

framerate = 24
brk = ' '
car = 'c'
symbols = ('0','1',car,'2','3')
tones = (14000,14500,15000,15500,16000)
binwidth = 500

def dft_term(signal, samplerate, frequency):
    return abs(sum(sample*(math.e**complex(0,-2*math.pi*index/samplerate*frequency)) for index,sample in enumerate(signal)))/(len(signal)/2)

def detector(signal, samplerate):
    code = ''
    length = int(samplerate/binwidth)
    for offset in range(0,len(signal)-length,length):
        slice = signal[offset:offset+length]
        response = list(dft_term(slice, samplerate, frequency) for frequency in tones)
        code += symbols[response.index(max(response))] if max(response)>0.3 else brk
    return code

def filter(code):
    filtered = ''
    last = brk
    previous = brk
    count = 0
    for char in code+brk:
        if char == previous:
            count += 1
        else:
            if count > (binwidth/framerate*0.5):
                if (last==brk) and (previous==car):
                    pass
                elif (last==car) and (previous==brk):
                    filtered += brk
                elif (last==car) and (previous in symbols):
                    pass
                elif (last != car) and (last in symbols) and (previous == car):
                    filtered += last
                else:
                    filtered = ''
                last = previous
            count = 1
        previous = char
    return filtered

def getsignal(data, sampwidth, channels):
    samples = list(struct.unpack(['<B','<h'][sampwidth-1], data[index:index+sampwidth])[0] for index in range(0,len(data),sampwidth))
    return list((sample-128)/128.0 if sampwidth==1 else sample/32768.0 for sample in samples)[::channels]

def main():
    input = wave.open(sys.argv[1], 'rb')
    data = input.readframes(input.getnframes())
    signal = getsignal(data, input.getsampwidth(), input.getnchannels())
    code = detector(signal, input.getframerate())
    code = filter(code)
    print(code)

if __name__ == '__main__':
    main()
