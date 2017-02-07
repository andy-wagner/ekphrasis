from classes.SocialTokenizer import SocialTokenizer
from classes.TextPreProcessor import TextPreProcessor
from dicts.emoticons import emoticons

text_processor = TextPreProcessor(
    backoff=['url', 'email', 'percent', 'money', 'phone', 'user', 'time', 'url', 'date', 'number'],
    include_tags={"hashtag", "allcaps", "elongated", "repeated", 'emphasis', 'censored'},
    fix_html=True,
    segmenter="twitter",
    corrector="twitter",
    unpack_hashtags=True,
    unpack_contractions=True,
    spell_correct_elong=False,
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    dicts=[emoticons])

sentences = [
    "CANT WAIT for the new season of #TwinPeaks ＼(^o^)／ !!! #DavidLynch #tvseries :) ",
    "The new #johndoe suuuuucks!!! WAISTED $10... #badmovies >:/",
]

for s in sentences:
    print(" ".join(text_processor.pre_process_doc(s)))