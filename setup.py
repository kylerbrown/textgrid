from setuptools import setup

setup(name='textgrid',
      version='0.2',
      description='tools for reading and converting textgrid files',
      url='http://github.com/kylerbrown/textgrid',
      author='Kyler Brown',
      author_email='kylerjbrown@gmail.com',
      license='MIT',
      py_modules=["textgrid"],
      entry_points= {
          'console_scripts' : [
              'textgrid2csv = textgrid:textgrid2csv',
              ]
          },
      zip_safe=False)
