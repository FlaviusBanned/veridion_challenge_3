import pandas as pd

def load_facebook_data(file_path):
    df = pd.read_csv(file_path, on_bad_lines='skip') 
    return df

def extract_columns(df):
    columns_to_extract = ['domain', 'address', 'city', 'country_code', 'phone', 'region_code', 'region_name']
    extracted_data = df[columns_to_extract]
    
    return extracted_data

def save_data(extracted_data, output_file):
    extracted_data.to_csv(output_file, index=False)

def main():
    facebook_df = load_facebook_data('facebook_dataset.csv')
    extracted_data = extract_columns(facebook_df)
    
    save_data(extracted_data, 'extracted_facebook_data.csv')

if __name__ == "__main__":
    main()
