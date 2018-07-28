import networkx as nx
import matplotlib.pyplot as plt
import BiconnectedComponent
import random
# 单个社区内的度 e
def single_community_degree(G):
    e = 0
    for i in nx.degree(G).values():
        e = e + i
    return float(e)

# 单个社区内的node的度 a
def single_community_node_degree(G):
    node_bunch = nx.nodes(G)
    a = 0
    for i in nx.degree(G,nbunch=node_bunch).values():
        a = a + i
    return float(a)

# 组合而成的社区的度 m
def compose_community_degree(Composed_Graph):
    m = 0
    for i in nx.degree(Composed_Graph).values():
        m = m + i
    return float(m)

# 计算模块度 Q = sum[e/m - ((a/m)^2)]
def modularity(graph_1,graph_2):
    e1 = single_community_degree(graph_1)
    e2 = single_community_degree(graph_2)
    a1 = single_community_node_degree(graph_1)
    a2 = single_community_node_degree(graph_2)
    Composed_Graph = nx.compose(graph_1,graph_2)
    m = compose_community_degree(Composed_Graph)
    Q = ((e1/m)-((a1/m)**2)) + ((e2/m)-((a2/m)**2))
    return Q

# 通过模块度进行合并图的过程
def compose_Graph_process(bicomponents):
    i = 1
    new_bicomponents = []
    if(len(bicomponents) > 2):
        Q_left  = modularity(bicomponents[0],bicomponents[1])
        Q_right = modularity(bicomponents[1],bicomponents[2])
        print("第一个图为" + str(bicomponents[0].nodes()))
        print("第二个图为" + str(bicomponents[1].nodes()))
        print("第三个图为" + str(bicomponents[2].nodes()))
        print("第一个图和第二个图的Q:" + str(Q_left))
        print("第二个图和第三个图的Q:" + str(Q_right))
        print('--------------------------')
        if(Q_left > Q_right):
            new_graph = nx.compose(bicomponents[0],bicomponents[1])
            new_bicomponents.append(new_graph)
            for i in range(2,len(bicomponents)):
                new_bicomponents.append(bicomponents[i])
        else:
            new_graph = nx.compose(bicomponents[1],bicomponents[2])
            new_bicomponents.append(bicomponents[0])
            new_bicomponents.append(new_graph)
            for i in range(3,len(bicomponents)):
                new_bicomponents.append(bicomponents[i])
    # while(i <= len(bicomponents)-1):
    #     if(i <= len(bicomponents)-5):
    #         Q_left = modularity(bicomponents[i-1],bicomponents[i])
    #         Q_right = modularity(bicomponents[i],bicomponents[i+1])
    #         # print('---------------------------------------------------------------')
    #         print('第' + str(i-1) + '个图为：' + str(bicomponents[i-1].nodes()))
    #         print('第' + str(i) + '个图为：' + str(bicomponents[i].nodes()))
    #         print('第' + str(i+1) + '个图为：' + str(bicomponents[i+1].nodes()))
    #         print('第' + str(i-1) + '个图与第' + str(i) + '个图的Q:' + str(Q_left))
    #         print('第' + str(i) + '个图与第' + str(i+1) + '个图的Q:' + str(Q_right))
    #         print('--------------------------')
    #         if(Q_left > Q_right):
    #             new_graph = nx.compose(bicomponents[i-1],bicomponents[i])
    #             new_bicomponents.append(new_graph)
    #             i = i + 2
    #         else:
    #             new_graph = nx.compose(bicomponents[i+1],bicomponents[i])
    #             new_bicomponents.append(bicomponents[i-1])
    #             new_bicomponents.append(new_graph)
    #             i = i + 3
    #     elif(i == len(bicomponents) - 4):
    #         Q_left = modularity(bicomponents[i - 1], bicomponents[i])
    #         Q_right = modularity(bicomponents[i], bicomponents[i + 1])
    #         # print('---------------------------------------------------------------')
    #         print('第' + str(i - 1) + '个图为：' + str(bicomponents[i - 1].nodes()))
    #         print('第' + str(i) + '个图为：' + str(bicomponents[i].nodes()))
    #         print('第' + str(i + 1) + '个图为：' + str(bicomponents[i + 1].nodes()))
    #         print('第' + str(i - 1) + '个图与第' + str(i) + '个图的Q:' + str(Q_left))
    #         print('第' + str(i) + '个图与第' + str(i + 1) + '个图的Q:' + str(Q_right))
    #         print('--------------------------')
    #         if (Q_left > Q_right):
    #             new_graph = nx.compose(bicomponents[i - 1], bicomponents[i])
    #             new_bicomponents.append(new_graph)
    #             i = i + 2
    #         else:
    #             new_graph = nx.compose(bicomponents[i + 1], bicomponents[i])
    #             new_bicomponents.append(bicomponents[i - 1])
    #             new_bicomponents.append(new_graph)
    #             new_bicomponents.append(bicomponents[i+2])
    #             new_bicomponents.append(bicomponents[i+3])
    #             i = len(bicomponents)
    #     elif(i == len(bicomponents) - 3):
    #         Q_left = modularity(bicomponents[i - 1], bicomponents[i])
    #         Q_right = modularity(bicomponents[i], bicomponents[i + 1])
    #         # print('---------------------------------------------------------------')
    #         print('第' + str(i - 1) + '个图为：' + str(bicomponents[i - 1].nodes()))
    #         print('第' + str(i) + '个图为：' + str(bicomponents[i].nodes()))
    #         print('第' + str(i + 1) + '个图为：' + str(bicomponents[i + 1].nodes()))
    #         print('第' + str(i - 1) + '个图与第' + str(i) + '个图的Q:' + str(Q_left))
    #         print('第' + str(i) + '个图与第' + str(i + 1) + '个图的Q:' + str(Q_right))
    #         print('--------------------------')
    #         if (Q_left > Q_right):
    #             new_graph = nx.compose(bicomponents[i - 1], bicomponents[i])
    #             new_bicomponents.append(new_graph)
    #             new_bicomponents.append(bicomponents[i + 1])
    #             new_bicomponents.append(bicomponents[i + 2])
    #             i = len(bicomponents)
    #         else:
    #             new_graph = nx.compose(bicomponents[i + 1], bicomponents[i])
    #             new_bicomponents.append(bicomponents[i - 1])
    #             new_bicomponents.append(new_graph)
    #             new_bicomponents.append(bicomponents[i + 2])
    #             i = len(bicomponents)
    #     elif(i == len(bicomponents) - 2):
    #         Q_left = modularity(bicomponents[i - 1], bicomponents[i])
    #         Q_right = modularity(bicomponents[i], bicomponents[i + 1])
    #         # print('---------------------------------------------------------------')
    #         print('第' + str(i - 1) + '个图为：' + str(bicomponents[i - 1].nodes()))
    #         print('第' + str(i) + '个图为：' + str(bicomponents[i].nodes()))
    #         print('第' + str(i + 1) + '个图为：' + str(bicomponents[i + 1].nodes()))
    #         print('第' + str(i - 1) + '个图与第' + str(i) + '个图的Q:' + str(Q_left))
    #         print('第' + str(i) + '个图与第' + str(i + 1) + '个图的Q:' + str(Q_right))
    #         print('--------------------------')
    #         if (Q_left > Q_right):
    #             new_graph = nx.compose(bicomponents[i - 1], bicomponents[i])
    #             new_bicomponents.append(new_graph)
    #             new_bicomponents.append(bicomponents[i+1])
    #             i = len(bicomponents)
    #         else:
    #             new_graph = nx.compose(bicomponents[i + 1], bicomponents[i])
    #             new_bicomponents.append(bicomponents[i - 1])
    #             new_bicomponents.append(new_graph)
    #             i = len(bicomponents)
    #     elif(i == len(bicomponents) - 1):
    #         new_bicomponents.append(bicomponents[i])
    #         i = len(bicomponents)
    return new_bicomponents

