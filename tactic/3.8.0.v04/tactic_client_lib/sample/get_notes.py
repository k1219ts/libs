# -*- coding: utf-8 -*-

import os
import sys
from tactic_client_lib import TacticServerStub

_login = "test.creator"
_server = "10.0.0.51"
_project = "mrgo"
_password = "eprtmxj"

server = TacticServerStub(login=_login, password=_password, server=_server, project=_project)


search_type = "vfx/shot"
try:
    shot = server.eval("@SOBJECT(vfx/shot['code', 'CAT_0010'])")[0] # CAT_0010 샷만
except:
    sys.exit()

code = shot.get("code") # return : CAT_0010
search_id = shot.get("id") # return : 297

search_key = server.build_search_key(search_type, code)  # return : vfx/shot?project=mrgo&code=CAT_0010
full_search_type = server.build_search_type(search_type) # return : vfx/shot?project=mrgo

# 선택된 샷의 모든 노트 가지고 오기
notes = server.eval("@SOBJECT(sthpw/note['search_type', '%s']['search_id', %d])" % (full_search_type, search_id))
for note in notes:
    _id = note.get('id')
    _project_code = note.get('project_code')
    _search_type = note.get('seearch_type')
    _search_id = note.get('search_id')
    _login = note.get('login')
    _context = note.get('context')
    _timestamp = note.get('timestamp')
    _note =  note.get('note')
    _process = note.get('process')
    _code = note.get('code')

    print _id, _project_code, _search_type, _search_id, _login, _context, _timestamp, _note, _process, _code


# CAT_0010 샷에 노트 추가하기
data = {
        'project_code' : 'mrgo',
        'search_type' : full_search_type, #
        'search_id' : search_id, #
        'login' : 'dongwan.kwon',
        'context' : 'creature',
        'process' : 'creature',
        'note' : '노트 내용'
        }

#server.insert( search_type, data ) # 기본적으로 트리거는 True
#server.insert( search_type, data, triggers=False ) # 트리거 사용하지 않을 경우

#################################################################################################
#
#  sthpw/note
#
#################################################################################################
#    Column    |            Type             |                     Modifiers                     
#--------------+-----------------------------+---------------------------------------------------
# id           | integer                     | not null default nextval('note_id_seq'::regclass)
# project_code | character varying(30)       | 
# search_type  | character varying(200)      | 
# search_id    | integer                     | 
# login        | character varying(30)       | 
# context      | character varying(60)       | 
# timestamp    | timestamp without time zone | default now()
# note         | text                        | 
# title        | character varying(1024)     | 
# parent_id    | bigint                      | 
# status       | character varying(256)      | 
# label        | character varying(256)      | 
# process      | character varying(60)       | 
# sort_order   | integer                     | 
# access       | character varying(256)      | 
# code         | character varying(256)      | 
#################################################################################################


# CAT_0010 에 등록된 프로세스 가지고 오기
processes = server.get_pipeline_processes(search_key) # return : ['matchmove', 'model', 'creature', 'animation', 'texture', 'lighting', 'mattepaint', 'fx', 'crowd', 'comp', 'rnd', 'edit', 'di', 'acquisition', 'test', 'objtracking', 'camtracking', 'finalize', 'facial', 'rigging', 'fur', 'cloth', 'rotomation', 'mocapclean', 'hdriedit', 'lookdev', 'roto', 'ocular', 'cleanup', 'projectionsetup', 'crowdcomp', 'libdev', 'scrdev', 'guidev', 'otldev', 'debug']

# Tactic 에 등록된 유저 가지고 오기
users = server.eval("@SOBJECT(sthpw/login)")     # 모든 칼럼  가지고 오기
#users = server.eval("@GET(sthpw/login.login)")  # 로그인 칼럼만 가지고 오기

for user in users:
    login = user.get('login')
    departmentment = user.get('department')
    email = user.get('email')
    print login, email


#################################################################################################
#
#  sthpw/login
#
#################################################################################################
#      Column      |            Type             |                     Modifiers                      
#------------------+-----------------------------+----------------------------------------------------
# id               | integer                     | not null default nextval('login_id_seq'::regclass)
# login            | character varying(100)      | not null
# password         | character varying(255)      | 
# login_groups     | text                        | 
# first_name       | character varying(100)      | 
# last_name        | character varying(100)      | 
# email            | character varying(200)      | 
# phone_number     | character varying(32)       | 
# department       | character varying(256)      | 
# namespace        | character varying(255)      | 
# snapshot         | text                        | 
# s_status         | character varying(30)       | 
# project_code     | text                        | 
# license_type     | character varying(256)      | 
# hourly_wage      | double precision            | 
# code             | character varying(512)      | 
# mobile_number    | character varying(256)      | 
# role             | text                        | 
# preview          | character varying(256)      | 
# department_short | character varying(256)      | 
# name_kr          | character varying(256)      | 
# job_level        | character varying(256)      | 
# job_title        | character varying(256)      | 
# department_kr    | character varying(256)      | 
# location         | text                        | 
# description      | character varying(256)      | 
# start_date       | timestamp without time zone | 
# emploee_number   | character varying(256)      | 
# birthday         | timestamp without time zone |
#################################################################################################
