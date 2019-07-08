import csv


def text_extract(input_file, old_file, new_file):
    with open(input_file, encoding='UTF-8') as f:
        my_new_info = [line.replace('Subject: ', '') for line in f if "Subject: " in line and "UTF" not in line]

    with open(old_file, 'r') as f:
        my_old_info = [line for line in f if "UTF" not in line]

    new_info = my_new_info + my_old_info

    with open(new_file, 'w') as f:
        for subject in new_info:
            f.write(subject)


def csv_extract(input_file,old_file, new_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        my_new_info = [line[0] for line in reader if 'Subject' not in line]

    with open(old_file, 'r') as f:
        my_old_info = [line for line in f]

    new_info = my_new_info + my_old_info

    with open(new_file, 'w') as f:
        for subject in new_info:
            f.write('\n' + subject)

def filter_subjects(filename):
    with open(filename, 'r') as f:
        filtered = []
        for line in f:
            if line != '':
                x=1
def main():
    outlook_inbox_file = 'OUTLOOK\inbox.csv'
    outlook_classes_file = 'OUTLOOK\deleted.csv'
    outlook_deleted_file = 'OUTLOOK\deleted.csv'
    gmail_Archived = 'Archived.mbox'
    gmail_Inbox = 'Archived.mbox'
    gmail_Sent = 'Sent.mbox'

    new_file = 'test_subjects.txt'

    with open(new_file, 'w') as f:
        f.write('')
    csv_extract(outlook_inbox_file, new_file, new_file)
    csv_extract(outlook_deleted_file, new_file, new_file)
    text_extract(gmail_Archived, new_file, new_file)
    text_extract(gmail_Inbox, new_file, new_file)
    text_extract(gmail_Sent, new_file, new_file)

    filter_subjects(new_file)



if __name__ == '__main__':
    main()
