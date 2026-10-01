import os
import random
import numpy as np
import pandas as pd

from faker import Faker
from datetime import timedelta

fake = Faker()

random.seed(42)
np.random.seed(42)

STUDYID = "HYPER-P2"

SITES = [
    "101",
    "102",
    "103",
    "104",
    "105"
]

N_SUBJECTS = 100

VISITS = {
    "SCREENING": 0,
    "BASELINE": 1,
    "WEEK4": 29,
    "WEEK8": 57,
    "WEEK12": 85
}

os.makedirs("data/raw", exist_ok=True)
