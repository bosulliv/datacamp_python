from .token_utils import tokenize
from collections import Counter
from .document import Document

# Define Document class
class SocialMedia(Document):
    """A class for text analysis of tweets
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Call Parent Class
        super().__init__(text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()


    def _count_hashtags(self):
        return self._filter_word_counts(self.word_counts, '#')

    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return self._filter_word_counts(self.word_counts, first_char='@')
    
    
    def _filter_word_counts(self, word_counts, first_char):
        """Filter Document.word_counts by the first character of the word

        :param word_counts: the word_counts attribute of a Document class instance
        :param first_char: only keep word counts that start with this character

        >>> # How to filter to only words that start with 'A'
        >>> filter_word_counts(document.word_counts, 'A')
        """
        return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})
    