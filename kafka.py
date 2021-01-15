import glob, os
from flask import Flask
from flask import request
import pyTigerDriver as tg


############# CONF TigerGraph Box #############
TG_Host = "127.0.0.1"
TG_User = "tigergraph"
TG_Pass = "tigergraph"
TG_Vers = "3.0.5"
################################################

############## KAFKA Related ###################
progress_files_path = "/home/tigergraph..../"
pregress_files_exte = "*.progress"
#################################################


# Flask Endpoint 5000 <-> 9000 => nginx conf 
app = Flask(__name__)
# tgCl : TigerGraph GSQL Client
tgCl = tg.Client(server_ip=TG_Host,username=TG_User,password=TG_Pass,version=TG_Vers)


def file_lister():
    files_list = []
    os.chdir(pregress_files_exte)
    for file in glob.glob(pregress_files_exte):
        # remove - suppress not used files 
        #
        #

        files_list.append(file)
    return files_list


def Files_Progress_Getter(graph_list):        
    content_files = {}
    for element in graph_list:
        # read file 
        #
        # get json
        #
        # Append result 
        content_files["s"] = ''
    return content_files

def GSQL_Progress_Getter(graph_list):
    progress = {}
    for graph in graph_list:
        tgCl.Gsql.query("USE {}".format(graph))
        res = tgCl.Gsql.query("SHOW STAUS PROGRESS KAFKA")
        progress[graph] = res
    return progress

@app.route('/kafka/', methods = ['GET', 'POST', 'DELETE'])
def kafka():
    if request.method == 'GET':
        gsql_result = {}

        #files = file_lister()

        #gsql_result = GSQL_Progress_Getter(files)
        return {"HI":gsql_result}
    if request.method == 'POST':
        data = request.form 
        return data
    if request.method == 'DELETE':
        return "DELETE"
    else:
        return "405"


app.run(debug=True)