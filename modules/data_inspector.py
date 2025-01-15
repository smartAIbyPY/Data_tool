def inspect_data(data):
    """Displays basic dataset insights."""
    print("\n--- Data Overview ---")
    print(data.head())
    print("\n--- Data Types ---")
    print(data.dtypes)
    print("\n--- Missing Values ---")
    print(data.isnull().sum())
    print("\n--- Summary Statistics ---")
    print(data.describe())
