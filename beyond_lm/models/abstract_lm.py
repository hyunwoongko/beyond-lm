import os
import re
from typing import Tuple, Union

import openai


class AbstractLM(object):
    def __init__(self, lang: str, verbose: bool = True, api_key: str = None):
        assert lang in ["en", "ko"], "param `lang` must be one of ['en', 'ko']"
        self.lang = lang
        self.verbose = verbose

        if api_key is None:
            openai.api_key = os.environ["OPENAI_API_KEY"]
        else:
            openai.api_key = api_key

    def ask(self, question: str, *args, **kwargs) -> Union[str, Tuple[str, str]]:
        """
        Ask a question to the model.

        Args:
            question (str): question to ask the model.

        Returns:
            str: answer from the model.
        """
        raise NotImplementedError

    def scenario(self) -> str:
        """
        Return the scenario of the experiment.

        Returns:
            str: scenario of the experiment.
        """
        return "Scenario: " + re.sub(
            r"\s+", " ", self.__doc__.split("Scenario:")[-1].strip()
        )
