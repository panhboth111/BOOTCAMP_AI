import numpy as np
class MatrixModule:
    @staticmethod
    def gen_empty_matrix(height,width):
        return np.full((height,width),'')
    @staticmethod
    def gen_value_matrix(val,height,width):
        return np.full((height,width),val)
    @staticmethod
    def gen_border_matrix(height,width,border):
        if(border>height/2 or border>width/2 or border<0):
            return None
        else:
            arr = np.full((height-(border*2),width-(border*2)),0)
            arr = np.pad(arr,pad_width=border,mode='constant', constant_values=1)
            return arr

