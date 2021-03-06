#!/usr/bin/env python3

import pytest
import pandas as pd
import os
import utils

test_output_path = os.path.dirname(os.path.abspath(__file__)) + \
    '/../../'


@pytest.mark.makeBigWig
def test_makeBigWig():
    assert os.path.exists(os.path.join(test_output_path, 'Q-Y5F6_1M.se.bw'))
