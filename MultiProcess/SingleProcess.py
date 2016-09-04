from multiprocessing import  Process

import  os

def run_proc(name):
    print('run child process named %s, and processId %d'%(name,os.getpid()))

if __name__=='__main__':
    p=Process(target=run_proc,args=('childProceess',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')