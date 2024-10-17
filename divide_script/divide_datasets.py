import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, on_bad_lines='skip', dtype={'phone': str})
    return df


def separate_data(df):
    complete_data = df.dropna(subset=['domain', 'address', 'city', 'country_code', 'phone', 'region_code', 'region_name'])
    incomplete_data = df[df.isnull().any(axis=1)]

    return complete_data, incomplete_data

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

def main():
   
    file_path = 'merged_dataset.csv' 
    df = load_data(file_path)
    
    complete_data, incomplete_data = separate_data(df)
    
    save_data(complete_data, 'complete_data.csv')
    incomplete_domains = incomplete_data[['domain']].dropna()
    save_data(incomplete_domains, 'incomplete_domains.csv')

if __name__ == "__main__":
    main()
