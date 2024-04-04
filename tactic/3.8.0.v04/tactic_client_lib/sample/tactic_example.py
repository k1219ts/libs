# -*- coding: utf-8 -*-

from tactic_client_lib import TacticServerStub

server = TacticServerStub(login="test.creator", password="eprtmxj", server="10.0.0.51", project="mrgo")

####################
# SHOT
####################
shot_exp = "@SOBJECT(vfx/shot)" # 모든 샷 (모든 컬럼 포함)
#shot_exp = "@SOBJECT(vfx/shot['code', 'PBS_0040'])" # PBS_0040 샷만 보고 싶을 때
shotList = server.eval(shot_exp)
for shot in shotList:    
    code = shot['code'] # 추후 shot['name'] 으로 바뀔 예정
    tc_frame_start = shot['tc_frame_start'] # 핸들 적용한 프레임
    tc_frame_end = shot['tc_frame_end']
    frame_in = shot['frame_in'] # 101 프레임
    frame_out = shot['frame_out']
    print code, tc_frame_start, tc_frame_end, frame_in, frame_out

#===============================================================================
#         Column        |            Type             |                     Modifiers                     
# ----------------------+-----------------------------+---------------------------------------------------
# status               | text                        | 
# tc_frame_end         | integer                     | 
# code                 | character varying(256)      | not null
# type                 | character varying(256)      | 
# description          | text                        | 
# frame_out            | integer                     | 
# short_code           | character varying(256)      | 
# s_status             | character varying(256)      | 
# scan_status          | character varying(256)      | 
# frame_note           | text                        | 
# tc_frame_start       | integer                     | 
# priority             | character varying(256)      | 
# complexity           | integer                     | 
# pipeline_code        | character varying(256)      | 
# sequence_code        | character varying(256)      | 
# timestamp            | timestamp without time zone | default now()
# images               | text                        | 
# frame_in             | integer                     | 
# sort_order           | integer                     | 
# id                   | integer                     | not null default nextval('shot_id_seq'::regclass)
# parent_code          | character varying(256)      | 
# duration             | integer                     | 
# keywords             | text                        | 
# scene                | character varying(256)      | 
# cut                  | character varying(256)      | 
# take                 | character varying(256)      | 
# original_filename_l  | character varying(256)      | 
# original_filename_r  | character varying(256)      | 
# tc_in                | character varying(256)      | 
# tc_out               | character varying(256)      | 
# handle_count         | integer                     | 
# stereo               | character varying(256)      | 
# fps                  | double precision            | 
# vfx_check            | text                        | 
# brnote_interaction   | character varying(256)      | 
# brnote_animation     | character varying(256)      | 
# brnote_matchmove     | character varying(256)      | 
# brnote_modeling      | character varying(256)      | 
# brnote_lighting      | character varying(256)      | 
# brnote_fx            | character varying(256)      | 
# brnote_2d_roto       | character varying(256)      | 
# brnote_2d_remove     | character varying(256)      | 
# cam_slate            | character varying(256)      | 
# cam_grip_info        | character varying(256)      | 
# cam_slate_lens_set   | character varying(256)      | 
# cam_lens             | character varying(256)      | 
# cam_stereo_rig       | character varying(256)      | 
# cam_focus            | character varying(256)      | 
# cam_tstop            | character varying(256)      | 
# cam_filter           | character varying(256)      | 
# cam_inter_occular    | character varying(256)      | 
# editor_note          | character varying(256)      | 
# brnote_direction_vsp | character varying(256)      | 
# brnote_rotomation    | character varying(256)      | 
# brnote_rigging       | character varying(256)      | 
# brnote_creature      | character varying(256)      | 
# brnote_cloth         | character varying(256)      | 
# brnote_model         | character varying(256)      | 
# brnote_texture       | character varying(256)      | 
# brnote_mattepaint    | character varying(256)      | 
# brnote_comp          | character varying(256)      | 
# brnote_fur           | text                        | 
# brnote_finalize      | text                        | 
#===============================================================================


####################
# HDRI
####################
hdri_exp = "@SOBJECT(vfx/hdri)"
hdriList = server.eval(hdri_exp)
for hdri in hdriList:
    name = hdri['name']
    original_cut_number = hdri['original_cut_number']
    original_path = hdri['original_path']
    assemble_path = hdri['assemble_path']
    final_path = hdri['final_path']
    print name, original_cut_number, original_path, assemble_path, final_path

#===============================================================================
#       Column        |            Type             |                     Modifiers                     
# ---------------------+-----------------------------+---------------------------------------------------
# code                | character varying(256)      | 
# description         | text                        | 
# timestamp           | timestamp without time zone | default now()
# s_status            | character varying(256)      | 
# keywords            | text                        | 
# login               | character varying(256)      | 
# id                  | integer                     | not null default nextval('hdri_id_seq'::regclass)
# name                | character varying(256)      | 
# asset_code          | character varying(256)      | 
# original_cut_number | character varying(256)      | 
# original_path       | character varying(256)      | 
# assemble_path       | character varying(256)      | 
# final_path          | character varying(256)      | 
#===============================================================================
