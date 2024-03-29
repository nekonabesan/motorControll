from typing import Optional

from pydantic import BaseModel, Field

class GetBase(BaseModel):
    pwm_value: int = Field(None, example=10, ge=-100, le=100)

class Get(GetBase):
    done: bool = Field(True, description="完了フラグ")