ACKNOWLEDGEMENT:

  This work was supported in part by NSF grantCNS1758017.

  Adviser of my project is Dr. Markus Eger at Cal Poly Pomona: https://yawgmoth.github.io/

  I used Demo Analyzer, developed by Aaron Parker to parse CSGO demo [1]



PROCEDURE

  In short, our approach consists of three parts: 
  
  1) Collect replay files and extract locations of players;
   
  2) Record network traffic received from Valve server and; 
   
  3) Find a correlation between the two using a neural network.

The procedure involves the use of Pytorch, a Demo Analyzer parser, Artificial Neural Network, and network sniffing library: Wireshark.

The following steps can be use as guidance to replicate our experiment. The files needed for the program can be found at: github.com/ginnygreen110/CSGO\_NeuralNetworks

Please extract CSGOreplaysfiles.7z and DemoAnalyzer-good.7z before get started.

Notice: If you decide to use our provided data set, skip step 1-6. If you want to produce from scratch your own dataset, follow all of the steps.

1. To start collecting demos, we need to enable CSGO competitive ranked mode to get downloadable replays from CSGO.

2. Wireshark needs to be running and capturing network data from Valve server the entire duration of game play. However, we specifically only want the network data realeted from CSGO. To achieve this, we need to filter network data our local machine receives from Valve server, use NetRange: 162.254.192.0-162.254.199.255 [2]

3. After filtering, these network data should be saved as .json files into CSGOreplaysfiles folder. 

4. Use Jupyter notebook file jsontocsv.ipynb, insert .json file in normalize("file_filtered.json") to flatten and retrieve network bytes, lengths and timestamps from .json to .csv. desired file is auto-saved into CSGOreplaysfiles.

5. After having downloadable replay files from CSGO, run file DemoAnalyzer.exe in DemoAnalyzer-good\DemoAnalyzer\bin\Debug to extract data from desired replays files' players' x, y coordinates and their corresponding game time; These data are auto-saved as .csv files into folder CSGOreplaysfiles as well.

6. Before running main.py, input the .csv files of network data and players' positions extracted from Demo Analyzer: networkdatafile="_networkdata_clean.csv"; replaydatafile="_playersposition_file.csv". What we want to accomplish is to correctly predict players' positions when having a sample of network bytes. We have written a .py script to achieve this goal.

7. From your command line, navigate to directory where you save the repository, then run python main.py to run the script. When running main.py the following procedures are conducted:

  - Conversion of network bytes to numeric values.

  - Using the timestamps to align network bytes with the corresponding players' locations. Eg: Players' positions data at time t should be connected to network byte data at time m that is the smaller and is the closest value to t.

  - Data is normalized and randomly splitted into two sets: 80\% as training set to Neural Network model and 20\% is used as testing set.

  - The algorithm we are using includes of 4 hidden layers and Artificial Neural Network method with back-propagation, where MSE losses (errors) are sent back to fine-tune the weights of the net based on loss from previous iteration to lower error rates and increase its generalization, activation functions used is Leaky ReLU.

  - Three samples are randomly selected to show the real and their corresponding predictions.


REFERENCES

  [1]  Aaron Parker. Demo analyzer. https://github.com/AronParker/DemoAnalyzer,2021.
  
  [2]  162.254.193.0/24  as32590  valve  corporation  united  states  valve.net  reg-istry: Arin 256 ip addresses id: Valve-v4-6
