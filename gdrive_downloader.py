import sys
s = sys.argv
FILE_ID = s[1]
cmd = f"wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={FILE_ID}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p')&id={FILE_ID}\" -O filename && rm -rf /tmp/cookies.txt"

print(cmd)

with open("./tmp.sh", "w") as f:
    f.write(cmd)

import subprocess
subprocess.check_call(["bash", "tmp.sh"])
