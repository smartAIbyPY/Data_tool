from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

def preprocess_data(data):
    """Preprocesses the data by encoding categorical variables and scaling numerical ones."""
    # One-hot encode categorical variables
    cat_columns = data.select_dtypes(include=['object']).columns
    if not cat_columns.empty:
        data = pd.get_dummies(data, columns=cat_columns)
    
    # Standardize numerical data
    num_columns = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    data[num_columns] = scaler.fit_transform(data[num_columns])
    
    return data
