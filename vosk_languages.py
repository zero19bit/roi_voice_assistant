from vosk import Model
import json

models = json.load(open("models.json", "r"))

model_path_FA = models["model_path_FA"]
model_FA = Model(model_path_FA)

model_path_TR = models["model_path_TR"]
model_TR = Model(model_path_TR)

model_path_US = models["model_path_US"]
model_US = Model(model_path_US)

