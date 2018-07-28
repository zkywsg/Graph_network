#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt


# 对karate.gml文件进行格式化处理
def renew_gml(file):
    with open(file,'r') as f:
        line = f.readlines()
        line = str(line)
        line = line.replace('[','').replace('\'','').replace('\\n','').replace('node','node [')\
                        .replace('edge','edge [').replace('graph','graph [').replace(']]',']')
        print(line)
        with open('test.gml','w') as w:
            words = line.split(',')
            print(words)
            count = 1
            for word in words:
                if(word == '   '):
                    continue

                else:
                    w.write(word)
                    w.write('\n')

# 调用函数将karate.gml处理成test.gml
# renew_gml('karate.gml')


g = nx.read_gml('test.gml')
# 将test.gml进行图形化展示
nx.draw_networkx(g)
plt.show()

# print(g.nodes())
# print(g.edges())

