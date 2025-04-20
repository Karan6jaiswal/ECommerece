import schedule
import time
import subprocess

# === Define what each task does ===

def run_script_1():
    print("Running script1.py")
    subprocess.run(["python", "jiomart2.py"])

def run_script_2():
    print("Running script2.py")
    subprocess.run(["python", "zep2.py"])

def run_script_3():
    print("Running script3.py")
    subprocess.run(["python", "sig2.py"])

# === Schedule each task ===

# Run script1 every 10 seconds
schedule.every().day.at("00:00").do(run_script_3)
run_script_1()
# Run script2 every 1 minute
schedule.every().day.at("01:00").do(run_script_3)
run_script_2()
# # Run script3 every day at 2 PM
schedule.every().day.at("02:00").do(run_script_3)
run_script_3()
# === Keep checking for scheduled tasks ===

while True:
    schedule.run_pending()
    time.sleep(1)
