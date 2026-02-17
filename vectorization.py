# vectorization.py to calcualate sales a
import numpy as np

num_products = 1_000_000  

prices = np.random.uniform(10, 1000, size=num_products)  

tax_rate = 0.50       
discount_rate = 0.10
final_prices = prices * (1 + tax_rate) * (1 - discount_rate)
# Step 4: Summary statistics
print("Number of products:", num_products)
print("Original price sample:", prices[:5])
print("Final price sample:", final_prices[:5])
print("Total revenue if all sold:", np.sum(final_prices))
print("Average final price:", np.mean(final_prices))
print("Maximum final price:", np.max(final_prices))
print("Minimum final price:", np.min(final_prices))
