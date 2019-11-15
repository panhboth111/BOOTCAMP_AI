import numpy as np
import matplotlib as mp
import pandas as pd
class InfoModule:
    @staticmethod
    def numpy_version():
        return np.version.version
    @staticmethod
    def pandas_version():
        return pd.__version__
    @staticmethod
    def matplotlib_version():
        return mp.__version__
    @staticmethod
    def all_versions():
        return {'numpy': np.version.version, 'pandas':pd.__version__, 'matplotlib': mp.__version__}