from nltk.corpus import stopwords
import nltk
import operator

def text_extract(phish_subjects, safe_subjects):

    with open(phish_subjects, 'rb') as f:
        phishes = [line.decode("utf-8") for line in f]

    with open(safe_subjects, 'r') as f:
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
    phish_subjects = 'phishSubjects.txt'
    safe_subjects = 'safeSubjectLines.txt'
    phishes, safe = text_extract(phish_subjects, safe_subjects)
    stop = set(stopwords.words('english'))
    phishwords = nltk.word_tokenize(' '.join(phishes))
    safewords = nltk.word_tokenize(' '.join(safe))
    p1, s1, c1 = count_words(phishwords, safewords, stop)

    threats = list(set(p1) - c1)
    x=1


if __name__ == '__main__':
    main()

