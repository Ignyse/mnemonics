import csv
class UseData:
    fieldnames = ['word','meaning','mnemonic']

    # returns dictionary
    @staticmethod
    def read_in_german(txtfile):
        data = []
        with open (txtfile, mode='r',encoding = 'utf-8') as file:
            csv_reader= csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
    
    # update the mnemonic
    @staticmethod
    def update_in_german(txtfile, row, new_mnemonic):
        print(row)
        data = UseData.read_in_german(txtfile)
        data[row]['mnemonic'] = new_mnemonic
        with open(txtfile, mode='w', encoding='utf-8', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=UseData.fieldnames)
            # Write the headers first
            csv_writer.writeheader()
            csv_writer.writerows(data)  # Write the updated rows