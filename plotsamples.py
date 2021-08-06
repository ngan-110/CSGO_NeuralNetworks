
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


def connectpoints(real,predict,sample, playerx, playery):
        x1, x2 = real[sample][playerx], predict[sample][playerx]
        y1, y2 = real[sample][playery], predict[sample][playery]
        plt.plot([x1,x2],[y1,y2],'k-', ls = '--', alpha = 0.4)

def plotsamples(filereal, filepredict, Time):
    df = pd.read_csv(filereal)
    dff = pd.read_csv(filepredict)
    # Read column that has timestamps from replays
    plt.figure(figsize=(4,3))
    plt.tick_params(labelsize=14)
    df = df.drop(['Time'],axis=1)
    dff = dff.drop(['Time'],axis=1)
    mpl.style.use('seaborn')

    plt.xlim(-.6, .4)
    plt.ylim(-.7, 0.3)

    time = Time.replace(":", "_")
    
    Title = "Real vs predicted positions:\n %s \n  Players 1-5" %Time
    plt.title(Title, fontsize = 18) 
    plt.plot(df.Player1_x,df.Player1_y, '#00FFFF', marker = '.', markersize = 10, label = "Player1" )
    plt.plot(df.Player2_x,df.Player2_y, '#9ACD32', marker = '.', markersize = 10, label = "Player2")
    plt.plot(df.Player3_x,df.Player3_y, '#A52A2A', marker = '.', markersize = 10, label = "Player3")
    plt.plot(df.Player4_x,df.Player4_y, '#D2B48C', marker = '.', markersize = 10, label = "Player4")
    plt.plot(df.Player5_x,df.Player5_y, '#FF7F50', marker = '.', markersize = 10, label = "Player5")
    
    
    plt.plot(dff.Player1_x,dff.Player1_y, '#13EAC9', marker = '*', markersize = 10, label = "Player1-Predict" )
    plt.plot(dff.Player2_x,dff.Player2_y, '#BBF90F', marker = '*', markersize = 10, label = "Player2-Predict")
    plt.plot(dff.Player3_x,dff.Player3_y, '#653700', marker = '*', markersize = 10, label = "Player3-Predict")
    plt.plot(dff.Player4_x,dff.Player4_y, '#D1B26F', marker = '*', markersize = 10, label = "Player4-Predict")
    plt.plot(dff.Player5_x,dff.Player5_y, '#FC5A50', marker = '*', markersize = 10, label = "Player5-Predict")

    df = pd.DataFrame(df)
    df = df.values 
    dff = pd.DataFrame(dff)
    dff = dff.values            

    for sample in range (0,3,1):
        for playerx in range (0, 9, 2):
            playery = playerx+1
            connectpoints(df,dff,sample,playerx,playery)
    
    plt.legend(bbox_to_anchor=(1, 1),fontsize = 13, loc='upper left', borderaxespad=0.)
    
    namefig = "%s Real vs predicted positions Players 1-5.png" %time
    plt.savefig(namefig, bbox_inches='tight') 
    plt.show()

    df = pd.read_csv(filereal)
    dff = pd.read_csv(filepredict)
    # Read column that has timestamps from replays
    plt.figure(figsize=(4,3))
    plt.tick_params(labelsize=14)
    df = df.drop(['Time'],axis=1)
    dff = dff.drop(['Time'],axis=1)
    mpl.style.use('seaborn')

    plt.xlim(-.6, .4)
    plt.ylim(-.7, 0.3)
    
    Title = "Players 6-10"
    plt.title(Title, fontsize = 18) 
    plt.plot(df.Player6_x,df.Player6_y, '#DC143C', marker = '.', markersize = 10, label = "Player6")
    plt.plot(df.Player7_x,df.Player7_y, '#FF00FF', marker = '.', markersize = 10, label = "Player7")
    plt.plot(df.Player8_x,df.Player8_y, '#FFD700', marker = '.', markersize = 10, label = "Player8")  
    plt.plot(df.Player9_x,df.Player9_y, '#FFC0CB', marker = '.', markersize = 10, label = "Player9")    
    plt.plot(df.Player10_x,df.Player10_y, '#008080', marker = '.', markersize = 10, label = "Player10")

    plt.plot(dff.Player6_x,dff.Player6_y, '#8C000F', marker = '*', markersize = 10, label = "Player6-Predict")
    plt.plot(dff.Player7_x,dff.Player7_y, '#ED0DD9', marker = '*', markersize = 10, label = "Player7-Predict")
    plt.plot(dff.Player8_x,dff.Player8_y, '#DBB40C', marker = '*', markersize = 10, label = "Player8-Predict") 
    plt.plot(dff.Player9_x,dff.Player9_y, '#FF81C0', marker = '*', markersize = 10, label = "Player9-Predict")  
    plt.plot(dff.Player10_x,dff.Player10_y, '#029386', marker = '*', markersize = 10, label = "Player10-Predict")
        
    df = pd.DataFrame(df)
    df = df.values 
    dff = pd.DataFrame(dff)
    dff = dff.values 

    for sample in range (0,3,1):
        for playerx in range (10, 19, 2):
            playery = playerx+1
            connectpoints(df,dff,sample,playerx,playery)
    
    plt.legend(bbox_to_anchor=(1, 1),fontsize = 13, loc='upper left', borderaxespad=0.)
    
    namefig = "%s Real vs predicted positions Players 6-10.png" %time
    plt.savefig(namefig,bbox_inches='tight') 
    plt.show()

 