import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

import read_config


def test_get_config():
    assert read_config.get_config('ip1') == '192.168.1.12'


if __name__ == '__main__':
    test_get_config()
    print(read_config.get_config('ip1'))
