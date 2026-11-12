
import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,60,30], color='blue', label='Class A')
plt.scatter([1,2,3], [40,50,53], color='orange', label='Class B')

plt.xlabel('hour studied')
plt.ylabel('exam score')
plt.title('Relation between time and study')

plt.legend()
plt.grid(True)
plt.show()
