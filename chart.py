import matplotlib.pyplot as plt
products=['product a','product b','product c','product d']
inventory=[45,88,21,63]
plt.figure(figsize=(8,5))
plt.bar(products,inventory,color='teal',edgecolor='black',width=0.6)
plt.title('current stock inventory level',fontsize=14)
plt.xlabel('product catalog',fontsize=12)
plt.ylabel('units available',fontsize=12)
plt.show()
