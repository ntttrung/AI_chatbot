# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# import re
# from typing import Any, Dict, List, Text

# from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
# from rasa.nlu.training_data import Message

# from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES
# from Sudachipy import dictionary
# from Sudachipy import tokenizer
# class JapaneseTokenizer(Tokenizer):

#     provides = [TOKENS_NAMES[attribute] for attribute in MESSAGE_ATTRIBUTES]

#     def __init__(self, component_config: Dict[Text, Any] = None) -> None:
#         super().__init__(component_config)
#         self.tokenizer_obj = dictionary.Dictionary().create()
#         self.mode = tokenizer.Tokenizer.SplitMode.A

#     def tokenize(self, message: Message, attribute: Text) -> List[Token]:
#         text = message.get(attribute)
#         words = [m.surface() for m in self.tokenizer_obj.tokenize(text, self.mode)]

#         return self._convert_words_to_tokens(words, text)


