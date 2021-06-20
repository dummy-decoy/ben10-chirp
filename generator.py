#!/usr/bin/env python3

import sys
import math
import struct
import wave
import winsound
import io
import optparse
import time


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

def wavefile(signal, samplerate):
    file = io.BytesIO()
    data = bytes.join(b'', (struct.pack('<h',int(sample*32767)) for sample in signal))
    output = wave.open(file, 'wb')
    output.setparams((1,2,samplerate,0,'NONE',''))
    output.writeframes(data)
    output.close()
    return file

def play(data):
    winsound.PlaySound(data, winsound.SND_MEMORY)

def save(data, filename):
    file = open(filename, 'wb')
    file.write(data)
    file.close()

def getcodes(code, prefix=''):
    generated = prefix[:]
    if len(code)==0:
        yield prefix
    elif code[0] in ('0','1','2','3'):
        generated += code[0]
        yield from getcodes(code[1:], generated)
    elif code[0] == '*':
        for wildcard in ('0','1','2','3'):
            generated += wildcard
            yield from getcodes(code[1:], generated)
            generated = generated[:-1]
    else:
        raise ValueError('invalid character in code: '+code[0]+'. allowed characters are \'0\',\'1\',\'2\',\'3\' and \'*\'')

def main():
    parser = optparse.OptionParser('usage: %prog [options] (code)+ \n\ngenerate waveforms corresponding to the given codes which trigger actions on a ben10 omnitrix toy device.\n\ncode is a string of base 4 digit (0,1,2,3) of any length forming a code to generate. you can specify multiple codes, they will be either played in sequence or saved individually as wave files. you can also use a asterisk (*) as a wildcard for any digit of the code, the generator will then generate multiple codes going through all posible values for this digit.')
    parser.add_option('-e', '--export',     dest='export',     action='store_true', default=False, help='export the generated waveforms as .wav file named after each code into the current folder.')
    parser.add_option('-p', '--play',       dest='play',       action='store_true', default=False, help='play the generated waveforms on the default system soundcard. each code is played one after the other, with a pause inbetween each. the pause time is controlled with the -t option. play is the default action if none of play or export are specified.')
    parser.add_option('-t', '--pause',      dest='pause',      type='int',          default=1,     help='duration in seconds of the pause interval between each waveform when playing. (default: %default s)')   
    parser.add_option('-s', '--samplerate', dest='samplerate', type='int',          default=48000, help='sample rate used for waveform generation.(default: %default hz)') 
    (options, args) = parser.parse_args()

    global samplerate
    samplerate = options.samplerate

    for arg in args:
        for code in getcodes(arg):
            print('generating ben10-chirp code:', code)
            samples = generate(code)
            data = wavefile(samples, samplerate)
            if options.export:
                save(data.getbuffer(), code+'.wav')
            if options.play or (not options.play and not options.export):
                play(data.getbuffer())
                time.sleep(options.pause)
            data.close()

if __name__ == '__main__':
    main()
