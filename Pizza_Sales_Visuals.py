#Using Python to make Visualizations 

#Visualization 1- Bar Chart for Top Selling Pizza
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv(r'C:\Users\tbkcpu\Documents\PizzaSalesCleaned.csv')

# Group and sort to find top-selling pizzas
top_pizzas = df.groupby('pizza_name')['quantity'].sum().sort_values(ascending=False).head(10)

# Plot with Set 2 color palette
plt.figure(figsize=(12, 6))
colors = plt.cm.Set2.colors  # Use Set 2 color palette
bars = plt.bar(top_pizzas.index, top_pizzas.values, color=colors)

plt.title('Top 10 Best-Selling Pizzas')
plt.xlabel('Pizza Name')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save as JPEG
plt.savefig(r'C:\Users\tbkcpu\Documents\top_selling_pizzas.jpeg', format='jpeg')

# Show the plot
plt.show()

# Visualization 2- Stacked Bar Chart for Pizza Sales by Size and Category

# Group by pizza_size and pizza_category, summing the quantity
grouped = df.groupby(['pizza_size', 'pizza_category'])['quantity'].sum().unstack().fillna(0)

# Plot the stacked bar chart
grouped.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set3')

plt.title('Pizza Sales by Size and Category')
plt.xlabel('Pizza Size')
plt.ylabel('Total Quantity Sold')
plt.legend(title='Pizza Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the figure as a JPEG in the Documents folder
plt.savefig(r'C:\Users\tbkcpu\Documents\pizza_sales_by_size.jpeg', format='jpeg', dpi=300)

plt.show()

#  Visualization 3: Line Chart for Pizza Sales by Week 

# Convert order_date to datetime if not already
df['order_date'] = pd.to_datetime(df['order_date'])



# Create a 'week' column
df['week'] = df['order_date'].dt.isocalendar().week

# Group by week and sum the quantity
weekly_sales = df.groupby('week')['quantity'].sum()

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(weekly_sales.index, weekly_sales.values, marker='o', linestyle='-', color='teal')

plt.title('Total Pizza Sales by Week')
plt.xlabel('Week Number')
plt.ylabel('Total Pizzas Sold')
plt.grid(True)

# Save the figure
plt.savefig(r'C:\Users\tbkcpu\Documents\weekly_pizza_sales.jpeg', format='jpeg', dpi=300)

plt.show()

#  Visualization 4: Pie Chart for Pizza Sales by Category 

# Group by pizza_category and sum the quantity
category_sales = df.groupby('pizza_category')['quantity'].sum()

# Plot the pie chart with only percentages
plt.figure(figsize=(8, 8))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='Set3', wedgeprops={'edgecolor': 'black'})

plt.title('Pizza Sales by Category')
plt.ylabel('')  # Hide the 'y' label

# Save the figure
plt.savefig(r'C:\Users\tbkcpu\Documents\pizza_sales_by_category.jpeg', format='jpeg', dpi=300)

plt.show()