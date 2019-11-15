import numpy as np
class CaseModule:
    @staticmethod
    def cap_array(arr=[]):
        return np.char.capitalize(arr) if arr else arr
    @staticmethod
    def lower_array(arr=[]):
        return np.char.lower(arr) if arr else arr
    @staticmethod
    def upper_array(arr=[]):
        return np.char.upper(arr)if arr else arr
    @staticmethod
    def title_array(arr=[]):
        return np.char.title(arr)if arr else arr
    @staticmethod
    def swap_array(arr=[]):
        return np.char.swapcase(arr)if arr else arr