

import numpy as np

    
def is_sheet_usable(sheet):
    
    if check_is_valid_array(sheet):
    
        sheet_slices = np.zeros((100, 100), dtype=np.int32)
        if sheet[sheet == 1].sum() < 9:
            for i in range(0, 97, 1):
                for j in range(0, 97, 1):
                    sheet_slice = sheet[i:i + 3, i:i + 3]
                    if sheet_slice[sheet_slice == 1].sum() > 4:
                        sheet_slices[i, j] = 1 
            if sheet_slices.sum() == 0:
                return True
            else:
                return False
        else:
            return False


def check_is_valid_array(sheet):
    if type(sheet) == np.ndarray:
        if sheet.shape == (100, 100):
            is_valid_array = np.all((sheet == 1) | (sheet == 0)) 
            if not is_valid_array:
                raise ValueError("array values need to be 0 or 1")    
        else:
            raise ValueError("array dimensions not 100 by 100")
    else:
        raise TypeError("Sheet not an ndarray")
    
    return is_valid_array
    


