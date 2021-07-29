import csv
import pandas as pd
from pathlib import Path
import numpy


def get_randomsamples(data_folder, realfile,predictedfile,num_sample):
    sample_realfile = "sample_%s" %realfile
    sample_realfile = data_folder/sample_realfile
    sample_predictedfile = "sample_%s" %predictedfile
    sample_predictedfile = data_folder/ sample_predictedfile
    realfile = data_folder / realfile
    predictedfile = data_folder / predictedfile
    csv_reader_real = pd.read_csv(realfile, skiprows=[1] ,header = None)
    df_real = pd.DataFrame(csv_reader_real)
    csv_reader_predict = pd.read_csv(predictedfile, skiprows=[1] , header = None)
    df_predict = pd.DataFrame(csv_reader_predict)
    y = df_real.sample(num_sample)
    field_names = ['Player1_x','Player1_y','Player2_x','Player2_y','Player3_x','Player3_y',
                    'Player4_x','Player4_y','Player5_x','Player5_y','Player6_x','Player6_y',
                    'Player7_x','Player7_y', 'Player8_x','Player8_y', 'Player9_x','Player9_y','Player10_x','Player10_y', 'Time']
    
    with open(sample_realfile, 'w', newline='') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(field_names)
        df_real = numpy.array(y)
        mywriter = csv.writer(resultFile, delimiter=',')
        mywriter.writerows(df_real)
   
    with open(sample_predictedfile, 'w', newline='') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(field_names)
        sample_line = []
        time_label = []
        
        for i in range (0,3,1):
            value = y.iloc[i, 20]
            line =0
            while line < len(df_predict):
                if str(value) == str(df_predict.iloc[line, 20]):
                    sample_line.append(df_predict.iloc[line,:])
                    time_label.append(value)
                line+=1
        sample_line = pd.DataFrame(sample_line)
        sample_line = numpy.array(sample_line)
        mywriter = csv.writer(resultFile, delimiter=',')
        mywriter.writerows(sample_line)
        eachtime = ""
        for positions in time_label:   
            each = positions[11:19]
            eachtime += "_"+each   
        eachtime = eachtime[1:]
    return sample_realfile, sample_predictedfile,eachtime