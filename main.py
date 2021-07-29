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
import get_randomsamples


def main():
    networkdatafile = "july16_networkdata_clean.csv"
    replaydatafile = "july16_test.csv"
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
    realfile = "real_"+ replaydatafile
    predictfile = "predict_"+ replaydatafile
    results=predict.predict(x,y,time,model,realfile,predictfile,data_folder)

    plotfiles.plotfiles(data_folder,realfile, "Real")
    plotfiles.plotfiles(data_folder,predictfile, "Predicted")
    sample_realfile, sample_predictedfile,eachtime = get_randomsamples.get_randomsamples(data_folder, realfile,predictfile,3)
    print(eachtime)

    plotsamples.plotsamples(data_folder/sample_realfile,data_folder/sample_predictedfile, eachtime)  

if __name__ == "__main__":
    main()