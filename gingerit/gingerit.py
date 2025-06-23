import logging
import os

import requests

log = logging.getLogger(__name__)

URL = "https://ginger4.p.rapidapi.com/correction"
GINGER_IT_API_KEY = os.getenv("GINGER_IT_API_KEY")


class GingerIt:
    def __init__(self):
        self.url = URL
        self.api_key = GINGER_IT_API_KEY
        self.lang = "US"

    def parse(self, text):
        session = requests.session()
        request = session.post(
            URL,
            data=text,
            headers={
                "content-type": "text/plain",
                "Content-Type": "text/plain",
                "Accept-Encoding": "identity",
                "X-RapidAPI-Key": GINGER_IT_API_KEY,
                "X-RapidAPI-Host": "ginger4.p.rapidapi.com",
            },
            params={
                "lang": "US",
                "generateRecommendations": "false",
                "flagInfomralLanguage": "true",
            },
            verify=True,
        )
        data = request.json()
        return self._process_data(text, data)

    @staticmethod
    def _change_char(original_text, from_position, to_position, change_with):
        return f"{original_text[:from_position]}{change_with}{original_text[to_position + 1 :]}"

    def _process_data(self, text, data):
        result = text
        corrections = []

        log.error(data)

        for suggestion in reversed(data["GingerTheDocumentResult"]["Corrections"]):
            start = suggestion["From"]
            end = suggestion["To"]

            if suggestion["Suggestions"]:
                suggest = suggestion["Suggestions"][0]
                result = self._change_char(result, start, end, suggest["Text"])

                corrections.append(
                    {
                        "start": start,
                        "text": text[start : end + 1],
                        "correct": suggest.get("Text", None),
                        "definition": suggest.get("Definition", None),
                    }
                )

        return {"text": text, "result": result, "corrections": corrections}
