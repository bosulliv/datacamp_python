def filter_lines(text, first_chars):
    """Filter lines by beginning characters (case sensitive)

    :param text:  multi-line text to filter
    :param first_chars: required characters for line to start with to be returned
    :return: text with only lines starting with first_chars included

    >>> text = 'humpty dumpty\\nsat on a wall\\nhumpty dumpty\\nhad a great fall'
    >>> filter_lines(text, 'h')
    'humpty dumpty\\nhumpty dumpty\\nhad a great fall'

    >>> filter_lines(text, 'humpty')
    'humpty dumpty\\nhumpty dumpty'
    """
    n_chars = len(first_chars)
    lines = text.split('\n')

    filtered_lines = [l for l in lines if l[:n_chars] == first_chars]

    return '\n'.join(filtered_lines)