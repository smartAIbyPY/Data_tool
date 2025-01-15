import argparse
from modules.data_loader import load_dataset
from modules.data_inspector import inspect_data
from modules.data_visualizer import plot_distributions, plot_correlation_heatmap
from modules.data_cleaner import clean_missing_data, remove_duplicates
from modules.data_preprocessor import preprocess_data
from modules.data_saver import save_dataset

def main():
    parser = argparse.ArgumentParser(description="Data Tool for Loading, Inspecting, Cleaning, and Preprocessing Datasets.")
    parser.add_argument("file", help="Path to the dataset (CSV or Excel).")
    parser.add_argument("--output", default="processed_dataset.csv", help="Path to save the processed dataset.")
    parser.add_argument("--inspect", action="store_true", help="Inspect the dataset.")
    parser.add_argument("--visualize", action="store_true", help="Visualize the dataset.")
    parser.add_argument("--clean", action="store_true", help="Clean the dataset.")
    parser.add_argument("--preprocess", action="store_true", help="Preprocess the dataset.")
    
    args = parser.parse_args()
    
    # Load the dataset
    data = load_dataset(args.file)
    
    # Perform actions based on CLI arguments
    if args.inspect:
        inspect_data(data)
    
    if args.visualize:
        plot_distributions(data)
        plot_correlation_heatmap(data)
    
    if args.clean:
        data = clean_missing_data(data)
        data = remove_duplicates(data)
        print("Data cleaned.")
    
    if args.preprocess:
        data = preprocess_data(data)
        print("Data preprocessed.")
    
    # Save the dataset
    save_dataset(data, args.output)

if __name__ == "__main__":
    main()
