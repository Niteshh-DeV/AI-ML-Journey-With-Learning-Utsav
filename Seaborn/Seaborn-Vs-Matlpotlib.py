import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = sns.load_dataset('tips')

# ---------- 1. SCATTER PLOT ----------
plt.figure(figsize=(10,4))

# Seaborn version
plt.subplot(1,2,1)
sns.set_style("darkgrid")
sns.set_palette("deep")
sns.scatterplot(x='total_bill', y='tip', data=data, hue='sex') # hue is used to set the color of points based on a categorical variable
plt.title("Seaborn Scatter Plot (darkgrid + deep)")

# Matplotlib equivalent
plt.subplot(1,2,2)
plt.scatter(data['total_bill'], data['tip'], c='orange', edgecolor='black') # 'c' is used to set the color of points
plt.title("Matplotlib Scatter Plot")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.tight_layout()
plt.show()

# ---------- 2. HISTOGRAM ----------
plt.figure(figsize=(10,4))

# Seaborn version
plt.subplot(1,2,1)
sns.set_style("whitegrid")
sns.set_palette("coolwarm")
sns.histplot(data['total_bill'], bins=20, kde=True) # kde=True adds a kernel density estimate line. 
#Karnel density estimation is a way to estimate the probability density function of a random variable. It shows the distribution of data over a continuous interval.
plt.title("Seaborn Histogram (whitegrid + coolwarm)")

# Matplotlib equivalent
plt.subplot(1,2,2)
plt.hist(data['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title("Matplotlib Histogram")
plt.xlabel("total_bill")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------- 3. BAR PLOT ----------
plt.figure(figsize=(10,4))

# Seaborn version
plt.subplot(1,2,1)
sns.set_style("ticks") # 'ticks' style adds ticks to the axes
sns.set_palette("muted") # 'muted' palette provides a set of muted colors, we can use other palettes like 'deep', 'bright', 'dark', 'colorblind', 'pastel', 'Set1', 'Set2', 'Set3', 'Paired', 'coolwarm', 'viridis', 'plasma', etc.
sns.barplot(x='day', y='total_bill', data=data, estimator='mean', errorbar=None) # errorbar=None removes the error bars 
# estimator='mean' calculates the mean of total_bill for each day
plt.title("Seaborn Bar Plot (ticks + muted)")

# Matplotlib equivalent
plt.subplot(1,2,2)
avg_bill = data.groupby('day')['total_bill'].mean()
plt.bar(avg_bill.index, avg_bill.values, color='lightgreen', edgecolor='black')
plt.title("Matplotlib Bar Plot")
plt.xlabel("day")
plt.ylabel("Average total_bill")
plt.tight_layout()
plt.show()

# ---------- 4. BOX PLOT ----------
plt.figure(figsize=(10,4))

# Seaborn version
plt.subplot(1,2,1)
sns.set_style("dark")
sns.set_palette("rocket")
sns.boxplot(x='day', y='tip', data=data)
plt.title("Seaborn Box Plot (dark + rocket)")

# Matplotlib equivalent
# matplot does not have a direct equivalent for seaborn's boxplot with styling options, so we use basic boxplot with some customizations.
plt.subplot(1,2,2)
data.boxplot(column='tip', by='day', grid=False, patch_artist=True,
             boxprops=dict(facecolor='lightcoral')) 
# Here patch_artist=True allows us to fill the box with color, boxprops is used to set properties of the box and dict means dictionary
plt.title("Matplotlib Box Plot")
# plt.suptitle("")  # remove automatic title
plt.xlabel("day")
plt.ylabel("tip")
plt.tight_layout()
plt.show()