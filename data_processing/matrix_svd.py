# encoding=utf-8

import numpy as np
from scipy.sparse.linalg import svds
from scipy import sparse as sp
from hyperparams import Hyperparams as hp


def vector_to_diagonal(vector):
    """
    将向量放在对角矩阵的对角线上
    :param vector:
    :return:
    """
    if (isinstance(vector, np.ndarray) and vector.ndim == 1) or \
            isinstance(vector, list):
        length = len(vector)
        diag_matrix = np.zeros((length, length))
        np.fill_diagonal(diag_matrix, vector)
        return diag_matrix
    return None


interMatrix = np.load('matrix.npy')

interMatrix = interMatrix.astype('float')
U, S, VT = svds(sp.csr_matrix(interMatrix), k=hp.pca_dim, maxiter=hp.pca_maxiter)  # 2个隐主题
S = vector_to_diagonal(S)

print('RNA vector representation shape:')
print(U.shape)
print('Singular value matrix：')
print(np.sum(S, axis=0))
print('disease vector representation shape:')
print(VT.T.shape)

np.save('u_feature.npy', U)
np.save('v_feature.npy', VT.T)

