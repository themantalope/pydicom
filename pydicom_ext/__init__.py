# Copyright 2008-2018 pydicom_ext authors. See LICENSE file for details.
"""pydicom_ext package -- easily handle DICOM files.
   See Quick Start below.

-----------
Quick Start
-----------

1. A simple program to read a dicom file, modify a value, and write to a new
   file::

    from pydicom_ext.filereader import dcmread
    dataset = dcmread("file1.dcm")
    dataset.PatientName = 'anonymous'
    dataset.save_as("file2.dcm")

2. See the files in the examples directory that came with this package for more
   examples, including some interactive sessions.

3. Learn the methods of the Dataset class; that is the one you will work with
   most directly.

4. Questions and comments can be directed to the pydicom_ext google group:
   http://groups.google.com/group/pydicom_ext

5. Bugs and other issues can be reported in the issue tracker:
   https://www.github.com/pydicom_ext/pydicom_ext

"""


from pydicom_ext.dataelem import DataElement
from pydicom_ext.dataset import Dataset, FileDataset
from pydicom_ext.filereader import dcmread, read_file
from pydicom_ext.filewriter import dcmwrite, write_file
from pydicom_ext.sequence import Sequence

from ._version import __version__, __version_info__

__all__ = ['DataElement',
           'Dataset',
           'FileDataset',
           'Sequence',
           'dcmread',
           'dcmwrite',
           'read_file',
           'write_file',
           '__version__',
           '__version_info__']

from pydicom_ext.compat import in_py2
if in_py2:
    import warnings
    msg = 'Python 2 will no longer be supported after the pydicom_ext v1.4 release'
    warnings.warn(msg, DeprecationWarning)
