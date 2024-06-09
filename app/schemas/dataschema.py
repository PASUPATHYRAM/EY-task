from pydantic import BaseModel,Field
from pydantic_computed import Computed,computed
from typing import List,Optional
from datetime import datetime

#request model
class PayloadRequest(BaseModel):
    batchid: str
    data: List[List[int]]

class PayloadResponse(PayloadRequest):
    data_compute: Optional[List[int]]

    def __init__(self, **data):
        super().__init__(**data)
        self.data_compute = [sum(d) for d in self.data]
#response model

class PayloadResponses(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime





