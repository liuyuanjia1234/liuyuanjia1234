import jieba
import numpy
import re
import math
import jieba.analyse as analyse

tfidf = analyse.extract_tags
jieba.setLogLevel(jieba.logging.INFO)


def duplicate_check_function_1(o_file, c_file):
    """
    注释：
        首先读取数据，然后对数据进行分词，并且过滤掉标点
    :param o_file: 原始论文的地址
    :param c_file: 抄袭论文的地址
    :return: 返回列表，包含两个分词的结果
    """
    jieba.setLogLevel(jieba.logging.INFO)  # 使用中文词库来进行分词
    o_list = []
    c_list = []
    try:
        with open(o_file, 'r', encoding='utf-8') as f:
            o_lines = f.readlines()
        for line in o_lines:
            pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")  # 正则匹配保留中文字符
            target = pattern.sub("", line)
            for data in jieba.lcut(target):
                o_list.append(data)
    except Exception as e:
        print(f"出现异常了,异常为:{e}")

    try:
        with open(c_file, 'r', encoding='utf-8') as f:
            c_lines = f.readlines()
        for line in c_lines:
            pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")  # 正则匹配保留中文字符
            target = pattern.sub("", line)
            for data in jieba.lcut(target):
                c_list.append(data)
    except Exception as e:
        print(f"出现异常了,异常为:{e}")

    final_list = list(set(o_list).union(set(c_list)))
    print(final_list)
    list_a = []
    list_b = []
    # 转换为向量的形式
    for word in final_list:
        list_a.append(o_list.count(word))
        list_b.append(c_list.count(word))

    # 计算余弦相似度
    parameter_a = numpy.array(list_a)
    parameter_b = numpy.array(list_b)
    cos = (numpy.dot(parameter_a, parameter_b.T)) / (
            (math.sqrt(numpy.dot(parameter_a, parameter_a.T))) * (math.sqrt(numpy.dot(parameter_b, parameter_b.T))))
    # print(f"两篇文章的相似度为{cos}")
    print('两篇文章的相似度为%.2f' % cos)
    f = open("D:/answer.txt", "a", encoding="UTF-8")
    f.write('%.2f'%cos)
    f.write('\n')
    f.close()

def duplicate_check_function_2(file):
    # 提取关键字
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"出现异常了,异常为:{e}")

    tags = jieba.analyse.extract_tags(content, 10)
    return tags


# 计算相似度
def calculate_similarity(o_file, c_file):
    parameter_i = set(o_file).intersection(set(c_file))
    parameter_j = set(o_file).union((set(c_file)))
    return round(len(parameter_i) * 100 / len(parameter_j), 2)


def func(o_file, c_file):
    f1 = duplicate_check_function_2(o_file)
    f2 = duplicate_check_function_2(c_file)
    result = calculate_similarity(f1, f2)/100
    f = open("D:/answer.txt", "a", encoding="UTF-8")
    f.write('%.2f'%result)
    f.write('\n')
    f.close()
    return result

