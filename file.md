# Weekly Step Count Analysis

## Introduction  
Tracking our daily step count helps us stay active and compare progress over time. This report analyzes the number of steps walked each day for a week, comparing it with a friend's step count.

## Methodology  
- Data collected using a **fitness tracker**.  
- Steps recorded for *seven consecutive days*.  
- Compared with a friend's step data.

## Step Count Data  

| Day        | My Steps | Friend's Steps |
|------------|---------|---------------|
| Monday     | 7,500   | 8,200         |
| Tuesday    | 8,200   | 7,900         |
| Wednesday  | 6,700   | 7,500         |
| Thursday   | 9,000   | 8,800         |
| Friday     | 10,200  | 9,300         |
| Saturday   | 12,500  | 11,800        |
| Sunday     | 11,300  | 10,900        |

## Key Insights  
1. **Friday and Saturday** had the highest step count.  
2. **Wednesday** had the lowest step count for both.  
3. Maintaining at least **8,000 steps per day** is beneficial.

## Python Code to Visualize the Data  
```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
my_steps = [7500, 8200, 6700, 9000, 10200, 12500, 11300]
friend_steps = [8200, 7900, 7500, 8800, 9300, 11800, 10900]

plt.plot(days, my_steps, label="My Steps", marker="o")
plt.plot(days, friend_steps, label="Friend's Steps", marker="s")

plt.xlabel("Days of the Week")
plt.ylabel("Steps")
plt.title("Step Count Comparison")
plt.legend()
plt.show()
