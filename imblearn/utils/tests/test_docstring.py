"""Test utilities for docstring."""

# Authors: Guillaume Lemaitre <g.lemaitre58@gmail.com>
# License: MIT

import pytest

from imblearn.utils import Substitution

func_docstring = \
    """A function.

    Parameters
    ----------
    xxx

    yyy
    """.rstrip()


def func(param_1, param_2):
    """A function.

    Parameters
    ----------
    {param_1}

    {param_2}
    """
    return param_1, param_2


cls_docstring = \
    """A class.

    Parameters
    ----------
    xxx

    yyy
    """.rstrip()


class cls(object):
    """A class.

    Parameters
    ----------
    {param_1}

    {param_2}
    """
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2


@pytest.mark.parametrize(
    "obj, obj_docstring",
    [(func, func_docstring),
     (cls, cls_docstring)]
)
def test_docstring_inject(obj, obj_docstring):
    obj_injected_docstring = Substitution(param_1='xxx', param_2='yyy')(obj)
    obj_injected_docstring.__doc__ == obj_docstring
