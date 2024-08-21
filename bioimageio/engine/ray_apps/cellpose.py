from hypha_rpc import api

class CellposeModel:
    def __init__(self):
        # Load model
        pass

    def predict(self, image: str) -> str:
        pass
    
    def train(self, data: str, config: str) -> str:
        pass


api.export(CellposeModel, {"name": "cellpose", "type": "ray"})