import matplotlib.pyplot as plt

product = ['a', 'b', 'c', 'd']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color='orange', label='Sales 2020')

plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sale Comparison')

plt.legend()
plt.show()