import nltk
import scipy.stats as st

class ThreatDetector:
    def __init__(self, subject_threat_words_filename='subject_threat_words.txt', body_threat_words_filename='body_threat_words.txt'):
        self.p_avg_subject_threats_per_word = 0.39198340154041067
        self.p_stddev_subject_threats_per_word = 0.2301476308224313
        self.s_avg_subject_threats_per_word = 0.041405169117432514
        self.s_stddev_subject_threats_per_word = 0.09456239042678115

        self.p_avg_body_threats_per_word = 0.10762692505398647
        self.p_stddev_body_threats_per_word = 0.13055473517793445
        self.s_avg_body_threats_per_word = 0.005167319794593551
        self.s_stddev_body_threats_per_word = 0.038670845208877064

        self.subject_threats_per_word = None
        self.body_threats_per_word = None

        dirname = os.path.dirname(__file__)
        subject_threat_words_filename = os.path.join(dirname, subject_threat_words_filename)
        body_threat_words_filename = os.path.join(dirname, body_threat_words_filename)
        self.body_threats = []
        self.subject_threats = []
        with open(body_threat_words_filename, 'r') as f:
            self.body_threat_words = [line.rstrip() for line in f]
        with open(subject_threat_words_filename, 'r') as f:
            self.subject_threat_words = [line.rstrip() for line in f]

    def detect_subject(self, subject_string):
        subject_words = nltk.word_tokenize(subject_string)
        self.subject_threats = [word for word in subject_words if word in self.subject_threat_words
                                or word.lower() in self.subject_threat_words]
        if len(subject_words) == 0:
            self.subject_threats_per_word = 0
        else:
            self.subject_threats_per_word = len(self.subject_threats) / len(subject_words)

    def detect_body(self, body_string):
        body_words = nltk.word_tokenize(body_string)
        self.body_threats = [word for word in body_words if word in self.body_threat_words
                             or word.lower() in self.body_threat_words]
        if len(body_words) == 0:
            self.body_threats_per_word = 0
        else:
            self.body_threats_per_word = len(self.body_threats) / len(body_words)

    def return_threats(self):
        return self.subject_threats, self.body_threats

    def return_stats(self):
        z_score_subject = (self.subject_threats_per_word - self.p_avg_subject_threats_per_word) / self.p_stddev_subject_threats_per_word
        z_score_body = (self.body_threats_per_word - self.p_avg_body_threats_per_word) / self.p_stddev_body_threats_per_word
        subject_percent = st.norm.cdf(z_score_subject)
        body_percent = st.norm.cdf(z_score_body)
        if self.body_threats_per_word > 0 and self.subject_threats_per_word > 0:
            return subject_percent, body_percent
        elif self.body_threats_per_word == 0 and self.subject_threats_per_word == 0:
            return 0, 0
        elif self.body_threats_per_word == 0:
            return subject_percent, 0
        elif self.subject_threats_per_word == 0:
            return 0, body_percent

def main():
    sub_file = 'subject_threat_words.txt'
    bod_file = 'body_threat_words.txt'

    sub_string_phish = 'Your Chase Online Access placed on Restriction.'
    bod_string_phish = 'Dear Esteem Customer, YOUR ACCOUNT HAS NOW BEEN TEMPORARILY RESTRICTED. During our regularly scheduled account maintenance and verification procedures,  We noticed some unusual activity on your Chase account, There has been a recent change of account email from an unknown device on  For security purpose, We ve temporarily disabled access to your account to secure your account. To continue using this account, We need you to confirm ownership of this a...'

    sub_string_safe = 'Your E-statement is ready'
    bod_string_safe = 'Thank you for choosing River Valley Credit Union where we encourage you to Dream Big!  We appreciate your business. Your credit union eStatement is ready to view. Please log into ItsMe247 Online Banking and click the E-Statements link.'

    detector = ThreatDetector(sub_file, bod_file)
    detector.detect_subject(sub_string_phish)
    detector.detect_body(bod_string_phish)
    sub_threats, bod_threats = detector.return_threats()

    detector2 = ThreatDetector(sub_file, bod_file)
    detector2.detect_subject(sub_string_safe)
    detector2.detect_body(bod_string_safe)
    sub_threats2, bod_threats2 = detector2.return_threats()
    x=1


if __name__ == '__main__':
    main()
