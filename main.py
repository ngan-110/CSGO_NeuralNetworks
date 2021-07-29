import get_tensors
import prepare_data
import Model
import train
import evaluation
from numpy import sqrt
import predict
import plotfiles
import plotsamples
from pathlib import Path

def main():
    networkdatafile = r'july16_networkdata_clean.csv'
    replaydatafile = r'july16_test.csv'
    x,y,time,max_value = get_tensors.get_tensors(replaydatafile, networkdatafile) 
    print(x.size())
    print(y.size())
    print(len(time))
    print(max_value)


    trainx, valx, trainy, valy = prepare_data.prepare_data(x, y)
    print(trainx.size())
    print(trainy.size())
    print(valx.size())
    print(valy.size())

    model = Model.Model(max_value)
    train.train(model, trainx, trainy)

    mse = evaluation.evaluation(model, valx, valy)
    print('MSE: %.3f, RMSE: %.3f' % (mse, sqrt(mse)))

    data_folder = Path("../CSGOreplaysfiles/")
    realfile = data_folder / "real_july16_test.csv"
    predictfile = data_folder /  "predict_july16_test.csv"
    results = predict.predict(x,y,time,model,realfile,predictfile )

    plotfiles.plotfiles(realfile, "Real")
    plotfiles.plotfiles(predictfile, "Predicted")

    plotsamples.plotsamples(data_folder/'sample_july16_real_test.csv', data_folder/'sample_july16_predict_test.csv', "Time:12:40:03-05")  


if __name__ == "__main__":
    main()