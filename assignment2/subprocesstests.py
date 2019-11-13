import subprocess
import re
# Trying to find a method of communicating with a subprocess's event loop

"""
sts = subprocess.run(['python3', 'assignment2.py', 'cnnhealth.txt'],stdout=subprocess.PIPE,input='q\n',encoding='ascii')    
print(sts.returncode)
print(sts.stdout)
"""

"""
def test_eval_quit2(self):
    subprocess.run(["python3", "assignment2.py", "cnnhealth.txt"; "q"])
    s = subprocess.check_call("python3 assignment2.py cnnhealth.txt;q", shell = True)
    print("Return code", s)
"""

# open shell, running that file and one of the tweet files
# enter q
#os.system('python3 assignment2.py cnnhealth.txt')

q = subprocess.run(['pwd'],stdout=subprocess.PIPE)
print(q.stdout)

p = subprocess.run(['python3', 'assignment2.py','bbchealth.txt'], stdout=subprocess.PIPE, input='n\nn\np\np\n36\nf\nq\n', encoding='ascii')
print(p.returncode)
stripped = re.sub(r"([\s\t\n])", r"", p.stdout.strip())
print(stripped)

# ['\s+','\n+','\t+']