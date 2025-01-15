def save_dataset(data, output_path):
    """Saves the dataset to a CSV file."""
    data.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
