import sys; sys.path.insert(0,"build")
from common import *
SRC="build/baseline.pptx"
prs=Presentation(SRC)
P="photos/"

# ---------------- slide 7: two photos side by side, text over lower-third gradient
s=prs.slides[6]
clear(s,{3,4,25})
cards=[
 dict(x=0.5, photo="pg13-000.png", cx=0.5, cy=0.5, tag="PRIORITY 1", name="DIY online borrowers",
      body="Build their own shortlist in search, comparison sites and AI tools, the channels a digital budget touches directly. Refinancers and upgraders behave the same way once a trigger fires.",
      job="Confirm a better deal is safe before committing"),
 dict(x=5.1, photo="pg9-000.png", cx=0.5, cy=0.5, tag="PRIORITY 2", name="Broker-placed borrowers",
      body="Four in five loans. The broker builds the shortlist from lenders they know and can place quickly. Brokers do not need to hear of AMB; they need a reason to swap a familiar name for it.",
      job="Get a loan sorted without becoming an expert"),
]
Y=1.3; W=4.4; H=3.0
for c in cards:
    im=crop(P+c["photo"],W/H,c["cx"],c["cy"])
    im=gradient_lower(im)
    path=save(im,"s7_%s.jpg"%c["photo"][:-4])
    s.shapes.add_picture(path,Inches(c["x"]),Inches(Y),Inches(W),Inches(H))
    pill=rect(s,c["x"]+0.25,Y+0.2,1.1,0.26,fill=GREEN)
    text(s,c["x"]+0.25,Y+0.2,1.1,0.26,[[(c["tag"],"Calibri",10,"FFFFFF",True)]],anchor=MSO_ANCHOR.MIDDLE,align=PP_ALIGN.CENTER)
    text(s,c["x"]+0.25,Y+1.32,3.9,0.38,[[(c["name"],"Cambria",20,"FFFFFF",True)]])
    text(s,c["x"]+0.25,Y+1.76,3.9,0.8,[[(c["body"],"Calibri",11,"EEF2F8",False)]])
    # white floating card straddling the photo's lower edge
    cy=Y+H-0.28
    rect(s,c["x"]+0.25,cy,3.9,0.52,fill="FFFFFF",line=RULE)
    rect(s,c["x"]+0.25,cy,0.05,0.52,fill=LEAF)
    text(s,c["x"]+0.42,cy,3.65,0.52,[[("Job to be done: ","Calibri",11,GREEN,True),(c["job"],"Calibri",11,NAVY,True)]],anchor=MSO_ANCHOR.MIDDLE)
# not-prioritised: accent rule + plain text (no card)
rect(s,0.5,4.84,0.5,0.03,fill=LEAF)
text(s,0.5,4.94,8.3,0.5,[[("Not prioritised  ","Calibri",10.5,NAVY,True),
 ("Borrowers who go straight to the family's big-four bank have no evaluation step to intercept. First-home, refinance and upgrade are triggers rather than channels: when they fire, the person either searches online or calls a broker, so the two moves above reach them.","Calibri",10.5,GREY,False)]])

# ---------------- slide 11: circular medallions, diameter scaled to budget share
s=prs.slides[10]
clear(s,{3,4,29,30})
cols=[
 dict(x=0.5, d=1.1, photo="pg4-001.png", pct="20%", amt="$150k · owned + earned", head="Make AMB easy to verify",
      body="Reviews on Google and ProductReview, independent ratings, APRA and Roy Morgan proof, real rates, fees and approval times on the site; visible in search and AI answers.",
      acts="Acts on: The borrower's own check"),
 dict(x=3.55, d=1.34, photo="pg4-005.png", pct="55%", amt="$412.5k · paid + owned", head="Enter the broker's working set",
      body="Confirm AMB brand accreditation on the major panels (XXX); a digital proof pack and listing on aggregator broker platforms; live tracking of a 48-hour turnaround commitment; BDM coverage behind it.",
      acts="Acts on: The broker's shortlist"),
 dict(x=6.6, d=0.9, photo="pg4-002.png", cx=0.66, pct="15%", amt="$112.5k · earned", head="Member check-your-offer link",
      body="A member sends a friend one link; the friend uploads the offer they already have; AMB returns a firm rate within 24 hours. Tracked from link to settlement.",
      acts="Acts on: The friend's recommendation"),
]
CW=2.9; MY=1.97
for x in (3.475,6.525): rect(s,x,1.45,0.01,3.4,fill=RULE)
for c in cols:
    cx=c["x"]+CW/2; d=c["d"]
    sq=crop(P+c["photo"],1.0,c.get("cx",0.5),0.5)
    path=save(sq,"s11_%s.jpg"%c["photo"][:-4],minw=600)
    pic=s.shapes.add_picture(path,Inches(cx-d/2),Inches(MY-d/2),Inches(d),Inches(d))
    pic.auto_shape_type=MSO_SHAPE.OVAL
    rg=rect(s,cx-d/2-0.07,MY-d/2-0.07,d+0.14,d+0.14,line=LEAF,lw=1.25,shape=MSO_SHAPE.OVAL)
    L=c["x"]+0.1; w=CW-0.2
    text(s,L,2.76,w,0.5,[[(c["pct"],"Cambria",30,NAVY,True)]],align=PP_ALIGN.CENTER)
    text(s,L,3.26,w,0.22,[[(c["amt"],"Calibri",10.5,GREEN,False)]],align=PP_ALIGN.CENTER)
    text(s,L,3.52,w,0.28,[[(c["head"],"Calibri",14,NAVY,True)]],align=PP_ALIGN.CENTER)
    text(s,L+0.05,3.84,w-0.1,0.8,[[(c["body"],"Calibri",10,GREY,False)]],align=PP_ALIGN.CENTER)
    text(s,L,4.76,w,0.22,[[(c["acts"],"Calibri",10.5,GREEN,True)]],align=PP_ALIGN.CENTER)
prs.save("AMB_Draft_4_remaster_wip.pptx")
