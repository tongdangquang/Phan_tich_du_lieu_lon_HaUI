import pandas as pd
import numpy as np
# # Đọc tệp dữ liệu Karate.net
# df = pd.read_csv('KAR.net')
#
# # In thông tin cơ bản về dữ liệu
# print("Thông tin về dữ liệu:")
# print("Số lượng dòng và cột:", df.shape)
# print("\nCác cột trong dữ liệu:")
# print(df.columns)
# print("\nMột số dòng đầu của dữ liệu:")
# print(df.to_string())

def ReadNet(filename):
    f = open(filename, 'r')
    item = f.readline()
    n = int(item.split()[1])
    for i in range(n+1):
        item = f.readline()
    network = []
    while item != '':
        item = f.readline()
        if item != '':
            line = item.split()
            network.append(list(map(int, line)))
    return network, n

def ReadPairs(filename):
    network = []
    f = open(filename, 'r')
    item = f.readline()
    network.append(list(map(int, item.split())))
    while item != '':
        item = f.readline()
        if item != '':
            network.append(list(map(int, item.split())))
    return network

Net = np.loadtxt('KAR.pairs')

netnumeric = []
for x in Net:
    netnumeric.append(list(map(int, x)))

print(netnumeric)

