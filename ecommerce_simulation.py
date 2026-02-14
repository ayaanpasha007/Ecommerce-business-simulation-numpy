# MINI PROJECT
# E-Commerce Business Simulation (30 Days)

import numpy as np

# Daily customers (Poisson)
customers=np.random.poisson(100,30)

# Purchase amount (Normal)
purchase=np.random.normal(1500,300,30)

# Product category (Multinomial)
products=np.random.multinomial(30,[0.3,0.3,0.2,0.2])

# Delivery time (Poisson)
delivery=np.random.poisson(3,30)

# Waiting time between orders (Exponential)
waiting=np.random.exponential(2,30)

# Product quality (Binomial)
quality=np.random.binomial(1,0.9,30)

print("Customers:",customers)
print("Purchase:",purchase)
print("Product category:",products)
print("Delivery:",delivery)
print("Waiting:",waiting)
print("Quality:",quality)
