import os
import re
import csv
import pypdf

def find_the_phone_number():
  phone_number = ''
  phone_number_pattern = r'\d{3}\.\d{3}\.\d{3}'
  google_drive_url_chars = []
  # Read the csv
  try:
    with open(file=os.path.join('exercise_materials', 'find_the_link.csv'), encoding="utf-8") as csv_file:
      csv_data = csv.reader(csv_file)
      row_index = 0
      for row_index, data_row in enumerate(csv_data):
        for row_item_index in range(len(data_row)):
          if row_index == row_item_index:
            google_drive_url_chars.append(data_row[row_item_index])
        row_index += 1
  except Exception as e:
    print(e)
  # Construct google drive url
  google_drive_url = ''.join(google_drive_url_chars)
  # Attempt to fetch 
  print(f"Google Drive URL: {google_drive_url}")
  # Opening the downloaded file
  try:
    with open(file=os.path.join('exercise_materials', 'Find_the_Phone_Number.pdf'), mode="rb") as pdf_file:
      pdf_reader = pypdf.PdfReader(pdf_file)
      for page_index in range(pdf_reader.get_num_pages()):
        pdf_page_content = pdf_reader.get_page(page_index)
        phone_number_result = re.search(pattern=phone_number_pattern, string=pdf_page_content.extract_text()) 
        if phone_number_result != None:
          phone_number = phone_number_result.group()
  except Exception as e:
    print(e)
    
  print(f'Phone Number: {phone_number}')
  

if __name__ == "__main__":
  find_the_phone_number()