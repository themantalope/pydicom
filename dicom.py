msg = """
pydicom_ext via 'import dicom' has been removed in pydicom_ext version 1.0.
Please install the `dicom` package to restore function of code relying
on pydicom_ext 0.9.9 or earlier. E.g. `pip install dicom`.
Alternatively, most code can easily be converted to pydicom_ext > 1.0 by
changing import lines from 'import dicom' to 'import pydicom_ext'.
See the Transition Guide at
https://pydicom_ext.github.io/pydicom_ext/stable/transition_to_pydicom_ext1.html.
"""

raise ImportError(msg)
