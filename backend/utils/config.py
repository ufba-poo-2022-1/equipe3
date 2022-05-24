import logging
import os
from doctest import FAIL_FAST

log = logging.getLogger(__name__)

DB_NAME = "Test.sqlite"

DB_PATH = os.path.abspath(DB_NAME)


