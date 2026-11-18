import numpy as np
def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Write code here
    data = np.array(data)
    
    min_max = []
    
    for i in range(0, data.shape[1]):
        min_max.append( [min(data[:, [i]])[0], max(data[:, [i]])[0]])
    
    output = []
    for row in range(0, data.shape[0]):
        for column in range(0, data.shape[1]):
            denominator = (min_max[column][1] - min_max[column][0])
            if denominator == 0:
                equation = 0.0
            else:
                equation = (data[row][column] - min_max[column][0]) / denominator
            output.append(equation)
    return np.array(output).reshape(data.shape).tolist()            