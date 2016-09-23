import math

from scipy import stats


def x_sum(data_):
    return sum([item[1] for item in data_])


def y_sum(data_):
    return sum([item[2] for item in data_])


def xx_sum(data_):
    return double_sum(data_, 1, 1)


def xy_sum(data_):
    return double_sum(data_, 1, 2)


def yy_sum(data_):
    return double_sum(data_, 2, 2)


def double_sum(data_, param1, param2):
    return sum(item[param1] * item[param2] for item in data_)


def x_avg(data_):
    return x_sum(data_) / len(data_)


def y_avg(data_):
    return y_sum(data_) / len(data_)


def calculate_b1(data_, x):
    sum_ = xy_sum(data_)
    nom = sum_ - len(data_) * x_avg(data_) * y_avg(data_)
    denom = sum([item[x] ** 2 for item in data_])
    denom -= len(data_) * x_avg(data_) ** 2
    return nom / denom


def make_histogram(grade_list):
    histogram = [0] * 10
    i = 0
    while i < len(grade_list):
        grade = grade_list[i] / 10
        histogram[grade] += 1
        i += 1.
    return histogram


def calculate_b0(data_, b1):
    return y_avg(data_) - b1 * x_avg(data_)


def variance(data_, b0, b1):
    sum_ = 0
    for i in range(0, len(data_)):
        sum_ += float((float(data_[i][2]) - b0 - (b1 * float(data_[i][1]))) ** 2)
    return float(sum_) * (1 / (len(data_) - 2))


def __range__(data_, alpha, x_k, b0, b1):
    return t_distr(data_, alpha) * std_deviation(data_, b0, b1) * math.sqrt(
        1 + 1 / len(data_) + ((x_k - x_avg(data_)) ** 2 / ((x_sum(data_) - x_avg(data_)) ** 2)))


def std_deviation(data_, b0, b1):
    return math.sqrt(variance(data_, b0, b1))


def t_distr(data_, alpha):
    return stats.t(len(data_) - 2).isf(1 - alpha)


def calc_alpha(percent):
    return 0.85 if percent == 70 else 0.95


def linear_regression(data_):
    b1 = calculate_b1(data_, 1)
    b0 = calculate_b0(data_, b1)
    x_k = 644
    r_90 = __range__(data_, calc_alpha(90), x_k, b0, b1)
    r_70 = __range__(data_, calc_alpha(70), x_k, b0, b1)
    print('Range 70%: ' + str(int(r_70)) + '\nUPI 70%: ' + str(int(x_k + r_70)) + ',  LPI 70%: ' + str(int(x_k - r_70)))
    print('Range 90%: ' + str(int(r_90)) + '\nUPI 90%: ' + str(int(x_k + r_90)) + ',  LPI 90%: ' + str(int(x_k - r_90)))
    print('Beta0: %.4f' % b0)
    print('Beta1: %.4f' % b1)

