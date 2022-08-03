import sys

# modify from https://blender.stackexchange.com/questions/3219/how-to-show-to-the-user-a-progression-in-a-script

def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    sys.stdout.write(msg)
    sys.stdout.flush()

def finish_progress():
    sys.stdout.write(' 100% \n')
    sys.stdout.flush()
