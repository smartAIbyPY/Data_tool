def clean_missing_data(data):
    """Drops rows with missing values."""
    return data.dropna()

def remove_duplicates(data):
    """Removes duplicate rows."""
    return data.drop_duplicates()
