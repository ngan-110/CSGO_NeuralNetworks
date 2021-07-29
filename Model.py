import torch.nn as nn
import torch.nn.functional as f


class Model(nn.Module):
    def __init__(self, max_value): 
        super(Model, self).__init__()
        first_layer = round(max_value*66/100)
        self.fc1 = nn.Linear(max_value,first_layer)
        second_layer = round(first_layer*66/100)
        self.fc2 = nn.Linear(first_layer, second_layer)
        third_layer = round(second_layer*66/100)
        self.fc3 = nn.Linear(second_layer, third_layer)
        self.fc4 = nn.Linear(third_layer, 20)

    def forward(self, x):
        x = f.leaky_relu(self.fc1(x))
        x = f.leaky_relu(self.fc2(x))
        x = f.leaky_relu(self.fc3(x))
        x = self.fc4(x)
        return x
