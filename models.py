from pydantic import BaseModel
from typing import List

class Transcript(BaseModel):
  
    index: int
    speaker_label: str
    paragraph: str
    start_time: int
    end_time: int

class Summary(BaseModel):
   
    sentence: str
    is_inferable: bool
    explanation: str

class Assessment(BaseModel):
    question: str
    answer: str
    evidence: List[str]

class Evaluation(BaseModel):
 
    question: str
    answer: str
    inferability_score_1: int
    inferability_score_2: int

