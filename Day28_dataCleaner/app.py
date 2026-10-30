import pandas as pd

def load_data(file_path):
    """Load data from CSV file"""
    
    try:
        df = pd.read_csv(file_path)
        print("Data Loaded successfully")
        return df
    except Exception as e:
        print("Error loading the data:",e)
        return None
    
def clean_data(df):
    '''Clean the Data'''
    print("\n---Cleaning Data---")
    print("Initial Shape:", df.shape)
    
    # Handle Missing Values
    print("\nHandling Missing Values...")
    df = df.dropna() # Drop rows with Missing values
    print("After Dropping the Missing Values:", df.shape)
    
    # Remove Duplicates
    print("\nRemoving Duplicates...")
    df = df.drop_duplicates()
    print("After Removing Duplicates:",df.shape)
    
    return df

def save_data(df, output_path):
    """Save the Cleaned data into new csv file"""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print("Error saving data:",e)
        
def main():
    print("Welcome to the Data Cleaner Tool")
    
    #Input File
    input_file = input("Enter The path to csv file:")
    df = load_data(input_file)
    if df is None:
        return
    
    # Show Initial Data
    print("\n---Initial Data---")
    print(df.head())
    
    # Clean the Data
    df = clean_data(df)
    
    # Save Cleaned Data
    output_file = input("\n Enter the Path to save the cleaned CSV data: ")
    save_data(df,output_file)
    
if __name__=="__main__":
    main()