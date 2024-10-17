import pandas as pd

def load_website_data(file_path):
    df = pd.read_csv(file_path, sep=';', on_bad_lines='skip')  
    return df

def extract_columns(df):
    columns_to_extract = ['root_domain', 'main_city', 'main_country', 'main_region', 'phone']
    extracted_data = df[columns_to_extract]
    
    return extracted_data

def save_data(extracted_data, output_file):
    extracted_data.to_csv(output_file, index=False)

def main():
    website_df = load_website_data('website_dataset.csv')  
    extracted_data = extract_columns(website_df)
    save_data(extracted_data, 'extracted_website_data.csv')  

if __name__ == "__main__":
    main()
