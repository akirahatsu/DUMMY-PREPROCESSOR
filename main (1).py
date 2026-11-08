
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from groq import Groq

app = FastAPI()

class AIRequest(BaseModel):
    statistics: str = Field(max_length=10000)

@app.get("/")
def home():
    return {"status": "Cleanflow AI is running"}

@app.post("/ai-check")
def ai_check(data: AIRequest):

    api_key = os.getenv("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")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="Groq API key is not configured."
        )

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Dataset statistics:
                    {raw_train.describe()}

                    Identify suspicious values.
                    Answer in one short sentence,
                    maximum 30 words.
                    """
                }
            ],
            max_completion_tokens=150,
            reasoning_effort="low",
            temperature=0.1
        )

        return {
            "result": response.choices[0].message.content
        }

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI service is temporarily unavailable."
        )
