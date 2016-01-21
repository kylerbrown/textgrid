#!/usr/bin/python

from collections import namedtuple

Entry = namedtuple("Entry", ["start",
                             "stop",
                             "label"])

def read_textgrid(filename):
    """
    Reads a TextGrid file into a dictionary object
    ONLY includes a flat list of dictionaries.
    each dictionary has the following keys:
    "start"
    "stop"
    "label"

    **** "class" labels are discarded ****
    Points use the same format, but the value for "start" and "stop" are the same
    """
    if isinstance(filename, str):
        with open(filename, "r") as f:
            content = _read(f)
    elif hasattr(filename, "readlines"):
        content = _read(filename)
    else:
        raise TypeError("filename must be a string or a readable buffer")

    interval_lines = [i for i, line in enumerate(content)
                      if line.startswith("intervals [")
                      or line.startswith("points [")]
    return [_build_entry(i, content) for i in interval_lines]


def _read(f):
    return [x.strip() for x in f.readlines()]

def write_csv(textgrid_list, filename=None, sep=",", header=True):
    """
    Writes a list of textgrid dictionaries to a csv file.
    If no filename is specified, csv is printed to standard out.
    """
    columns = list(Entry._fields)
    if filename:
        f = open(filename, "w")
    if header:
        hline = sep.join(columns)
        if filename:
            f.write(hline + "\n")
        else:
            print(hline)
    for entry in textgrid_list:
        if entry.label:  # skip unlabeled intervals
            row = sep.join(str(x) for x in list(entry))
            if filename:
                f.write(row + "\n")
            else:
                print(row)
    if filename:
        f.flush()
        f.close()

def _build_entry(i, content):
    """
    takes the ith line that begin an interval and returns
    a dictionary of values
    """
    start = _get_float_val(content[i + 1])  # addition is cheap typechecking
    if content[i].startswith("intervals ["):
        offset = 1
    else:
        offset = 0 # for "point" objects
    stop = _get_float_val(content[i + 1 + offset])
    label = _get_str_val(content[i + 2 + offset])
    return Entry(start=start, stop=stop, label=label)


def _get_float_val(string):
    """
    returns the last word in a string as a float
    """
    return float(string.split()[-1])


def _get_str_val(string):
    """
    returns the last item in quotes from a string
    """
    return string.split('"')[-2]


def main(textgridfile, outputfile=None, sep=",", header=True):
    tgrid = read_textgrid(textgridfile)
    write_csv(tgrid, outputfile, sep, header)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="convert a TextGrid file to a CSV.")
    parser.add_argument("TextGrid",
                        help="a TextGrid file to process")
    parser.add_argument("-o", "--output", help="(optional) outputfile")
    parser.add_argument("--sep", help="separator to use in CSV output",
                        default=",")
    parser.add_argument("--header", help="adds a header to the CSV",
                        action="store_true")
    args = parser.parse_args()
    main(args.TextGrid, args.output, args.sep, args.header)
