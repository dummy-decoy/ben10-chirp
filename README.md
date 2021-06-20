# Ben10 Omnitrix Omni-Link chirp generator

## The Omnitrix
Ben10 Omnitrix is an interactive toy which reacts to some sounds embedded inside the soundtrack of the comic series. 

## usage

### generator

The `generator.py` script generates a wave file for a given code.

Use python 3 to launch the generator.

```bash
> python3 generator.py 232012130112
```
The code to generate is specified as a base 4 integer. Length of the code is irrelevant, although currently known codes seem to be 12 digits long.
The generator will create a wav file in the current folder named after the code. The wav file is 48kHz 16 bit audio. 

### extractor

The `extractor.py` script will extracts the code from a given wave file.

```bash
> python3 extractor.py "\058 Wildmutt SE 15kHz.wav.wav"
```