# 循环执行模块度的计算
def modularity_loop(bicomponents,cluster):
    count = 1
    while(len(bicomponents) > 0):
        if(len(bicomponents) > cluster):
            print('*******************' + '以下为第' + str(count) + '轮的模块度的计算********************')
            new_bicomponents = compose_Graph_process(bicomponents)
            for num in range(0,len(new_bicomponents)):
                print("第" + str(num) + "个子图的节点为: " + str(new_bicomponents[num].nodes()))
            count = count + 1
            print('*********************************************************************************')
            bicomponents = new_bicomponents

        else:
            break
    return bicomponents

# 绘制需要的层数的图
def draw_modularity_graph(bicomponents):
    nodeColor_list = ['#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3', '#DCDCDC', '#F5F5F5',
                      '#800000', '#B22222', '#A52A2A', '#FF0000', '#CD5C5C', '#BC8F8F', '#F08080',
                      '#FA8072', '#FFE4E1', '#E9967A', '#FF4500', '#FFA07A', '#A0522D', '#8B4513',
                      '#D2691E', '#F4A460', '#FFDAB9', '#CD853F', '#FF8C00', '#FFE4C4', '#DEB887',
                      '#FFDEAD', '#DAA520', '#FFD700', '#F0E68C', '#BDB76B', '#808000', '#FFFF00',
                      '#FAFAD2', '#556B2F', '#ADFF2F', '#006400', '#008000', '#00FF00', '#8FBC8F',
                      '#2E8B57', '#3CB371', '#00FF7F', '#00FA9A', '#40E0D0', '#20B2AA', '#008080',
                      '#008B8B', '#2F4F4F', '#00CED1', '#AFEEEE', '#5F9EA0', '#B0E0E6', '#00BFFF',
                      '#87CEEB', '#87CEFA', '#4682B4', '#1E90FF', '#708090', '#6495ED', '#4169E1',
                      '#000080', '#0000FF', '#483D8B', '#6A5ACD', '#9370DB', '#8A2BE2', '#4B0082',
                      '#BA55D3', '#8B008B', '#FF00FF', '#DDA0DD', '#C71585', '#DB7093', '#DC143C']
    for num in range(0,len(bicomponents)):
        color = random.randint(0,76)
        for i in bicomponents[num].nodes():
            NodeColor[i-1] = nodeColor_list[color]
    for i in cut_vertices:
        # NodeColor[i] = '#FFFFFF'
        NodeColor[i-1] = 'r'
    plt.subplot(212)
    nx.draw_networkx(G,node_color = NodeColor)
    plt.show()




bicomponents,NodeColor,cut_vertices,G = BiconnectedComponent.BiconnectedGraph('data/cond.gml')
bicomponents = modularity_loop(bicomponents,2)
draw_modularity_graph(bicomponents)
