# textgrid

Version 0.2 

A minimal python TextGrid module and CSV converter.

Tier labels are saved as a column called "tier". Points are treated as intervals with identical start and stop values.

Example input:

```
File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0 
xmax = 4387.9766666666665 
tiers? <exists> 
size = 1
item []: 
    item [1]:
        class = "IntervalTier" 
        name = "Mary" 
        xmin = 0 
        xmax = 4387.9766666666665 
        intervals: size = 1
        intervals [1]:
            xmin = 0 
            xmax = 5.537098932314087 
            text = "z"
```

Example ouput using `textgrid2csv example.TextGrid`

```
start,stop,name,tier
0.0,5.537098932314087,z,Mary
```

## installation

    git clone https://github.com/kylerbrown/textgrid.git
    cd textgrid
    pip install .

    # optional testing (requires pytest)
    pytest -v

## usage

    usage: textgrid2csv [-h] [-o OUTPUT] [--sep SEP] [--noheader] [--savegaps]
                        TextGrid

    convert a TextGrid file to a CSV.

    positional arguments:
      TextGrid              a TextGrid file to process

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            (optional) outputfile
      --sep SEP             separator to use in CSV output
      --noheader            no header for the CSV
      --savegaps            preserves intervals with no label

## programmatic usage with Python and Pandas:
```
>>> import pandas as pd
>>> import textgrid
>>> tgrid = textgrid.read_textgrid("example.TextGrid")
>>> tgrid
[Entry(start=0.0, stop=5.537098932314087, name='z', tier='Mary')]
>>> pd.DataFrame(tgrid)
   start      stop name    tier
0      0  5.537099     z    Mary
>>> 
```
