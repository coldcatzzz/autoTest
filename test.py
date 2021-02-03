import pandas

data = pandas.read_excel('calc.xlsx',sheet_name=0,names=['s1','op','s2','yq'],dtype={'s1':str,'op':str,'yq':str},header=None)
data = data.values.tolist()
print(data)