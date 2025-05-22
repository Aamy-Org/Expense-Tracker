import matplotlib.pyplot as plt

categories = {'apples':35, 'bananas':25, 'cherries':25, 'dates':15}

plt.figure(figsize=(5,6))
plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
plt.title('Fruit Distribution')
plt.savefig('fruit_distribution.png')
plt.show() 