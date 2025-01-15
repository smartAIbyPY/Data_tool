import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(data):
    """Plots distributions of numerical columns."""
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(data[column], kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()

def plot_correlation_heatmap(data):
    """Plots a correlation heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
