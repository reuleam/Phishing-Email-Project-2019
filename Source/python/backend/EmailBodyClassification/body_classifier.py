from nltk.corpus import stopwords
import nltk
import operator

def text_extract(phish_bodies, safe_bodies):

    with open(phish_bodies, 'r') as f:
        phishes = [line for line in f]

    with open(safe_bodies, 'r') as f:
        safe = [line for line in f]

    return phishes, safe


def count_words(big_phishwords, big_safewords, stop):
    phishwords = [word for word in big_phishwords if len(word) > 2 and word not in stop and word.lower() not in stop]
    safewords = [word for word in big_safewords if len(word) > 2 and word not in stop and word.lower() not in stop]

    phish_freq = {}
    safe_freq = {}

    for word in phishwords:
        if word not in phish_freq.keys():
            phish_freq.update({word: 1})
        else:
            phish_freq[word] += 1
    for word in safewords:
        if word not in safe_freq.keys():
            safe_freq.update({word: 1})
        else:
            safe_freq[word] += 1

    max_phish = dict(sorted(phish_freq.items(), key=operator.itemgetter(1), reverse=True)[:1000])
    max_safe = dict(sorted(safe_freq.items(), key=operator.itemgetter(1), reverse=True)[:1000])

    common_terms = set(max_phish.keys()) & set(max_safe.keys())

    return max_phish, max_safe, common_terms

def main():
    phish_bodies = 'phishBodies.txt'
    safe_bodies = 'safeBodies.txt'
    phishes, safe = text_extract(phish_bodies, safe_bodies)
    stop = set(stopwords.words('english'))
    phishwords = nltk.word_tokenize(' '.join(phishes))
    safewords = nltk.word_tokenize(' '.join(safe))
    p1, s1, c1 = count_words(phishwords, safewords, stop)

    threats = list(set(p1) - c1)
    with open('body_threat_words.txt', 'w') as f:
        for threat in threats:
            f.write(str(threat) + '\n')
    x=1


if __name__ == '__main__':
    main()
