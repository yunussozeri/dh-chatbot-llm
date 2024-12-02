from llama_index.core.program import LLMTextCompletionProgram
from llama_index.core.bridge.pydantic import BaseModel, Field


class TableInfo(BaseModel):
    """Information regarding a structured table."""

    table_name: str = Field(
        ..., description="table name (must be underscores and NO spaces)"
    )
    table_summary: str = Field(
        ..., description="short, concise summary/caption of the table"
    )

def generate_summary(summery_llm):
    prompt_str = """\
    Give me a summary of the table with the following JSON format.

    - The table name must be unique to the table and describe it while being concise. 
    - Do NOT output a generic table name (e.g. table, my_table).

    Do NOT make the table name one of the following: {exclude_table_name_list}

    Table:
    {table_str}

    Summary: """

    program = LLMTextCompletionProgram.from_defaults(
        output_cls=TableInfo,
        llm=summery_llm,
        prompt_template_str=prompt_str,
    )