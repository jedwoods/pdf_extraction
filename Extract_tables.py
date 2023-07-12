import camelot
import csv

def extract_tables_to_csv(pdf_path, output_path):
    # Extract tables from PDF using lattice mode
    tables = camelot.read_pdf(pdf_path, flavor='lattice', pages= 'all',line_scale=75, shift_text=[''],) # increase line_scale to get more tables and detect smaller lines, however a value over 150 will detect text as lines
    """tested Parameters"""
    # flavor='lattice', pages= 'all',, process_background=True
    # shift_text = ['' ] causes weightlessness, meaning the text is not shifted at all, this is the default
    # line_scale = 40, pretty decent
    # flavor = 'stream' reads non defined tables, basicaclly picked out bulleted text in the examples I tried
    # process_background=True, not super good at dececting background lines
    if not tables:
        print("No tables found in the PDF.")
        return
    
    camelot.plot(tables[0], kind='grid').show()

    # Write table data to CSV file
    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for table in tables:
            writer.writerows(table.df.values)
            writer.writerow([])  # Add an empty row between tables

    print(f"Table data extracted and saved to {output_path}")

# Specify the input PDF file path and output CSV file path
pdf_path = '/app/table_extraction/test_files/2020-PERSONAL LINES VARIABLE COMPENSATION AND COMMERCIAL LINES PROFIT  SHARE PROGRAM .pdf'
output_path = 'output.csv'

# Call the extract_tables_to_csv function
extract_tables_to_csv(pdf_path, output_path)
