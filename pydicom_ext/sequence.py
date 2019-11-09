# Copyright 2008-2018 pydicom_ext authors. See LICENSE file for details.
"""Define the Sequence class, which contains a sequence DataElement's items.

Sequence is a list of pydicom_ext Dataset objects.
"""

from pydicom_ext.dataset import Dataset
from pydicom_ext.multival import MultiValue


def validate_dataset(elem):
    """Check that `elem` is a :class:`~pydicom_ext.dataset.Dataset` instance."""
    if not isinstance(elem, Dataset):
        raise TypeError('Sequence contents must be Dataset instances.')

    return elem


class Sequence(MultiValue):
    """Class to hold multiple :class:`~pydicom_ext.dataset.Dataset` in a
    :class:`list`.

    This class is derived from :class:`~pydicom_ext.multival.MultiValue`
    and as such enforces that all items added to the list are
    :class:`~pydicom_ext.dataset.Dataset` instances. In order to do this,
    a validator is substituted for `type_constructor` when constructing the
    :class:`~pydicom_ext.multival.MultiValue` super class.
    """

    def __init__(self, iterable=None):
        """Initialize a list of :class:`~pydicom_ext.dataset.Dataset`.

        Parameters
        ----------
        iterable : list-like of dataset.Dataset, optional
            An iterable object (e.g. :class:`list`, :class:`tuple`) containing
            :class:`~pydicom_ext.dataset.Dataset`. If not used then an empty
            :class:`Sequence` is generated.
        """
        # We add this extra check to throw a relevant error. Without it, the
        # error will be simply that a Sequence must contain Datasets (since a
        # Dataset IS iterable). This error, however, doesn't inform the user
        # that the actual issue is that their Dataset needs to be INSIDE an
        # iterable object
        if isinstance(iterable, Dataset):
            raise TypeError('The Sequence constructor requires an iterable')

        # the parent dataset
        self._parent = None

        # If no inputs are provided, we create an empty Sequence
        if not iterable:
            iterable = list()

        # validate_dataset is used as a pseudo type_constructor
        super(Sequence, self).__init__(validate_dataset, iterable)

    @property
    def parent(self):
        """Return the parent :class:`~pydicom_ext.dataset.Dataset`."""
        return self._parent

    @parent.setter
    def parent(self, value):
        """Set the parent :class:`~pydicom_ext.dataset.Dataset` and pass it to all
        :class:`Sequence` items.
        """
        if value != self._parent:
            self._parent = value
            for item in self._list:
                item.parent = self._parent

    def __setitem__(self, i, val):
        """Set the parent :class:`~pydicom_ext.dataset.Dataset` to the new
        :class:`Sequence` item
        """
        super(Sequence, self).__setitem__(i, val)
        val.parent = self._parent

    def __str__(self):
        """String description of the Sequence."""
        lines = [str(x) for x in self]
        return "[" + "".join(lines) + "]"

    def __repr__(self):
        """String representation of the Sequence."""
        formatstr = "<%(classname)s, length %(count)d>"
        return formatstr % {
            'classname': self.__class__.__name__,
            'count': len(self)
        }
