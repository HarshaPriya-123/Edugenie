from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import generate_content

router = APIRouter()


class SummarizeRequest(BaseModel):
    text: str
    length: str = "medium"  # short, medium, detailed


@router.post("/text")
def summarize_text(request: SummarizeRequest):
    length_instruction = {
        "short": "in 2-3 sentences",
        "medium": "in one concise paragraph (5-6 sentences)",
        "detailed": "in a detailed summary with key points as bullet points"
    }.get(request.length, "in one concise paragraph")

    prompt = f"""
You are EduGenie, an educational assistant that helps students study efficiently.
Summarize the following educational text {length_instruction}.
Focus on the key concepts a student needs to remember for exams.

Text to summarize:
\"\"\"
{request.text}
\"\"\"

Return only the summary, no extra commentary.
"""
    result = generate_content(prompt)
    return {"original_length": len(request.text), "summary": result}