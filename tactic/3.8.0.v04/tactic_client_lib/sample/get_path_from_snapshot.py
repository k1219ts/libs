# -*- coding: utf-8 -*-
'''
Created on Aug 16, 2012

@author: Seo Jungwook
'''

import os
import sys
from tactic_client_lib import TacticServerStub

_login = "test.creator"
_server = "10.0.0.51"
_project = "mrgo"
_password = "eprtmxj"

server = TacticServerStub(login=_login, password=_password, server=_server, project=_project)


#############
# Asset
#############
search_type = "vfx/asset"
#filters = [("name", "MCA001")]
filters = [("name", "like", "MCA%")]             # name 컬럼에서 MCA 로 시작하는 아이템을 찾는다.
context = "mocapclean/anim"

assets = server.query(search_type, filters)
if len(assets) == 0: # 검색된 결과가 0일 경우
    sys.exit()

for asset in assets:
    code = asset.get("code")
    search_key = server.build_search_key(search_type, code)
    snapshot = server.get_snapshot(search_key, context=context)
    if snapshot: # snapshot 이 존재할 경우
        snapshot_code = snapshot.get("code")
        
        # get_path_path_from_snapshot(snapshot_code, file_type='main', mode)
        # mode : 'lib', 'web', 'local_repo', 'sandbox', 'client_repo', 'relative'
        # 'lib' : 서버위치에서 바라보는 NFS 경로
        # 'web' : 클라이언트위치에서 바라보는 http asset 디렉토리
        # 'local_repo' : TACTIC 저장소의 로컬 싱크
        # 'sandbox' : TACTIC 에서 지정한 작업공간
        # 'client_repo; 클라이언트위치에서 바라보는 asset 디렉토리
        # 'relative' : 상대경로
        path = server.get_path_from_snapshot(snapshot_code, mode="client_repo")
        if os.path.isdir(path):
            print "Directory : " + path
            animList = os.listdir(path)
            for anim in animList:
                print os.path.join(path, anim)



print "Done."
