# Ben10 Omnitrix Omni-Link chirp generator

## The Omnitrix
Ben10 Omnitrix is an interactive toy which reacts to some sounds embedded inside the soundtrack of the comic series. 

## usage

### generator

```bash
> python3 generator.py --help
Usage: generator.py [options] (code)+

generate waveforms corresponding to the given codes which trigger
actions on a ben10 omnitrix toy device.

code is a string of base 4 digit (0,1,2,3) of any length forming a 
code to generate. you can specify multiple codes, they will be either
played in sequence or saved individually as wave files. you can also
use a asterisk (*) as a wildcard for any digit of the code, the
generator will then generate multiple codes going through all posible
values for this digit.

Options:
  -h, --help            show this help message and exit
  -e, --export          export the generated waveforms as .wav file named
                        after each code into the current folder.
  -p, --play            play the generated waveforms on the default system
                        soundcard. each code is played one after the other,
                        with a pause inbetween each. the pause time is
                        controlled with the -t option. play is the default
                        action if none of play or export are specified.
  -t PAUSE, --pause=PAUSE
                        duration in seconds of the pause interval between each
                        waveform when playing. (default: 1 s)
  -s SAMPLERATE, --samplerate=SAMPLERATE
                        sample rate used for waveform generation.(default:
                        48000 hz)

```

### extractor

the `extractor.py` script will extracts the code from a given wave file.

```bash
> python3 extractor.py "058 Wildmutt SE 15kHz.wav.wav"
```

### generate-random

the `generate-random.py` script generates a random code starting with 2 and ending with 1023. this convention stems from the fact that every known code to date conform to this format. 
