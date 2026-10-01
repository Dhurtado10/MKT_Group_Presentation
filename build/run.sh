#!/bin/bash
cd /home/user/MKT_Group_Presentation
python3 build/slides_7_11.py && python3 build/slides_light.py && build/render.sh AMB_Draft_4_remaster_wip.pptx 110 >/dev/null
