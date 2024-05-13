import pandas as pd
import re

def remove_links(text):
    # Regular expression pattern to match URLs
    url_pattern = r'https?://\S+|www\.\S+'
    return re.sub(url_pattern, '', text)

def remove_links_from_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Print column names
    print("Column names:", df.columns)
    
    # Modify the following line with the correct column name containing the text
    text_column_name = input("Enter the name of the column containing the text: ")
    
    # Apply remove_links function to the specified column
    df[text_column_name] = df[text_column_name].apply(lambda x: remove_links(str(x)))
    
    # Save the modified DataFrame back to the Excel file
    output_file_path = file_path.split('.')[0] + '_without_links.xlsx'
    df.to_excel(output_file_path, index=False)
    
    return output_file_path

# Example usage:
uploaded_file_path = '/content/hindi data set new.xlsx'
output_file_path = remove_links_from_excel(uploaded_file_path)
print(f"Links removed from '{uploaded_file_path}'. Output saved to '{output_file_path}'")
