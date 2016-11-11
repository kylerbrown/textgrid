# py.test unit tests

from io import StringIO
import textgrid

example_file1 = StringIO("""File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0 
xmax = 4387.9766666666665 
tiers? <exists> 
size = 3 
item []: 
    item [1]:
        class = "IntervalTier" 
        name = "Mary" 
        xmin = 0 
        xmax = 4387.9766666666665 
        intervals: size = 4 
        intervals [1]:
            xmin = 0 
            xmax = 5.537098932314087 
            text = "" 
        intervals [2]:
            xmin = 5.537098932314087 
            xmax = 18.917761588532382 
            text = "bar" 
        intervals [3]:
            xmin = 18.917761588532382 
            xmax = 23.177071623244515 
            text = "" 
        intervals [4]:
            xmin = 23.177071623244515 
            xmax = 4387.9766666666665 
            text = "" 
    item [2]:
        class = "IntervalTier" 
        name = "John" 
        xmin = 0 
        xmax = 4387.9766666666665 
        intervals: size = 5 
        intervals [1]:
            xmin = 0 
            xmax = 1.4385175781571313 
            text = "" 
        intervals [2]:
            xmin = 1.4385175781571313 
            xmax = 3.9699942969011333 
            text = "pip" 
        intervals [3]:
            xmin = 3.9699942969011333 
            xmax = 5.537098932314087 
            text = "" 
        intervals [4]:
            xmin = 5.537098932314087 
            xmax = 8.711490373278787 
            text = "foo" 
        intervals [5]:
            xmin = 8.711490373278787 
            xmax = 4387.9766666666665 
            text = "" 
    item [3]:
        class = "TextTier" 
        name = "bell" 
        xmin = 0 
        xmax = 4387.9766666666665 
        points: size = 2 
        points [1]:
            number = 15.140637595485778 
            mark = "a" 
        points [2]:
            number = 21.248327456582416 
            mark = "cool" 
""")

example_file2 = StringIO("""File type = "ooTextFile"
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
""")
example_file3 = StringIO("""
    item [3]:
        class = "TextTier" 
        name = "bell" 
        xmin = 0 
        xmax = 4387.9766666666665 
        points: size = 2 
        points [1]:
            number = 15.140637595485778 
            mark = "a" 
        points [2]:
            number = 21.248327456582416 
            mark = "cool" 
        """)
def test_get_float_val():
    assert textgrid._get_float_val("foo 123") == 123
    assert textgrid._get_float_val("number = 21.248327456582416") == 21.248327456582416
    assert textgrid._get_float_val("xmax = 4387.9766666666665") == 4387.9766666666665
    assert textgrid._get_float_val("xmin = 5.537098932314087 \n") == 5.537098932314087 


def test_get_str_val():
    assert textgrid._get_str_val('mark = "cool" ') == "cool"
    assert textgrid._get_str_val('text = "pip"') == "pip"


def test_build_entry_point():
    content = ["points [1]:",
               "number = 15.140637595485778 ",
               'mark = "a"']
    entry = textgrid._build_entry(0, content, tier='testtier')
    assert entry.start == 15.140637595485778
    assert entry.stop == 15.140637595485778
    assert entry.label == "a"
    assert entry.tier == "testtier"

def test_build_entry_interval():
    content = ["intervals [4]:",
                "xmin = 5.537098932314087",
                "xmax = 8.711490373278787",
                'text = "foo"']
    entry = textgrid._build_entry(0, content, tier='testtier')
    assert entry.start == 5.537098932314087
    assert entry.stop == 8.711490373278787
    assert entry.label == "foo"


def test_points():
    tgrid = textgrid.read_textgrid(example_file3)
    assert len(tgrid) == 2

def test_read_short():
    tgrid = textgrid.read_textgrid(example_file2)
    assert len(tgrid) == 1
    entry = tgrid[0]
    assert entry.start == 0
    assert entry.stop == 5.537098932314087
    assert entry.label == "z"
    assert entry.tier == "Mary"

def test_read_long():
    tgrid = textgrid.read_textgrid(example_file1)
    assert len(tgrid) == 11
    entry = tgrid[0]
    assert entry.start == 0
    assert entry.stop == 5.537098932314087 
    assert entry.label == ""
    entry2 = tgrid[-1]
    assert entry2.label == "cool"
    assert entry2.tier == "bell"
