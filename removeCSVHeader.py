import csv, os
from pathlib import Path

for file in os.listdir():
    if file.endswith('.csv'):

        #Open input file
        open_file = open(file)

        #Create new output file
        output_path = Path('no_headers_' + os.path.basename(file))
        output_file = open(output_path, 'w', newline='')

        #Read contents
        file_reader = csv.reader(open_file)
        data = list(file_reader)

        #If only header or empty
        if len(data) <= 1:
            output_file.close()
            open_file.close()
            if output_path.exists():
                os.remove(output_path)
            continue
        
        output_writer = csv.writer(output_file)
        for row in data[1:]:#skip header
            output_writer.writerow(row)

        #Closing files
        output_file.close()
        open_file.close()

                
