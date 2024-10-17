import pandas as pd
def load_data(file1, file2, file3):   
    df1 = pd.read_csv(file1, on_bad_lines='skip', dtype={'phone': str}) 
    df2 = pd.read_csv(file2, on_bad_lines='skip', dtype={'phone': str}) 
    df3 = pd.read_csv(file3, on_bad_lines='skip', dtype={'phone': str}) 
    
    return df1, df2, df3

def merge_data(df1, df2, df3):
    df3 = df3.rename(columns={
        'root_domain': 'domain',
        'main_city': 'city',
        'main_country': 'country_code',
        'main_region': 'region_name'
    })
    df1 = df1[['domain', 'address', 'city', 'country_code', 'phone', 'region_code', 'region_name']]
    df2 = df2[['domain', 'address', 'city', 'country_code', 'phone', 'region_code', 'region_name']]
    df3 = df3[['domain', 'city', 'country_code', 'region_name', 'phone']] 
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    
    return merged_df

def save_data(merged_df, output_file):
    merged_df.to_csv(output_file, index=False)

def main():
    df1, df2, df3 = load_data('extracted_facebook_data.csv', 'extracted_google_data.csv', 'extracted_website_data.csv')
    merged_df = merge_data(df1, df2, df3)
    save_data(merged_df, 'merged_dataset.csv')

if __name__ == "__main__":
    main()
