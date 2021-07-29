import torch



def prepare_data(x, y):
    idx = torch.randperm(x.size()[0])
    split = int(x.size()[0] * 0.80)
    trainx = x[idx[     :split], :]
    valx =   x[idx[split:     ], :]
    trainy = y[idx[     :split], :]
    valy =   y[idx[split:     ], :]
    return trainx, valx, trainy, valy