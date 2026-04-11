import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b) / (np.linalg.norm(a) * (np.linalg.norm(b)) + np.finfo(np.float64).eps)