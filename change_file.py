def changefile(file):
    with open(file,'r+') as f:
        with open("data/cond.gml",'r+') as w:
            content = f.readlines()
            count = 0
            for line in content:
                line = line.replace('  node\n','  node')
                line = line.replace('  edge\n', '  edge')
                if 'label' in line:
                    w.write('    label' + ' ' + str(count) + '\n')
                    count = count + 1
                else:
                    w.write(line)




changefile("data/cond-mat-2005.gml")