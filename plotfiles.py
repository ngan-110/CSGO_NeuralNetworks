import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def plotfiles(file, type):
    df = pd.read_csv(file)
    df = pd.read_csv(file, skiprows=[1])
    plt.figure(figsize=(4,3))
    plt.tick_params(labelsize=14)
    mpl.style.use('seaborn')
    plt.xlim(-.4, .4)
    plt.ylim(-.2, 0.5)    
    Titlename = "%s positions" %type
    plt.title(Titlename, fontsize = 20)
    plt.plot(df.Player1_x,df.Player1_y, '.',  markersize = 10, label = "Player1" )
    plt.plot(df.Player2_x,df.Player2_y, '.', markersize = 10,label = "Player2")
    plt.plot(df.Player3_x,df.Player3_y, '.', markersize = 10,label = "Player3")
    plt.plot(df.Player4_x,df.Player4_y, '.', markersize = 10,label = "Player4")
    plt.plot(df.Player5_x,df.Player5_y, '.', markersize = 10,label = "Player5")
    plt.plot(df.Player6_x,df.Player6_y, '.', markersize = 10,label = "Player6")
    plt.plot(df.Player7_x,df.Player7_y, '.', markersize = 10,label = "Player7")
    plt.plot(df.Player8_x,df.Player8_y, '.', markersize = 10,label = "Player8")
    plt.plot(df.Player9_x,df.Player9_y, '.', markersize = 10,label = "Player9")
    plt.plot(df.Player10_x,df.Player10_y, '.', markersize = 10,label = "Player10")
    plt.legend(bbox_to_anchor=(1, 1), fontsize = 13, loc='upper left', borderaxespad=0.)
    
    namefig = "%s.png" %Titlename
    plt.savefig(namefig, bbox_inches='tight')  
    plt.show()