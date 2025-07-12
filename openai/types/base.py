from pydantic import BaseModel

class BaseModelV2(BaseModel):
    def model_dump(self, **kwargs):
        return self.dict(**kwargs)

    def model_dump_json(self, **kwargs):
        return self.json(**kwargs)
