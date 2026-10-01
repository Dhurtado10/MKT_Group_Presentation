import sys; sys.path.insert(0,"build")
from common import *
F="AMB_Draft_4_remaster_wip.pptx"
prs=Presentation(F); P="photos/"; sl=prs.slides
CW=PP_ALIGN.CENTER

def pagenum_white(s,pid):
    set_color(shp(s,pid),"FFFFFF"); s.shapes._spTree.append(shp(s,pid)._element)

# =============== S2: shortlist visual
s=sl[1]; clear(s,{3,4,24})
band=s.shapes.add_picture(pattern_crop(10,1.3,fade=0.72,cx=0.55,cy=0.5,name="s2_band.jpg"),0,0,Inches(10),Inches(1.3)); to_back(s,band)
# row A: the shortlist
small_caps(s,0.5,1.47,5,"What we found in all six groups")
for i in range(4):
    x=0.5+i*1.22
    rrect(s,x,1.75,1.1,0.78,fill=NAVY,r=0.18)
    text(s,x,1.75,1.1,0.78,[[("Lender","Calibri",10,"AFC0DA",False)],[("they knew","Calibri",10,"AFC0DA",False)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
text(s,0.5,2.58,4.8,0.25,[[("Two to four lenders compared. The list was built before any rate was seen.","Calibri",10,GREY,False)]])
# AMB slot (dashed, leaf mark)
rrect(s,5.55,1.75,1.55,0.78,fill="FFFFFF",line=LEAF,lw=1.5,r=0.18,dash=True)
s.shapes.add_picture(BR+"amb_leaves_transparent.png",Inches(5.62),Inches(1.8),Inches(0.95),Inches(0.55))
text(s,6.5,1.75,0.6,0.78,[[("AMB","Calibri",11,GREEN,True)],[("absent","Calibri",9.5,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE)
text(s,5.55,2.58,1.6,0.25,[[("Never among them","Calibri",10,GREEN,True)]])
# strengths vs presence
line(s,7.4,1.55,7.4,2.8,RULE,1)
text(s,7.6,1.5,1.9,0.5,[[("5.94%","Cambria",24,GREEN,True)]])
text(s,7.6,2.0,1.9,0.4,[[("variable rate, competitive with the big four","Calibri",9.5,GREY,False)]])
text(s,7.6,2.42,1.9,0.4,[[("Most trusted sector in banking","Calibri",9.5,NAVY,True)]])
# row B: three moves
small_caps(s,0.5,3.05,5,"Three moves place AMB where the shortlist is built")
mv=[("Easy to verify online",NAVY),("In the broker's working set","24607F"),("Check-your-offer link",LEAF)]
for i,(t,c) in enumerate(mv):
    x=0.5+i*3.0
    sh=rect(s,x,3.33,3.0,0.72,fill=c,shape=MSO_SHAPE.PENTAGON if i==0 else MSO_SHAPE.CHEVRON)
    text(s,x+(0.5 if i else 0.22),3.33,2.5,0.72,[[(t,"Calibri",12,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE)
# row C: budget bar
small_caps(s,0.5,4.28,3,"Budget and return")
text(s,4.5,4.28,5,0.22,[[("Return of XXX x lifetime margin per funded loan","Calibri",9.5,GREY,False)]],align=PP_ALIGN.RIGHT)
segs=[("20%","Verify",1.8,"24607F"),("55%","Broker channel",4.95,NAVY),("15%","Referral",1.35,LEAF),("10%","Test",0.9,"B8C2D6")]
x=0.5
for pct,lab,w,c in segs:
    rect(s,x,4.55,w-0.03,0.42,fill=c)
    text(s,x,4.55,w-0.03,0.42,[[(pct,"Cambria",14,"FFFFFF" if c!="B8C2D6" else NAVY,True)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
    text(s,x,5.0,w-0.03,0.2,[[(lab,"Calibri",9,GREY,False)]],align=CW)
    x+=w

# =============== S6: shape-built "journey" table
s=sl[5]; clear(s,{3,4,6,7})
rows=[("Direct to big four",6,'The household decides. "Alternatives" only ever meant another big-four bank.',"Never evaluated"),
("Broker-placed",8,"The market was the two to four lenders the broker presented. No one recalled AMB.","Absent from working set"),
("DIY online",9,"Search starts with friends and the bank's app. All seven who chose went to a big four.","Scrolled past"),
("Refinancers",9,"Ads and comparison sites trigger the search; brand recognition was the top factor.","Not recognised"),
("Upgraders",6,"Comparison sites build awareness, not trust. The old lender calls back with a better rate.","Outbid at the close"),
("First-home buyers",4,"Discovery ran through a broker or a parent. None had heard of AMB.","Never heard of")]
for x,w,t in ((0.5,2.2,"Borrower group"),(3.0,3.9,"What the research found"),(7.0,2.5,"Where AMB is lost")):
    small_caps(s,x,1.3,w,t,color=NAVY if t!="Where AMB is lost" else GREEN)
rect(s,0.5,1.56,9.0,0.03,fill=LEAF)
Y0=1.68; PITCH=0.54; H=0.47
for i,(g,n,f,lost) in enumerate(rows):
    y=Y0+i*PITCH
    rect(s,0.5,y,2.1,H,fill=NAVY,shape=MSO_SHAPE.PENTAGON)
    text(s,0.65,y,1.7,H,[[(g,"Calibri",11,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE)
    o=rect(s,2.3,y+0.02,H-0.04,H-0.04,fill="FFFFFF",line=NAVY,lw=1.5,shape=MSO_SHAPE.OVAL)
    text(s,2.3,y+0.02,H-0.04,H-0.04,[[(str(n),"Cambria",12,NAVY,True)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
    rrect(s,2.95,y,3.95,H,fill="F1F4F9",r=0.2)
    text(s,3.08,y,3.72,H,[[(f,"Calibri",9.5,NAVY,False)]],anchor=MSO_ANCHOR.MIDDLE)
    rect(s,7.0,y,2.5,H,fill=GREEN if i%2==0 else LEAF,shape=MSO_SHAPE.PENTAGON)
    text(s,7.15,y,2.0,H,[[(lost,"Calibri",11,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE)
    line(s,2.62,y+H/2,2.95,y+H/2,"8A94A6",1)

# =============== S8: two charts kept, side panel simplified
s=sl[7]; clear(s,{3,4,5,6,13,14})
for cid,(y,h) in ((5,(1.4,2.1)),(6,(3.7,1.28))):
    ch=geom(s,cid,x=0.55,y=y,w=5.4,h=h)
c1=rrect(s,0.5,1.35,5.5,2.2,fill="FFFFFF",line=RULE,r=0.04); to_back_of(s,c1,5)
c2=rrect(s,0.5,3.65,5.5,1.38,fill="FFFFFF",line=RULE,r=0.06); to_back_of(s,c2,6)
rect(s,0.5,1.35,0.05,2.2,fill=NAVY); rect(s,0.5,3.65,0.05,1.38,fill=LEAF)
# panel
PX=6.2; PW=3.3
s.shapes.add_picture(pattern_crop(PW,1.55,fade=0.35,cx=0.6,cy=0.4,zoom=1.2,name="s8_pat.jpg"),Inches(PX),Inches(1.35),Inches(PW),Inches(1.55))
rect(s,PX,2.9,PW,2.13,fill=NAVY)
for k,(big,cap) in enumerate((("10 of 10","moved by a friend's good experience with AMB"),("3 of 10","moved by a better rate alone"))):
    x=PX+0.15+k*1.6
    rect(s,x,1.5,1.5,1.25,fill="FFFFFF"); alpha(s.shapes[-1],82)
    text(s,x+0.1,1.55,1.3,0.55,[[(big,"Cambria",24,NAVY,True)]])
    text(s,x+0.1,2.12,1.3,0.6,[[(cap,"Calibri",9.5,NAVY,False)]])
small_caps(s,PX+0.2,3.0,PW-0.4,"What would make them comfortable",color="7FD6BC",size=9)
items=[("Real rate, fees, approval time up front","7/8"),("Someone like them had used it","6/8"),("Independent reviews or ratings","6/8"),("A quantified, easy-to-verify advantage","6/8")]
for i,(t,v) in enumerate(items):
    y=3.28+i*0.32
    text(s,PX+0.2,y,2.5,0.28,[[(t,"Calibri",10,"FFFFFF",False)]],anchor=MSO_ANCHOR.MIDDLE)
    text(s,PX+2.6,y,0.5,0.28,[[(v,"Calibri",10.5,"7FD6BC",True)]],anchor=MSO_ANCHOR.MIDDLE,align=PP_ALIGN.RIGHT)
    if i<3: line(s,PX+0.2,y+0.3,PX+PW-0.2,y+0.3,"34497A",0.75)
text(s,PX+0.2,4.58,PW-0.4,0.4,[[("Customer-owned label: appealed to the 3 who had never borrowed; moved 2 of the 7 who had.","Calibri",8.5,"AFC0DA",False)]])

# =============== S9: pictograms on pattern, navy quote ribbon
s=sl[8]; clear(s,{3,4,21,22})
bg=s.shapes.add_picture(pattern_crop(10,5.625,fade=0.78,cx=0.5,cy=0.5,name="s9_bg.jpg"),0,0,Inches(10),Inches(5.625)); to_back(s,bg)
cards=[("3 of 4",3,"would check AMB themselves after a broker recommended it",GREEN),
("3 of 4",3,"read a written rate-match guarantee as suspicious",NAVY),
("1 of 4",1,"had heard of AMB; none were swayed by customer-owned",NAVY),
("XXX of 4",0,"say a friend's good AMB experience would make them consider it",NAVY)]
for i,(big,k,cap,col) in enumerate(cards):
    x=0.5+i*2.3; W=2.15
    rrect(s,x,1.45,W,2.25,fill="FFFFFF",line=RULE,r=0.06)
    rect(s,x,1.45,W,0.05,fill=LEAF)
    for d in range(4):
        filled=d<k
        o=rect(s,x+0.25+d*0.42,1.72,0.34,0.34,fill=NAVY if filled else None,line=NAVY if not filled else None,lw=1.25,shape=MSO_SHAPE.OVAL)
        if not filled and k==0: text(s,x+0.25+d*0.42,1.72,0.34,0.34,[[("?","Calibri",11,NAVY,True)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
    text(s,x+0.25,2.2,W-0.4,0.55,[[(big,"Cambria",30,col,True)]])
    text(s,x+0.25,2.85,W-0.4,0.8,[[(cap,"Calibri",10.5,GREY,False)]])
rect(s,0,3.95,10,1.675,fill=NAVY)
text(s,0.5,3.9,0.8,1.0,[[("“","Cambria",72,"7FD6BC",True)]])
text(s,1.25,4.12,6.0,0.7,[[("She trusts her broker completely, and in three years he has never put a mutual bank in front of her.","Cambria",15,"FFFFFF",False)]])
text(s,1.25,4.85,6.0,0.4,[[("Broker-placed respondent. Comfort for the rest came from APRA regulation and an explanation of why the loan suits them.","Calibri",9.5,"AFC0DA",False)]])
s.shapes.add_picture(BR+"amb_logo_white_transparent.png",Inches(7.6),Inches(4.1),Inches(1.2),Inches(0.91))
geom(s,21,x=1.25,y=5.28,w=6.3,h=0.3); set_color(shp(s,21),"AFC0DA"); scale_font(shp(s,21),0.8)
for e in (21,): s.shapes._spTree.append(shp(s,e)._element)
pagenum_white(s,22)

# =============== S10: three-circle overlap + rate ribbon
s=sl[9]; clear(s,{3,4,31})
cols=[("Consideration set","(Court et al., 2009)","Brands outside the first two to four names rarely win.","AMB is outside the set in every channel we studied.",NAVY),
("Status quo bias","(Samuelson and Zeckhauser, 1988)","The familiar option holds unless a trigger and a reason arrive together.","A better rate was not enough for 7 of 10 DIY borrowers.","2A6F97"),
("Social proof","(Cialdini, 1984)","People copy people like them, especially under uncertainty.","A friend's experience was the strongest lever: XXX of 14.",LEAF)]
D=2.0
pos=[(1.8,1.4),(0.75,2.45),(2.85,2.45)]   # top-left of circles
for (x,y),c in zip(pos,(cols[0][4],cols[1][4],cols[2][4])):
    o=rect(s,x,y,D,D,fill=c,shape=MSO_SHAPE.OVAL); alpha(o,82)
text(s,2.1,1.7,1.4,0.5,[[("Consideration","Calibri",11,"FFFFFF",True)],[("set","Calibri",11,"FFFFFF",True)]],align=CW)
text(s,0.85,3.55,1.3,0.5,[[("Status quo","Calibri",11,"FFFFFF",True)],[("bias","Calibri",11,"FFFFFF",True)]],align=CW)
text(s,3.5,3.55,1.3,0.5,[[("Social","Calibri",11,"FFFFFF",True)],[("proof","Calibri",11,"FFFFFF",True)]],align=CW)
for i,(n,cite,theory,saw,c) in enumerate(cols):
    y=1.38+i*1.07
    rect(s,5.3,y,0.06,0.92,fill=c)
    text(s,5.5,y-0.02,4.0,0.3,[[(n,"Cambria",14,NAVY,True),("  "+cite,"Calibri",8.5,"8A94A6",False)]])
    text(s,5.5,y+0.29,4.0,0.3,[[(theory,"Calibri",10,GREY,False)]])
    text(s,5.5,y+0.6,4.0,0.32,[[("WE SAW  ","Calibri",8.5,GREEN,True),(saw,"Calibri",10.5,NAVY,True)]])
rect(s,0,4.65,10,0.975,fill=NAVY)
text(s,0.5,4.76,8.0,0.35,[[("The problem is not the rate. It is that the rate is never weighed.","Cambria",16,"FFFFFF",True)]])
text(s,0.5,5.13,8.3,0.4,[[("AMB advertises 5.94% up to 60% LVR and 6.19% at 60 to 80%, against 6.09 to 6.25% at the big four (AMB, Mozo, Sep 2026).","Calibri",9.5,"AFC0DA",False)]])
s.shapes.add_picture(BR+"amb_mark_white_transparent.png",Inches(8.75),Inches(4.76),Inches(0.75),Inches(0.45))
pagenum_white(s,31)

# =============== S11: budget bar linked to medallions
s=sl[10]; clear(s,{3,4,29,30})
segs=[("20%","$150k",1.8,"24607F"),("55%","$412.5k",4.95,NAVY),("15%","$112.5k",1.35,LEAF),("10%","test",0.9,"B8C2D6")]
x=0.5; centers=[]
for pct,amt,w,c in segs:
    rect(s,x,1.4,w-0.03,0.5,fill=c)
    dark=c=="B8C2D6"
    text(s,x,1.4,w-0.03,0.5,[[(pct,"Cambria",15,NAVY if dark else "FFFFFF",True),("  "+amt,"Calibri",10,NAVY if dark else "D6E3F0",False)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
    centers.append(x+(w-0.03)/2); x+=w
colspec=[(1.95,1.05,"pg4-001.png",0.5,"Make AMB easy to verify","Ratings, real rates and approval times, visible in search and AI answers.","The borrower's own check"),
(5.0,1.35,"pg4-005.png",0.5,"Enter the broker's working set","Panel accreditation (XXX), digital proof pack, aggregator listing, 48-hour turnaround.","The broker's shortlist"),
(8.05,0.9,"pg4-002.png",0.66,"Member check-your-offer link","A member sends one link; the friend uploads an offer; AMB returns a firm rate in 24 hours.","The friend's recommendation")]
MY=2.95
for k,(cx,d,ph,pcx,head,body,acts) in enumerate(colspec):
    line(s,centers[k],1.92,cx,MY-d/2-0.12,"8A94A6",1.0,dash=True)
    pic=s.shapes.add_picture(save(crop(P+ph,1.0,pcx,0.5),"s11m_%d.jpg"%k,minw=600),Inches(cx-d/2),Inches(MY-d/2),Inches(d),Inches(d))
    pic.auto_shape_type=MSO_SHAPE.OVAL
    rect(s,cx-d/2-0.07,MY-d/2-0.07,d+0.14,d+0.14,line=LEAF,lw=1.25,shape=MSO_SHAPE.OVAL)
    text(s,cx-1.4,3.75,2.8,0.3,[[(head,"Cambria",14,NAVY,True)]],align=CW)
    text(s,cx-1.3,4.08,2.6,0.6,[[(body,"Calibri",10,GREY,False)]],align=CW)
    rrect(s,cx-1.2,4.68,2.4,0.26,fill="E3F3EF",r=0.5)
    text(s,cx-1.2,4.68,2.4,0.26,[[("Acts on: ","Calibri",9.5,GREEN,True),(acts,"Calibri",9.5,NAVY,False)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
for xx in (3.475,6.525): pass

# =============== S12: roadmap lanes
s=sl[11]; clear(s,{3,4,38})
QX=2.7; QW=1.7
heads=[("Q1","Prove",NAVY),("Q2","Broker push","24607F"),("Q3","Scale","1B7A86"),("Q4","Scale what converts",LEAF)]
for i,(q,lab,c) in enumerate(heads):
    sh=rect(s,QX+i*QW,1.35,QW+(0.08 if i<3 else -0.02),0.5,fill=c,shape=MSO_SHAPE.PENTAGON if i==0 else MSO_SHAPE.CHEVRON)
    text(s,QX+i*QW+(0.2 if i==0 else 0.32),1.35,QW-0.3,0.5,[[(q+"  ","Cambria",12,"FFFFFF",True),(lab,"Calibri",10,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE)
for xx,lab in ((QX+QW,"Day 90"),(QX+2*QW,"Day 180")):
    line(s,xx-0.025,1.95,xx-0.025,5.1,"8A94A6",1,dash=True)
    rrect(s,xx-0.4,5.1,0.75,0.24,fill="FFFFFF",line="8A94A6",r=0.5)
    text(s,xx-0.4,5.1,0.75,0.24,[[(lab,"Calibri",9,GREY,True)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)

lanes=[("Verify online","Digital marketing","Reviews, ratings, rate and fee pages live","Search and AI visibility maintained"),
("Broker channel","Third-party distribution","Panel accreditation confirmed","Digital proof pack, aggregator listing, BDMs"),
("Member referral","Member experience","Pilot with XXX members","Link to all members; scale if it converts"),
("Measurement","Lending ops owns the 24-hour firm rate","Baseline and dashboards","Quarterly review; cut what does not convert")]
for i,(lane,owner,q1,rest) in enumerate(lanes):
    y=2.1+i*0.76
    rrect(s,0.5,y,2.1,0.62,fill=NAVY,r=0.2)
    text(s,0.65,y+0.07,1.9,0.28,[[(lane,"Calibri",11.5,"FFFFFF",True)]])
    text(s,0.65,y+0.34,1.9,0.26,[[(owner,"Calibri",8,"AFC0DA",False)]])
    rrect(s,QX,y,QW-0.05,0.62,fill=NAVY,r=0.2)
    text(s,QX+0.1,y,QW-0.25,0.62,[[(q1,"Calibri",9.5,"FFFFFF",False)]],anchor=MSO_ANCHOR.MIDDLE)
    rect(s,QX+QW,y,3*QW+0.05,0.62,fill="E3F3EF",shape=MSO_SHAPE.PENTAGON)
    rect(s,QX+QW,y,0.05,0.62,fill=LEAF)
    text(s,QX+QW+0.2,y,3*QW-0.4,0.62,[[(rest,"Calibri",11,NAVY,False)]],anchor=MSO_ANCHOR.MIDDLE)

# =============== S13: lead -> lag -> return flow
s=sl[12]; clear(s,{3,4,19,20})
spec=[(0.5,"Within a quarter","Lead indicators",NAVY,["Branded search volume, reviews and rating (target XXX)","Broker accreditations live; submissions per broker","Referral links sent, offers uploaded, firm rates issued","Time to firm rate (target 24h) and to conditional approval (48h)"]),
(3.85,"Within a year","Lag indicators",LEAF,["Shortlist inclusion rate, from a shopper survey","Conversion when AMB is shown, by channel","Funded loans and cost per funded loan, by channel","Members retained at 12 months; referrals per new member"])]
for x,when,name,c,items in spec:
    rrect(s,x,1.4,3.0,3.55,fill="FFFFFF",line=RULE,r=0.03)
    rect(s,x,1.4,3.0,0.06,fill=c)
    small_caps(s,x+0.2,1.58,2.6,when,color=c)
    text(s,x+0.2,1.8,2.6,0.4,[[(name,"Cambria",17,NAVY,True)]])
    for i,it in enumerate(items):
        y=2.38+i*0.62
        o=rect(s,x+0.2,y+0.04,0.3,0.3,fill=c,shape=MSO_SHAPE.OVAL)
        text(s,x+0.2,y+0.04,0.3,0.3,[[(str(i+1),"Calibri",10,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE,align=CW)
        text(s,x+0.62,y,2.25,0.55,[[(it,"Calibri",10,NAVY,False)]],anchor=MSO_ANCHOR.MIDDLE)
for x in (3.52,6.87):
    rect(s,x,2.95,0.28,0.4,fill="8A94A6",shape=MSO_SHAPE.CHEVRON)
rect(s,7.25,1.4,2.75,4.225,fill=NAVY)
s.shapes.add_picture(BR+"amb_mark_white_faint.png",Inches(7.1),Inches(3.9),Inches(2.9),Inches(1.7))
small_caps(s,7.5,1.58,2.2,"Return on the $750k",color="7FD6BC")
text(s,7.5,1.85,2.3,0.8,[[("XXX x","Cambria",42,"7FD6BC",True)]])
steps=[("$750k \u00f7 cost per funded loan ($XXX)","= XXX funded loans"),("\u00d7 lifetime margin per loan","$614k avg (ABS) \u00d7 NIM (XXX%) \u00d7 life (XXX yrs)"),("Return","= total lifetime margin \u00f7 $750k")]
for i,(a,b) in enumerate(steps):
    y=2.85+i*0.7
    line(s,7.5,y,9.7,y,"34497A",0.75)
    text(s,7.5,y+0.07,2.2,0.6,[[(a,"Calibri",10,"FFFFFF",True)],[(b,"Calibri",9,"AFC0DA",False)]])
geom(s,19,w=6.3); 
pagenum_white(s,20)
prs.save(F)
