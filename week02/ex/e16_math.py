import numpy as np
class Math2DModule:
    @staticmethod
    def row_min(arr):
        return np.array([np.min(row) for row in arr])
    @staticmethod
    def row_max(arr):
        return np.array([np.max(row) for row in arr])
    @staticmethod
    def row_mean(arr):
        return np.array([np.mean(row) for row in arr])
    @staticmethod
    def row_median(arr):
        return np.array([np.median(row) for row in arr ])
    @staticmethod
    def column_min(arr):
        return np.amin(np.array(arr),axis=0)
    @staticmethod
    def column_max(arr):
        return np.amax(np.array(arr),axis=0)
    @staticmethod
    def column_mean(arr):
        return np.mean(np.array(arr),axis=0)
    @staticmethod
    def column_median(arr):
        return np.median(np.array(arr),axis=0)
