# Removes the header line from csv files
import csv, os

#create directory for headerless files
os.makedirs('headerRemoved', exist_ok=True)

#loop through every csv file in cwd
for file_name in os.listdir('.'):
    if file_name.endswith('.csv'):

        print(f'Removing headers from {file_name}...')

        csv_rows = []
        #Open input file
        with open(file_name, 'r') as input_file:
            input_reader = csv.reader(input_file)
            for row in input_reader:
                if input_reader.line_num == 1:
                    continue # skip header row
                csv_rows.append(row)

        # Ommiting empty files / files with only header
        if len(csv_rows) > 0:
        #Create new output file
            with open(os.path.join('headerRemoved', file_name), 'w', newline='') as output_file:
                csv_writer = csv.writer(output_file)
                #write rows into new file
                for row in csv_rows:
                    csv_writer.writerow(row)
            

                
