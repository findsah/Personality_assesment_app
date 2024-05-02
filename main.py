from fastapi import FastAPI, HTTPException
from typing import List
from models import Transcript, Summary, Assessment, Evaluation
import json

app = FastAPI(title="Personality Assessment API")

@app.get("/transcripts/", response_model=List[Transcript])
def get_transcripts():
    try:
        with open('Data/sample_transcript.json', 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in transcripts endpoint: {e}")

@app.get("/summaries/", response_model=List[Summary])
def get_summaries():
    try:
        with open('Data/sample_summary_evaluation.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in summaries endpoint: {e}")


@app.get("/assessments/", response_model=List[Assessment])
def get_assessments():
    try:
        with open('Data/sample_assessment_part.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Assessment file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="Error decoding JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in assessments endpoint: {e}")

@app.get("/evaluations/", response_model=List[Evaluation])
def get_evaluations():
    try:
        with open('Data/sample_assessment_part_evaluation.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in evaluations endpoint: {e}")
