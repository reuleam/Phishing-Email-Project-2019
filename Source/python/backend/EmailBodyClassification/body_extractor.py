import csv


def csv_extract(input_file, old_file, new_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        my_new_info = [line[1] for line in reader if 'Subject' not in line]

    with open(old_file, 'r') as f:
        my_old_info = [line for line in f]

    new_info = my_new_info + my_old_info

    with open(new_file, 'w') as f:
        for body in new_info:
            try:
                f.write('\n' + body)
            except:
                x=1


def main():
    outlook_inbox_file = 'ValidEmailSource\OUTLOOK\inbox.csv'
    outlook_classes_file = 'ValidEmailSource\OUTLOOK\deleted.csv'
    outlook_deleted_file = 'ValidEmailSource\OUTLOOK\deleted.csv'

    new_file = 'safeBodies.txt'

    with open(new_file, 'w') as f:
        f.write('')

    csv_extract(outlook_inbox_file, new_file, new_file)
    csv_extract(outlook_classes_file, new_file, new_file)
    csv_extract(outlook_deleted_file, new_file, new_file)


if __name__ == '__main__':
    main()
