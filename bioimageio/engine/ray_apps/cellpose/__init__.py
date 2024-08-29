from hypha_rpc import api

class CellposeModel:
    def __init__(self):
        # Load model
        pass

    def predict(self, image: str) -> str:
        prediction = "prediction of cellpose model on image: " + image
        return prediction

    def train(self, data: str, config: str) -> str:
        training = "training cellpose model on data: " + data + "with config:" + config
        return training


api.export(CellposeModel)
