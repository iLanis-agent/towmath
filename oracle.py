import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def nneg(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>=0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r5(x): return jround(x/5)*5

def tongue_plan(trailerLb):
    if not pos(trailerLb): return {"error":"the trailer weight must be above zero"}
    return {"low":r5(trailerLb*0.10),"high":r5(trailerLb*0.15)}

def render_tongue(r,trailerLb):
    return ("Your "+jsnum(trailerLb)+" lb trailer puts "+jsnum(r["low"])+"-"+jsnum(r["high"])
            +" lb on the hitch - the tongue weight the payload sticker will feel, before anyone climbs in.")

def payload_plan(payload,people,cargo,tongue):
    if not pos(payload): return {"error":"the payload rating must be above zero"}
    if not nneg(people) or not nneg(cargo) or not nneg(tongue): return {"error":"weights cannot go below zero"}
    left=payload-people-cargo-tongue
    return {"left":jround(left),"over":left<0}

def render_payload(r,payload,people,cargo,tongue):
    s=("After "+jsnum(people)+" lb of people, "+jsnum(cargo)+" lb of cargo and "+jsnum(tongue)
       +" lb of tongue, your "+jsnum(payload)+" lb payload ")
    if r["over"]: return s+"is over the sticker by "+jsnum(abs(r["left"]))+" lb - something gets left behind."
    return s+"has "+jsnum(r["left"])+" lb of margin."

def brake_plan(trailerLb):
    if not pos(trailerLb): return {"error":"the trailer weight must be above zero"}
    if trailerLb<1500: verdict="below the usual brake-law bite, but lights and the rating still apply"
    elif trailerLb<3000: verdict="in the gray zone - some states already want brakes here"
    else: verdict="over the common 3,000 lb line - trailer brakes and a controller are the honest plan"
    return {"verdict":verdict}

def render_brake(r,trailerLb):
    return "At "+jsnum(trailerLb)+" lb the trailer is "+r["verdict"]+". Rules differ by state and speed - check yours."

cases=[]
def add(tool,args):
    if tool=="tongue": r=tongue_plan(*args); fn=render_tongue
    elif tool=="payload": r=payload_plan(*args); fn=render_payload
    else: r=brake_plan(*args); fn=render_brake
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(5000,),(3500,),(1500,),(7000,),(2200,),(1200,),(4800,),(2990,)]:
    add("tongue",a)
for a in [(1500,400,200,600),(1800,500,300,750),(1200,300,150,300),(2000,600,400,1100),(1000,350,250,480),(1600,450,100,900),(1400,300,200,200)]:
    add("payload",a)
for a in [(2800,),(3200,),(1200,),(4500,),(1490,),(2990,)]:
    add("brake",a)
add("tongue",[0]); add("payload",[0,300,200,500]); add("payload",[1500,-50,0,0]); add("brake",[0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
