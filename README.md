# 🛒 E-Commerce Business Simulation using NumPy

A data science mini project that simulates **30 days of e-commerce business operations** using NumPy's probability distributions — demonstrating how statistical modeling is applied in real-world business analytics and ML simulations.

---

## 📌 Project Overview

This project generates realistic synthetic business data for an e-commerce platform by leveraging key probability distributions. It models day-to-day variability in customer behavior, purchases, deliveries, and product quality — the kind of data pipeline that powers dashboards, forecasting models, and business intelligence systems.

---

## 🎯 Key Concepts Demonstrated

| Distribution | Business Use Case |
|---|---|
| **Poisson** | Daily customer arrivals & delivery time estimation |
| **Normal** | Purchase amount variation around a mean basket size |
| **Multinomial** | Product category demand distribution |
| **Exponential** | Waiting time between consecutive orders |
| **Binomial** | Product quality pass/fail rate |

---

## 🚀 Features

- 📦 Simulates **30 days** of e-commerce activity
- 👥 **Customer traffic** modeled with Poisson distribution (avg. 100/day)
- 💰 **Purchase amounts** drawn from Normal distribution (mean ₹1500, std ₹300)
- 🗂️ **Product category** breakdown across 4 categories using Multinomial
- 🚚 **Delivery time** estimation in days using Poisson
- ⏱️ **Order waiting time** modeled with Exponential distribution
- ✅ **Quality check** pass/fail using Binomial distribution (90% pass rate)

---

## 🧰 Tech Stack

- **Language:** Python 3.x
- **Library:** NumPy

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Ecommerce-business-simulation-numpy.git

# 2. Navigate into the project directory
cd Ecommerce-business-simulation-numpy

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the simulation
python ecommerce_simulation.py
```

---

## 📊 Sample Output

```
Customers:   [102  96  95 109  96 ...]   # Daily visitor count
Purchase:    [1427.85 1985.63 1696.04 ...]  # Purchase amount in ₹
Product cat: [9 8 7 6]                   # Items per category
Delivery:    [3 2 4 3 2 ...]             # Estimated delivery days
Waiting:     [1.82 2.45 0.93 ...]       # Hours between orders
Quality:     [1 1 0 1 1 ...]            # 1 = Pass, 0 = Fail
```

---

## 📁 Project Structure

```
Ecommerce-business-simulation-numpy/
│
├── ecommerce_simulation.py   # Main simulation script
├── requirements.txt          # Python dependencies
├── sample_output.txt         # Example output preview
└── README.md                 # Project documentation
```

---

## 💡 Learning Outcomes

- Understanding how probability distributions model real-world business scenarios
- Foundation for **Monte Carlo simulations** used in forecasting
- Base for extending into **Pandas DataFrames**, **Matplotlib visualizations**, and **ML pipelines**

---

## 🔮 Future Improvements

- [ ] Add Pandas DataFrame for structured data analysis
- [ ] Visualize trends using Matplotlib / Seaborn
- [ ] Generate summary statistics (total revenue, avg customers, quality rate)
- [ ] Export simulation data to CSV for further analysis
- [ ] Build interactive dashboard using Streamlit

---

## 👤 Author

**Ayaan Pasha**
- 📧 ayaanpashacloud@gmail.com
- 🔗 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
