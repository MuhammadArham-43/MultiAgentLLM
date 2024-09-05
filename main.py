import sys
import argparse
import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from agent import build_pipeline

class UserInput(BaseModel):
    topic: str
    
class QueryOutput(BaseModel):
    response: str


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config_path", type=str, default="configuration.yaml", help="Path to configuation yaml file")

args = parser.parse_args()

try:
    with open(args.config_path, "r") as _f:
        config = yaml.safe_load(_f)
except Exception as e:
    print(f"Can not load configuration file from: {args.config_path}")
    print(f"Error: {e}")
    sys.exit(1)

pipeline = build_pipeline(config)
app = FastAPI()

@app.post("/query/")
def query(inputs: UserInput) -> dict:
    try:
        result = pipeline.kickoff(inputs={"topic": inputs.topic})
        return {
            "response": result.raw
        }
    except Exception as e:
        print(f"Error Handling Request: {e}")
        raise HTTPException(status_code=500, detail="Error handling request. Server-side issue.")
    

if __name__ == "__main__":
    uvicorn.run(app, host=config["server"]["host"], port=config["server"]["port"])