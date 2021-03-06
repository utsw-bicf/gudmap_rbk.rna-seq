#!/usr/bin/env python3

import pytest
import pandas as pd
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + \
    '/../../'


@pytest.mark.getData
def test_getData():
    assert os.path.exists(os.path.join(
        test_output_path, 'Q-Y5F6_inputBag/bagit.txt'))
    assert os.path.exists(os.path.join(
        test_output_path, 'Q-Y5F6_inputBag/data/assets/Study/Q-Y4GY/Experiment/Q-Y4DP/Replicate/Q-Y5F6/mMARIS_Six2-#3.gene.rpkm.txt'))
