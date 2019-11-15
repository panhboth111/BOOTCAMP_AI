import numpy as np
class MathModule:
    @staticmethod
    def get_min(arr=[]):
        try:
            return np.amin(arr) if arr  else arr
        except:
            return []
    @staticmethod
    def get_max(arr=[]):
        try:
            return np.amax(arr) if arr else arr
        except:
            return []
    @staticmethod
    def get_average(arr=[]):
        try:
            return np.average(arr) if arr else arr
        except:
            return []
    @staticmethod
    def get_min_max(arr=[]):
        try:
            return (np.amin(arr),np.amax(arr)) if arr else arr
        except:
            return []
    @staticmethod
    def get_diff(arr=[]):
        try:
            return np.amax(arr)-np.amin(arr) if arr else arr
        except:
            return []