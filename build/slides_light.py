import sys; sys.path.insert(0,"build")
from common import *
F="AMB_Draft_4_remaster_wip.pptx"
prs=Presentation(F); P="photos/"; sl=prs.slides

# ---- S2: right-bleed portrait photo strip, text column narrowed
s=sl[1]
im=crop(P+"pg1-000.png",2.3/4.325,0.5,0.55)
pic=s.shapes.add_picture(save(im,"s2_pg1.jpg"),Inches(7.7),Inches(1.3),Inches(2.3),Inches(4.325))
ROWS=((5,6,7,8),(10,11,12,13),(15,16,17,18),(20,21,22,23))
for k,ids in enumerate(ROWS):
    for i in ids:
        sh=shp(s,i); sh.top=sh.top+Inches(0.07*k)
    for i in ids[2:]: geom(s,i,w=6.3)
    scale_font(shp(s,ids[3]),0.9)
for k,i in enumerate((9,14,19)):
    sh=shp(s,i); sh.top=sh.top+Inches(0.07*(k+1)); sh.width=Inches(6.3)
set_color(shp(s,24),"FFFFFF")
s.shapes._spTree.append(shp(s,24)._element)  # page number above photo

# ---- S3: the "issue" card becomes a photo card (navy ramp keeps text legible)
s=sl[2]
im=crop(P+"pg89-000.png",2.9/3.5,0.5,0.35)
im=gradient_lower(im,y0f=0.12,y1f=0.5,peak=0.94)
put_picture(s,15,save(im,"s3_pg89.jpg"),6.6,1.45,2.9,3.5)

# ---- S5: photo with a white stat card floating over it
s=sl[4]
im=crop(P+"pg34-000.png",3.8/3.4,0.5,0.55)
put_picture(s,6,save(im,"s5_pg34.jpg"),5.7,1.45,3.8,3.4)
card=rect(s,5.95,2.05,3.3,2.55,fill="FFFFFF",line=RULE)
to_back_of(s,card,7)
geom(s,7,x=6.15,w=2.9,y=2.15,h=0.6); scale_font(shp(s,7),0.8)
geom(s,8,x=6.15,w=2.9,y=2.78,h=0.7); scale_font(shp(s,8),0.88)
geom(s,9,x=6.15,w=2.9,y=3.55)
geom(s,10,x=6.15,w=2.9,y=3.65,h=0.95); scale_font(shp(s,10),0.9)

# ---- S8: photo header on the side card (icon dropped to make room)
s=sl[7]
im=crop(P+"pg18-000.png",3.3/0.85,0.5,0.3)
pic=s.shapes.add_picture(save(im,"s8_pg18.jpg"),Inches(6.2),Inches(1.4),Inches(3.3),Inches(0.85))
to_back_of(s,pic,8)
remove(s,8,9)
geom(s,10,x=6.4,y=2.38,w=2.95,h=0.3); scale_font(shp(s,10),0.95)
geom(s,11,y=2.75); scale_font(shp(s,11),0.92)
geom(s,12,y=4.36,h=0.5); scale_font(shp(s,12),0.9)

# ---- S9: photo flush-left inside the navy quote banner (icon dropped)
s=sl[8]
im=crop(P+"pg10-000.png",1.5/1.35,0.5,0.45,zoom=1.3)
pic=s.shapes.add_picture(save(im,"s9_pg10.jpg"),Inches(0.5),Inches(3.55),Inches(1.5),Inches(1.35))
to_back_of(s,pic,20)
remove(s,18,19)
geom(s,20,x=2.25,w=7.05)

# ---- S10: no colour blocks; accent rule + hairlines, note becomes a ruled line
s=sl[9]
for i,x in ((5,0.5),(13,3.55),(21,6.6)):
    nofill(shp(s,i)); shp(s,i).line.fill.background()
    r=rect(s,x,1.4,2.9,0.04,fill=LEAF); to_back_of(s,r,shp(s,i+1).shape_id)
nofill(shp(s,29)); shp(s,29).line.fill.background()
bar=rect(s,0.5,4.35,0.05,0.68,fill=LEAF); to_back_of(s,bar,30)
geom(s,30,x=0.75,w=8.5)

# ---- S12: grey bars become hairline rows; accent rule under the quarter header
s=sl[11]
for i,y in ((14,1.8),(21,2.6),(28,3.4),(35,4.2)):
    nofill(shp(s,i)); r=rect(s,0.5,y+0.6,9.0,0.01,fill=RULE); to_back_of(s,r,i)
rect(s,0.5,1.7,9.0,0.03,fill=LEAF)

# ---- S13: ROI panel bleeds off the right and bottom edges
s=sl[12]
geom(s,15,w=3.25,h=4.225)
shp(s,15)._element.spPr.find('{http://schemas.openxmlformats.org/drawingml/2006/main}prstGeom').set('prst','rect')
geom(s,19,w=5.9)
set_color(shp(s,20),"FFFFFF")
prs.save(F)
