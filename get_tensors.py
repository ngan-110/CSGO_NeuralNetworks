import torch
import datetime
import csv
import pandas as pd
from pathlib import Path



def player_position(positionfile):
    feature_set = pd.read_csv(positionfile) 
    df = pd.DataFrame(feature_set)
    # Remove ticks, time and player names, columns
    df.drop(df.columns[[0,1,2,3,6,9,12,15,18,21,24,27,30]], axis = 1, inplace = True)
    df = df.values
    final_player_pos = []
    for line in df:
        player_row = []
        for i in range (0,20,1): 
            if str(line[i]) == 'nan':
                line[i] = float(0.0);  
            player_row.append(line[i])      
        final_player_pos.append(player_row)
    return final_player_pos

def player_time(positionfile): 
    with open(positionfile, 'r') as read_obj:
        player_timestamps = []
        csv_reader = pd.read_csv(read_obj, header = None)
        df = pd.DataFrame(csv_reader)
        # Read column that has timestamps from replays
        player_timestamps = df.iloc[:, 2]
    return player_timestamps

def network_bytes_data(networkfile): 
    with open(networkfile, 'r') as read_obj:
        byte_data = []
        csv_reader = pd.read_csv(read_obj, header = None)
        df = pd.DataFrame(csv_reader)
        # Read column that has byte data
        byte_data = df.iloc[:, 1]
        final_byte_data = []
        for line in byte_data:
            if str(line) == 'nan':
                line = '00';       
            final_byte_data.append(line)

        df = pd.read_csv(networkfile, low_memory=False)
        max_value = df.iloc[:, 2].max()
        max_value = int(max_value)
    return final_byte_data, max_value

def network_bytes_time(networkfile): #'networkdataclean.csv'
    with open(networkfile, 'r') as read_obj:
        timestamps = []
        csv_reader = pd.read_csv(read_obj, header = None)
        df = pd.DataFrame(csv_reader)
        # Read column that has time data
        timestamps = df.iloc[:, 0]
    return timestamps


# Function to get tensors
def get_tensors(positionfile, networkfile):
    Validation_file = "NEWFILE_%s" %positionfile
    data_folder = Path("../CSGOreplaysfiles/")
    positionfile = data_folder / positionfile
    networkfile = data_folder / networkfile
    
    # Get network bytes data
    data, max_value = network_bytes_data(networkfile)
    # Array of final bytes data
    final_byte_data = []
    for byte_string in data:
        # Array of bytes from a row
        byte_row = []
        byte_string = str(byte_string)
        
        # Convert byte data from hex to numeric values
        for i in range(0, len(byte_string),3):  
            pair = byte_string[i:i+2]
            bit = int(pair, 16)
            bit = float(bit)
            bit /= 240.0
            byte_row.append(bit) 
        # Fill in empty slots  
        if len(byte_row) < max_value:
                for j in range(max_value - len(byte_row)):
                    byte_row.append(float(0.0))   
        # Add byte data after conversion to final bytes data array 
        final_byte_data.append(byte_row)
    
    # Get timestamps from game replays after parsing
    player_pos_time = player_time(positionfile)
    # Get player position from game replays after parsing
    player_pos = player_position(positionfile)
    # Get timestamps from network data file
    timestamps = network_bytes_time(networkfile)

    # Array to store bytes as tensor
    tensorbyte = []
    # Array to store players' positions as tensors
    tensorposition = []
    # Array to store timestamp as verification
    time =[]
    time_player = []
    # Array to store timestamps from replays file after parsing
    player_time_array = []
    # Array to store timestamps from network data
    network_time_array = [] 

    # Read timestamps from game replays after parsing file to array
    for positions in player_pos_time:   
        if positions[11:13].isnumeric():
            hr=int(positions[11:13])      
        if positions[14:16].isnumeric():
            mins = int(positions[14:16])
        if positions[17:19].isnumeric():    
            sec = int(positions[17:19])
        if positions[20:23].isnumeric():    
            mill = int(positions[20:23])
        
        datetime_player = datetime.time(hr, mins, sec, mill)
        datetime_player = datetime.datetime.combine(datetime.date(1, 1, 1), datetime_player)
        player_time_array.append(datetime_player)
    
    # Read timestamps from network data file to array   
    for timestamp in timestamps:
        hr = int(timestamp[13:15])
        mins = int(timestamp[16:18])
        sec = int(timestamp[19:21])
        mill = int(timestamp[22:25])
        datetime_key = datetime.time(hr, mins, sec, mill)
        datetime_key = datetime.datetime.combine(datetime.date(1, 1, 1),datetime_key)
        network_time_array.append(datetime_key)
    it = 0
    count = 0
    # If Wireshark started receiving info before match starts, skip these rows
    while network_time_array[count] < player_time_array[0]:
        count+=1
    # If network timestamp is bigger than player timsetamps,
    while count < len(network_time_array) and it < len(player_time_array):
        if network_time_array[count] >= player_time_array[it]:
            # Recall and use the previous network timestamp 
            tensorbyte.append(final_byte_data[count-1])
            tensorposition.append(player_pos[it])
            time.append(network_time_array[count-1])
            time_player.append(player_time_array[it])
            # Move to next index
            it += 1
            while network_time_array[count] >= player_time_array[it] :
                it+=1
        count+=1
        

    # Create tensors from network byte data
    x = torch.FloatTensor(tensorbyte)
    # Create tensors from players' position data
    y = torch.FloatTensor(tensorposition)
    # Normalize these values for NN model
    y = torch.nn.functional.normalize(y)
    
    
    # Write network bytes, players' positions and timestamps to a file for verification
    with open(data_folder/Validation_file, "w") as csvfile:
        writer = csv.writer(csvfile)
        for value in range(len(tensorbyte)):
            writer.writerow([tensorbyte[value], y[value], tensorposition[value],time[value], time_player[value]])
    return x,y,time, max_value