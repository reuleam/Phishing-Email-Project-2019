from Source.python.backend.Detector.PhishDetector import ThreatDetector


def text_extract_s(phish_subjects, safe_subjects):
    with open(phish_subjects, 'rb') as f:
        phishes = [line.decode("utf-8") for line in f]

    with open(safe_subjects, 'r') as f:
        safe = [line for line in f]

    return phishes, safe


def text_extract_b(phish_subjects, safe_subjects):
    with open(phish_subjects, 'r') as f:
        phishes = [line for line in f if len(line) > 2]

    with open(safe_subjects, 'r') as f:
        safe = [line for line in f if len(line) > 2]

    return phishes, safe


def main():
    phish_subjects = 'SubjectLineClassification/phishSubjects.txt'
    safe_subjects = 'SubjectLineClassification/safeSubjectLines.txt'
    phish_body = 'EmailBodyClassification/phishBodies.txt'
    safe_body = 'EmailBodyClassification/safeBodies.txt'

    phishes_s, safes_s = text_extract_s(phish_subjects, safe_subjects)
    phishes_b, safes_b = text_extract_b(phish_body, safe_body)

    sub_cutoff = .5
    bod_cutoff = .5
    sub_successes = 0
    bod_successes = 0
    total = 0
    for sub, bod in zip(phishes_s, phishes_b):
        detector = ThreatDetector()
        detector.detect_subject(sub)
        detector.detect_body(bod)
        sub_percent, bod_percent = detector.return_stats()
        sub_percent = (sub_percent - .5) * 2
        bod_percent = (bod_percent - .5) * 2
        if sub_percent > sub_cutoff:
            sub_successes += 1
        if bod_percent > bod_cutoff:
            bod_successes += 1
        total += 1

    print('Sub accuracy', sub_successes/total)
    print('Bod accuracy', bod_successes/total)

    sub_false_pos = 0
    bod_false_pos = 0
    total = 0
    for sub, bod in zip(safes_s, safes_b):
        detector = ThreatDetector()
        detector.detect_subject(sub)
        detector.detect_body(bod)
        sub_percent, bod_percent = detector.return_stats()
        sub_percent = (sub_percent - .5) * 2
        bod_percent = (bod_percent - .5) * 2
        if sub_percent > sub_cutoff:
            sub_false_pos += 1
        if bod_percent > bod_cutoff:
            bod_false_pos += 1
        total += 1

    print('Sub false pos', sub_false_pos/total)
    print('Bod false pos', bod_false_pos/total)


if __name__ == '__main__':
    main()
