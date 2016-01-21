# textgrid.py

A simple TextGrid to CSV converter.

Tier labels are discarded, as are unnamed intervals and points. Points are treated as intervals with identical start and stop values.

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

Example ouput using `python textgrid.py example.TextGrid --header`

```
start,stop,label
0.0,5.537098932314087,z
```

## usage
    usage: textgrid.py [-h] [-o OUTPUT] [--sep SEP] [--header] TextGrid

    convert a TextGrid file to a CSV.

    positional arguments:
      TextGrid              a TextGrid file to process

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
	    					(optional) outputfile
      --sep SEP             separator to use in CSV output
      --header              adds a header to the CSV

## programmatic usage with Python and Pandas:
```
>>> import pandas as pd
>>> import textgrid
>>> tgrid = textgrid.read_textgrid("example.TextGrid")
>>> tgrid
[Entry(start=0.0, stop=5.537098932314087, label='z')]
>>> pd.DataFrame(tgrid)
   start      stop label
0      0  5.537099     z
>>> 
```
