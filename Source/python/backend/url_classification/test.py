from sklearn import model_selection, preprocessing
from sklearn.ensemble import RandomForestClassifier
import tqdm
import numpy as np

phish_file = 'phishing_urls.txt'
safe_file = 'safe_urls.txt'

with open(phish_file, 'r') as f:
    phishes = [line for line in f]

safes = []
with open(safe_file, encoding='UTF-8', mode='r') as f:
    for idx, line in enumerate(f):
        if idx > 5000:
            break
        safes.append(line)
labels, texts = [], []
for url in tqdm.tqdm(phishes):
    labels.append(1)
    ascii_url = [ord(c) for c in url]
    texts.append(ascii_url)
for url in tqdm.tqdm(safes):
    labels.append(0)
    ascii_url = [ord(c) for c in url]
    texts.append(ascii_url)

train_x, valid_x, train_y, valid_y = model_selection.train_test_split(texts, labels)

encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)

list_lengths = [len(url) for url in train_x]
max_len = max(list_lengths)
for idx, url in enumerate(tqdm.tqdm(train_x)):
    pad_size = max_len - len(url)
    pad = [-1 for val in range(pad_size)]
    url = url + pad
    train_x[idx] = url

classifier = RandomForestClassifier(n_estimators=100, random_state=0, verbose=1)
classifier.fit(train_x, train_y)

for idx, url in enumerate(valid_x):
    pad_size = max_len - len(url)
    pad = [-1 for val in range(pad_size)]
    url = url + pad
    valid_x[idx] = url

for idx, url in enumerate(valid_x):
    if len(url) > max_len:
        valid_x.remove(url)

y_pred = classifier.predict(valid_x)

# correct_list = [idx for idx, val in enumerate(valid_y) if val == y_pred[idx]]
# accuracy = len(correct_list)/len(y_pred)

#TEMPORARY TESTING
temp_urls = ['www.spotify.com/us/token-redirect/?url=/us/password-reset/change/#NApECiwKDVNwb3RpZnktdXNlcnMSEWJyYXlkZW5vc2Jvcm5lLXVzGgOoAQElUt7vXBIUCmA41Wbh4ehgv4B1SrkgmNpDqbg',
             'www.netflix.com/password?nftoken=BQAbAAEBEIQZQz8OsCA6LgEJ6jZAGTCAkPt2iHL8ZoIcmrcMRQQA2Ll3jK424M2deA7rNWb4b68m%2BvV7ifhi2NhCcuV%2B385L39Zjoj6FiucA4ANljYXfUJoLPuaXCR%2B1Xx4H5FZi7RkKlH7ACsXi7bBp6ZcqDV5ifqXTTK3%2F9J2w0QW7dcNxkRbLgEWteX%2BFoVAeK8D85XBBWiZsUsKIrf7wdnpjUYuSvw%3D%3D&lnktrk=EMP&g=C87532F97822C067BD133A7511BB955764513C37&lkid=URL_PASSWORD',
             'canopy.uc.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1',
             'www.google.com',
             'www.theninjahunterz.com/~gntcncum/D/H/L/EX-Press/document-/=46d37d3ffe90b3e56482e0726a2ff729cad88d5916aeb3e4a2a1d3c8889afd000dffdd18fe1509450bde3c1eebdef4be/tracking2.php',
             '100hot.com/hot100/ws/results/Web/92!FE5%20Montreal/1/302363/RightNav/Relevance/iq=true/zoom=off/qlnk=1/_iceUrlFlag=7?_IceUrl=true'
             ]

test_urls = []
for url in tqdm.tqdm(temp_urls):
    labels.append(1)
    ascii_temp_url = [ord(c) for c in url]
    test_urls.append(ascii_temp_url)
for idx, url in enumerate(test_urls):
    pad_size = max_len - len(url)
    pad = [-1 for val in range(pad_size)]
    url = url + pad
    test_urls[idx] = url
    if len(url) > max_len:
        test_urls.remove(url)


x = classifier.predict(test_urls)

# print(accuracy)
x=1
