import json


def main():
    filename = 'phishing_emails.json'

    with open(filename) as json_file:
        data = json.load(json_file)['phishing_emails']
    bodies = [email['body'] for email in data]

    with open('phishBodies.txt', 'w') as f:
        for body in bodies:
            try:
                f.write(body)
            except:
                x=1
    x=1


if __name__ == '__main__':
    main()
