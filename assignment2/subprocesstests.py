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