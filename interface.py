from abc import ABCMeta, abstractmethod


class BaseCorAna(metaclass=ABCMeta):

    @abstractmethod
    def standardization(self, matrix):
        """
        对应步骤一
        将向量按列标准化的方法
        :param matrix: 输入需标准化的矩阵
        :return: 标准化后的矩阵
        """

    @abstractmethod
    def initialFactorLoadMatrix(self, matrix):
        """
        对应步骤二
        输入标准化后的矩阵，根据主成分法计算初始因子载荷阵
        :param matrix: 标准化后的矩阵
        :return: 对应的初始因子载荷阵
        """

    def varMaxOrthogonalRotation(self, matrix):
        """
        对应步骤二
        对因子载荷阵进行方差最大化正交旋转
        :param matrix: 需进行方差最大化正交旋转的矩阵
        :return: 经过方差最大化正交旋转的因子载荷阵
        """

    def getMinColumnMatrix(self, matrix):
        """
        对应步骤二，计算初始因子载荷阵每行元素有最大绝对值且列数最小的矩阵
        并返回最小列数矩阵及列数逐渐加一的矩阵的列表
        :param nmatrix:
        :return:
        """

    def determineIfRatating(self, matrix_list):
        """
        对应步骤三，确定因子是否旋转
        :param matrix_list: 输入方差最大化正交旋转后因子载荷阵列表
        :return: 确定的因子载荷阵
        """

    def determineM(self, matrix_Lk, matrix_L0):
        """
        对应步骤四，确定因子个数m
        :param matrix_Lk:确定的因子载荷阵
        :param matrix_L0: 初始因子载荷阵
        :return: 因子个数m, 相应的因子载荷阵L和因子组成的元组
        """

    def determineF(self, matrix_f):
        """
        对应步骤六
        确定因子样品值矩阵
        :param matrix_f: 计算好的因子
        :return: 因子样品值矩阵F
        """

    def plotDoubleInfoGraphic(self, matrix_f, matrix_L, matrix_F):
        """
        作因子双重信息图，注意只能在二维或三维情形下作图
        :param matrix_f: 因子矩阵
        :param matrix_L: 因子载荷阵
        :param matrix_F: 因子样品值矩阵
        :return:
        """