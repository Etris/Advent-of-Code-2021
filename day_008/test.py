import pytest
from main import (
    prepare_mapping_patterns
)


def test_prepare_mapping_patterns():
    assert prepare_mapping_patterns(
        ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab',
         'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    ) == {
        0: 'cagedb',
        1: 'ab',
        2: 'gcdfa',
        3: 'fbcad',
        4: 'eafb',
        5: 'cdfbe',
        6: 'cdfgeb',
        7: 'dab',
        8: 'acedgfb',
        9: 'cefabd'
    }
