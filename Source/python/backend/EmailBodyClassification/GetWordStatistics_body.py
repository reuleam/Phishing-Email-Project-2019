import nltk
import statistics
import scipy.stats as st


def text_extract(phish_subjects, safe_subjects):
    with open(phish_subjects, 'r') as f:
        phishes = [line for line in f]

    with open(safe_subjects, 'r') as f:
        safe = [line for line in f]

    return phishes, safe


def main():
    phish_subjects = 'EmailBodyClassification/phishBodies.txt'
    safe_subjects = 'EmailBodyClassification/safeBodies.txt'
    threat_subjects = 'Detector/body_threat_words.txt'
    phishes, safe = text_extract(phish_subjects, safe_subjects)
    with open(threat_subjects) as f:
        threat_words = [line.rstrip('\n') for line in f]

    phishwords = [nltk.word_tokenize(line) for line in phishes]
    safewords = [nltk.word_tokenize(line) for line in safe]

    phish_lengths = [len(line) for line in phishwords]
    safe_lengths = [len(line) for line in safewords]

    phish_threats = []
    safe_threats = []
    print('Getting Threats')
    for line in phishwords:
        phish_threats.append([word for word in line if word in threat_words or word.lower() in threat_words])
    for line in safewords:
        safe_threats.append([word for word in line if word in threat_words or word.lower() in threat_words])

    phish_threat_lengths = [len(line) for line in phish_threats]
    safe_threat_lengths = [len(line) for line in safe_threats]

    threats_per_word_phish = []
    threats_per_word_safe = []

    for idx, length in enumerate(phish_threat_lengths):
        if length == 0:
            threats_per_word_phish.append(0)
        else:
            threats_per_word_phish.append(length/phish_lengths[idx])

    for idx, length in enumerate(safe_threat_lengths):
        if length == 0:
            threats_per_word_safe.append(0)
        else:
            threats_per_word_safe.append(length/safe_lengths[idx])

    p_avg = statistics.mean(threats_per_word_phish)
    p_stddev = statistics.stdev(threats_per_word_phish)
    s_avg = statistics.mean(threats_per_word_safe)
    s_stddev = statistics.stdev(threats_per_word_safe)

    print('Average Phish Threats: ' + str(p_avg) + '\n')
    print('Phish Threats Standard Deviation: ' + str(p_stddev) + '\n')
    print('Average Safe Threats: ' + str(s_avg) + '\n')
    print('Safe Threats Standard Deviation: ' + str(s_stddev) + '\n')


    myp = .42

    z = (myp - p_avg) / p_stddev
    percent = st.norm.cdf(z)
    print("There is a " + str(percent) + ' chance of this being a phishing email')


if __name__ == '__main__':
    main()
