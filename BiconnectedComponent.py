#coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt
import numpy
import random

#色值列表，随机给形成的2-连通分量上颜色
nodeColor_list = ['#696969','#808080','#A9A9A9','#C0C0C0','#D3D3D3','#DCDCDC','#F5F5F5',
                  '#800000','#B22222','#A52A2A','#FF0000','#CD5C5C','#BC8F8F','#F08080',
                  '#FA8072','#FFE4E1','#E9967A','#FF4500','#FFA07A','#A0522D','#8B4513',
                  '#D2691E','#F4A460','#FFDAB9','#CD853F','#FF8C00','#FFE4C4','#DEB887',
                  '#FFDEAD','#DAA520','#FFD700','#F0E68C','#BDB76B','#808000','#FFFF00',
                  '#FAFAD2','#556B2F','#ADFF2F','#006400','#008000','#00FF00','#8FBC8F',
                  '#2E8B57','#3CB371','#00FF7F','#00FA9A','#40E0D0','#20B2AA','#008080',
                  '#008B8B','#2F4F4F','#00CED1','#AFEEEE','#5F9EA0','#B0E0E6','#00BFFF',
                  '#87CEEB','#87CEFA','#4682B4','#1E90FF','#708090','#6495ED','#4169E1',
                  '#000080','#0000FF','#483D8B','#6A5ACD','#9370DB','#8A2BE2','#4B0082',
                  '#BA55D3','#8B008B','#FF00FF','#DDA0DD','#C71585','#DB7093','#DC143C']

# 初始化图,并通过二连通算法进行上色
def BiconnectedGraph(file):
    # 绘制成图
    G = nx.read_gml(file)
    # A = numpy.matrix([[0, 1, 1, 0, 0, 0, 0],
    #                   [1, 0, 1, 0, 0, 0, 0],
    #                   [1, 1, 0, 1, 0, 0, 0],
    #                   [0, 0, 1, 0, 1, 0, 0],
    #                   [0, 0, 0, 1, 0, 1, 1],
    #                   [0, 0, 0, 0, 1, 0, 1],
    #                   [0, 0, 0, 0, 1, 1, 0]])
    # B = numpy.matrix([[0,1,2,0,0,0,0,0,0,0],
    #                   [1,0,1,0,0,0,0,0,0,0],
    #                   [1,1,0,1,0,0,0,0,0,0],
    #                   [0,0,1,0,1,0,0,0,0,0],
    #                   [0,0,0,1,0,1,1,0,0,0],
    #                   [0,0,0,0,1,0,1,0,0,0],
    #                   [0,0,0,0,1,1,0,1,1,1],
    #                   [0,0,0,0,0,0,1,0,0,0],
    #                   [0,0,0,0,0,0,1,0,0,1],
    #                   [0,0,0,0,0,0,1,0,1,0]])
    # G = nx.from_numpy_matrix(B)
    # node的个数00000000000000000
    node_length = len(G.nodes())
    # print(node_length)

    # 一个列表 给node加颜色
    NodeColor = []

    """
    ------------------------------------------------------------------------------------------------------
    接下来为2-连通分量的实现

    """
    # 给所有的点设为透明
    for i in range(0,node_length):
        NodeColor.append('#FFFFFF')

    # 生成BiconnectedComponent
    bicomponents = list(nx.biconnected_component_subgraphs(G))
    # print(len(bicomponents))

    # 根据划分，给不同的components上不同的颜色
    for num in range(0,len(bicomponents)):
        color = random.randint(0,75)
        print("第" + str(num) + "个二连通子图的节点为: "+ str(bicomponents[num].nodes()))
        for i in bicomponents[num].nodes():
            NodeColor[i] = nodeColor_list[color]

    # 寻找割点，并用红色标注
    cut_vertices = list(nx.articulation_points(G))
    for i in cut_vertices:
        # NodeColor[i] = '#FFFFFF'
        NodeColor[i] = 'r'
    print("割点："+ str(cut_vertices))

    # G = nx.compose(bicomponents[0],bicomponents[1])
    # G = nx.compose(bicomponents[2],G)

    # 给图上色
    plt.figure(1)
    plt.subplot(211)
    nx.draw_networkx(G, node_color=NodeColor)

    # 展示图
    # plt.show()
    return bicomponents,NodeColor,cut_vertices,G


# 调用函数进行测试
# bicomponents = BiconnectedGraph('test.gml')
