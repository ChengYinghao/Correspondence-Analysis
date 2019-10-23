import numpy as np


def standardization(matrix):
    """
    步骤一 \n
    原始数据的标准化，
    即分别对每一个特征的值进行平移和缩放，
    使他们的均值为 0，方差为 1

    :param matrix: 原始数据矩阵，其 shape 为 (条目数, 特征数)
    :return: 标准化后的矩阵
    """
    # 平移使均值为 0
    matrix = matrix - np.mean(matrix, 0)
    # 缩放使方差为 1
    matrix /= np.sqrt(np.mean(np.square(matrix), 0))

    return matrix


def initial_factor_load_matrix(matrix):
    """
    步骤二 \n
    输入标准化后的矩阵，根据主成分法计算初始因子载荷阵

    :param matrix: 标准化后的矩阵，其 shape 为 (条目数, 特征数)
    :return: 对应的初始因子载荷阵
    """
    # 求协方差矩阵
    covar = np.mean(np.expand_dims(matrix, 1) * np.expand_dims(matrix, 2), 0)
    # 求特征值和特征向量
    values, vectors = np.linalg.eig(covar)
    # 将特征向量根据特征值大小排序
    vectors = vectors[np.argsort(values), :]
    # 用特征向量求主成分
    factor_matrix = np.sum(np.expand_dims(vectors, 0) * np.expand_dims(matrix, 1), -1)

    return factor_matrix


def varMaxOrthogonalRotation(matrix):
    """
    对应步骤二
    对因子载荷阵进行方差最大化正交旋转

    :param matrix: 需进行方差最大化正交旋转的矩阵
    :return: 经过方差最大化正交旋转的因子载荷阵
    """


def getMinColumnMatrix(matrix):
    """
    对应步骤二，计算初始因子载荷阵每行元素有最大绝对值且列数最小的矩阵
    并返回最小列数矩阵及列数逐渐加一的矩阵的列表

    :param matrix:
    :return:
    """


def determineIfRatating(matrix_list):
    """
    对应步骤三，确定因子是否旋转

    :param matrix_list: 输入方差最大化正交旋转后因子载荷阵列表
    :return: 确定的因子载荷阵
    """


def determineM(matrix_Lk, matrix_L0):
    """
    对应步骤四，确定因子个数m

    :param matrix_Lk:确定的因子载荷阵
    :param matrix_L0: 初始因子载荷阵
    :return: 因子个数m, 相应的因子载荷阵L和因子组成的元组
    """


def determineF(matrix_f):
    """
    对应步骤六
    确定因子样品值矩阵

    :param matrix_f: 计算好的因子
    :return: 因子样品值矩阵F
    """


def plotDoubleInfoGraphic(matrix_f, matrix_L, matrix_F):
    """
    作因子双重信息图，注意只能在二维或三维情形下作图

    :param matrix_f: 因子矩阵
    :param matrix_L: 因子载荷阵
    :param matrix_F: 因子样品值矩阵
    :return:
    """
