import csv
import pandas as pd
import numpy

def predict(x, y, time, model, filereal, filepredict, data_folder):
    filereal = data_folder / filereal
    filepredict = data_folder / filepredict
    rows = x.clone().detach().requires_grad_(True)
    yhat = model(rows)
    y = y.detach().numpy()
    yhat = yhat.detach().numpy()
    idx = 20
    field_names = ['Player1_x','Player1_y','Player2_x','Player2_y','Player3_x','Player3_y',
                    'Player4_x','Player4_y','Player5_x','Player5_y','Player6_x','Player6_y',
                    'Player7_x','Player7_y', 'Player8_x','Player8_y', 'Player9_x','Player9_y','Player10_x','Player10_y', 'Time']
    with open(filereal, 'w', newline='') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(field_names)
        df = pd.DataFrame(y)
        df.insert(loc=idx, column='Time', value=time)
        df = numpy.array(df)
        mywriter = csv.writer(resultFile, delimiter=',')
        mywriter.writerows(df)
        
    with open(filepredict, 'w', newline='') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(field_names)
        df = pd.DataFrame(yhat)
        
        df.insert(loc=idx, column='Time', value=time)
        df = numpy.array(df)
        mywriter = csv.writer(resultFile, delimiter=',')
        mywriter.writerows(df)