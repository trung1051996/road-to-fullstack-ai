from google import genai
from google.genai import types
from dotenv import load_dotenv
from typing import Type
from pydantic import BaseModel
import os
load_dotenv()

class GeminiClient:
    def __init__(
        self,
        model: str = 'gemini-3.6-flash',
        temperature: float = 0,
        top_p=0.95,
        top_k=20,
    ):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k

    def chat(self, prompt: str, response_schema: Type[BaseModel] | None = None):
        config_kwargs = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
        }
        if response_schema:
            config_kwargs["response_mime_type"] = "application/json"
            config_kwargs["response_schema"] = response_schema.model_json_schema()

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(**config_kwargs),
        )

        return response.parsed

    def embed(self, text: str):
        result = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )
        return result.embeddings[0].values


if __name__ == "__main__":
    service = GeminiClient()

    print(service.chat("Why is the sky blue?"))

