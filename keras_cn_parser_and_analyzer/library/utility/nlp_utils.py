from snownlp import SnowNLP


def print_snow(text):
    s = SnowNLP(text)

    print('words: ', s.words)
    print('tags: ', s.tags)
    print('sentiment: ', s.sentiments)
    print('pinyin: ', s.pinyin)
    print('han: ', ' '.join(s.han.split('\n')))
    print('keywords(3): ', s.keywords(3))
    print('summary(3): ', s.summary(3))
    print('sentences: ', s.sentences)

    print('+++++++++++++++++++++++++++++++++++++')


