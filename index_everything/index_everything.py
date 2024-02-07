import glob
import math

import os
import copy

import pandas as pd
import json
######
### using tree
tree_base_command = "tree -a -f -L 10000 -N -Q -s -D --dirsfirst -J"
# example
# tree -a -f -L 10000 -N -Q -s -D --dirsfirst -J /home/giggi/motorsport/ > /home/giggi/motorsport/motorsport_index.json
### spawning new termional windows
# gnome-terminal -- command
gnome_spawn_prefix = "gnome-terminal -- "
######
### paths
project_home = "/home/giggi/motorsport/index_everything/"
index_output_home = project_home + "index_outputs/"
child_scripts_home = project_home + "child_scripts/"

index_all_sh_filename = "index_all_drives.sh"
### drives and virtual drives
drives = [
['Data_4TB','/media/giggi/Data_4TB/'],
['Data_2TB','/media/giggi/Data_2TB/'],
['virtual_internal_drive_backup','/media/giggi/447d3972-5682-4c56-8b88-c3944525facb/']]

drives = pd.DataFrame(drives)
drives.columns = ["name","mounted_path"]

#################################################
#################################################
def setup_tree_commands():
    tree_commands = copy.deepcopy(drives)
    tree_commands["output_filename"] = tree_commands["name"] + "_index.json"
    tree_commands["output_filepath"] = index_output_home + tree_commands["output_filename"]
    tree_commands["command"] = tree_base_command + " " + tree_commands["mounted_path"] + " > " + tree_commands["output_filepath"]
    tree_commands["local_sh_filepath"] = child_scripts_home + tree_commands["name"] + ".sh"

    tree_commands["multi_command"] = gnome_spawn_prefix + "sh " + tree_commands["local_sh_filepath"]

    return tree_commands
def create_index_all_drives_sh(tree_commands):
    # create the sub scripts
    for index, row in tree_commands.iterrows():
        with open(row["local_sh_filepath"], "w") as f:
            f.write(row["command"])

    # create index all drives sh script
    index_all_drives = tree_commands["multi_command"].values.tolist()
    index_all_drives = "\n".join(index_all_drives)
    with open(project_home+index_all_sh_filename,'w') as f:
        f.write(index_all_drives)
    
    return
#################################################
#################################################
## injest the index outputs
#indexes = glob.glob(index_output_home+"/*")


#################################################
#################################################
#################################################
#tree_commands = setup_tree_commands()
#create_index_all_drives_sh(tree_commands)

print("tru")