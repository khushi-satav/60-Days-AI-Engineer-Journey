import numpy as np
prices=np.array([12,34,555,5])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)