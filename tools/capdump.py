#!/usr/bin/env python3
import argparse,json,subprocess,datetime
p=argparse.ArgumentParser();p.add_argument("--out",required=True);p.add_argument("--vulkaninfo",default="vulkaninfo");p.add_argument("--device",default="unknown");p.add_argument("--commit");a=p.parse_args()
r=subprocess.run([a.vulkaninfo,"--json"],capture_output=True,text=True)
d={"schema_version":1,"time":datetime.datetime.now(datetime.timezone.utc).isoformat(),"device":a.device,"commit":a.commit,"rc":r.returncode,"stderr":r.stderr}
try:d["vulkaninfo"]=json.loads(r.stdout)
except:d["stdout"]=r.stdout
json.dump(d,open(a.out,"w"),indent=2);print(a.out)
