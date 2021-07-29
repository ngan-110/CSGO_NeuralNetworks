from sklearn.metrics import mean_squared_error
from numpy import vstack

def evaluation(model, x, y):
    predictions, actuals = list(), list()
    print("Evaluating Model...")
    for i in enumerate(x):
        yhat = model(x)
        yhat = yhat.detach().numpy()
        actual = y.numpy() 
        predictions.append(yhat)
        actuals.append(actual)
    predictions, actuals = vstack(predictions), vstack(actuals)
    mse = mean_squared_error(actuals, predictions)
    return mse