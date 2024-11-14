from typing import Any, List, Union
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, FunctionMessage
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from agent import agent_executor
from langserve import add_routes

# app 생성
app = FastAPI()


class Input(BaseModel):
    input: str
    chat_history: List[Union[HumanMessage, AIMessage, FunctionMessage]] = Field(
        ...,
        extra={"widget": {"type": "chat", "input": "input", "output": "output"}},
    )


class Output(BaseModel):
    output: Any

add_routes(
    app,
    agent_executor.with_types(input_type=Input, output_type=Output).with_config(
        {"run_name": "agent"}
    ),
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)