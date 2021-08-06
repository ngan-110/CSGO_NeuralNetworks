import torch
import matplotlib.pyplot as plt


def train(m, x, y):
    print("\nTraining in progress...")
    opt = torch.optim.Adam(m.parameters(), lr=0.001)
    criterion = torch.nn.MSELoss()
    Loss_list = []

    for i in range(100):
        model_result  = m(x) #yhat
        opt.zero_grad()
        loss = criterion(model_result , y)
        loss.backward()
        opt.step()
        Loss_list.append(loss / (len(x)))
        
    print('Finished Training Trainset')
    x2 = range(0, 100)
    y2 = Loss_list
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('Loss vs. epoches')
    plt.ylabel('Loss')
    
    plt.savefig('Accuracy_loss.jpg')  

    plt.show()