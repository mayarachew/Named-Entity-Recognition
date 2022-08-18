# """Apply BERT to improve quality."""
# from enchant.checker import SpellChecker # type: ignore
# from typing import Tuple, List

# def apply_bert(text: str) -> Tuple[str, str, List[str]]:
#     """Transform data to json and add it to a .txt file
#     Args:
#         text (str): text extracted from image
#     Returns:
#         text (str): text after BERT correction
#     """

#     spell_checker = SpellChecker("en_US")

#     words = text.split()

#     punctuation_list = ["!", ",", ".", "\"", "?", '(', ')', '*', '']
#     incorrect_words = [word for word in words if not spell_checker.check(word) and word not in punctuation_list]
    
#     improved_text = text
#     for word in incorrect_words:
#         improved_text = text.replace(word, '[INCORRECT]')

#     suggested_words = [spell_checker.suggest(word) for word in incorrect_words]

#     return text, improved_text, suggested_words