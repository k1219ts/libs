import os
import time
from tactic_client_lib import TacticServerStub

_login = "test.creator"
_password = "eprtmxj"
_server = "10.1.0.144"
#_server = "10.0.0.51"
_project = "mrgo"

server = TacticServerStub(login=_login, password=_password, server=_server, project=_project)

task_dic = {}
my_tasks = server.eval("@SOBJECT(sthpw/task['project_code','%s']['assigned','kihong.oh']['status','In-Progress'])" % _project)

for t in my_tasks:
    search_type = t.get('search_type').split('?')[0]
    search_id = t.get('search_id')

    so = server.eval("@SOBJECT(%s['id',%s])" % (search_type, search_id), single=True) # asset , shot
    name = so.get("name")
    code = so.get("code")
    process = t.get("process")
    
    search_key = server.build_search_key(search_type, code) 
    
    task_dic[name] = [search_key, process]

for t in task_dic.keys():
    print t

mov_file = '/netapp/dexter/dept/PPS/tactic/spectator.mov'
if os.path.isfile(mov_file):
    name = 'spectator'
    search_key = task_dic[name][0]
    context = task_dic[name][1] + '/' + os.path.basename(mov_file)
    #print search_key, context, task_dic[name][1]
    
    # web mode
    server.simple_checkin( search_key, context, mov_file, description="Comment", mode="upload")

    # handoff mode
    #server.simple_checkin( search_key, context, mov_file, description="Comment", mode="copy")

print 'Done !!!'

time.sleep(5)

server.undo()
    
print 'Done !!!!!'