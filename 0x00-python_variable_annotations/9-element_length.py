#!/usr/bin/env python3
""" function element_length"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
