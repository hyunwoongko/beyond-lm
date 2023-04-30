import re
from typing import Tuple

import openai

from beyond_lm.models.abstract_lm import AbstractLM
from beyond_lm.prompts.socal_lm import KOREAN, ENGLISH


class SocialLM(AbstractLM):
    """
    Question:
        Can language model be further improved by social communication?

    Scenario:
        The questioner is a human, and the responder is a responder language model.
        Given a specific question, specify N roles that are suitable for that question.
        Each language model corresponding to each role has a single speaking opportunity.
        After the discussion of the language models is over,
        The responder model synthesizes the contents of the discussion as a single answer.
    """

    def __init__(self, lang: str, verbose: bool = True, api_key: str = None):
        super().__init__(lang, verbose, api_key)
        if lang == "en":
            self.prompts = ENGLISH
        elif lang == "ko":
            self.prompts = KOREAN
        else:
            raise NotImplementedError

    def ask(self, question: str, n: int) -> Tuple[str, str]:
        """
        Ask a question to the model.

        Args:
            question (str): question to ask the model.
            n (int): number of debaters.

        Returns:
            Tuple[str, str]: Answer of Social LM and ChatGPT.
        """

        roles = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.prompts["role_specifying_user"].format(
                        Q=question,
                        N=str(n),
                    ),
                },
                {
                    "role": "assistant",
                    "content": self.prompts["role_specifying_assistant"].format(
                        N=str(n),
                    ),
                },
            ],
        )
        roles = self.prompts["role_specifying_postprocess"](
            roles["choices"][0]["message"]["content"]
        )
        if self.verbose:
            print(f"> log -- roles: {roles}")

        debating_history = {}
        for role in roles:
            output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a {role}. Please answer the user's question as a {role}."
                        f"Rather than a general answer, please generate a special answer that only {role} can do.",
                    },
                    {
                        "role": "user",
                        "content": question,
                    },
                    {
                        "role": "assistant",
                        "content": f"{role}:",
                    },
                ],
            )

            response = output["choices"][0]["message"]["content"]
            response = response.replace(f"{role}:", "").strip()
            response = re.sub(r"\s+", " ", response)
            debating_history[role] = response

            if self.verbose:
                print(f"> log -- {role}: {response}")

        debating_history = "\n".join(
            [f"{role}: {answer}" for role, answer in debating_history.items()]
        )
        final_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Reference contents:\n{debating_history}",
                },
                {
                    "role": "user",
                    "content": question,
                },
                {
                    "role": "assistant",
                    "content": f"Responder model: ({self.prompts['final_response_hint']})",
                },
            ],
        )
        chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        social_lm_output = final_response["choices"][0]["message"]["content"]
        normal_chatgpt_output = chatgpt_response["choices"][0]["message"]["content"]
        return social_lm_output, normal_chatgpt_output
