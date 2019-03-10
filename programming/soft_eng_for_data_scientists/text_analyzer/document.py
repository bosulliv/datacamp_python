from .token_utils import tokenize
from .counter_utils import plot_counter
from collections import Counter

# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        self.text = text
        # Tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Perform word count with non-public count_words method
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)
    
    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)
    
    
    def plot_counts(self, attribute='word_counts', n_most_common=5):
        """ Plot most common elements of a ``collections.Counter`` instance attribute

        :param attribute: name of ``Counter`` attribute to use as object to plot
        :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
        :return: None; a plot is shown using matplotlib

        >>> doc = Document("duck duck goose is fun when you're the goose")
        >>> doc.plot_counts('word_counts', n_most_common=5)  # same as default call
        """
        plot_counter(getattr(self, attribute), n_most_common)
