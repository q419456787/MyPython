from multiprocessing import  Pool
import  os,time,random


def async_method(name):
    print('current Task named %s and its Id %d'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task named %s-%d have runed %0.2f'%(name,os.getpid(),end-start))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())

    p=Pool(4)
    for index in range(5):
        p.apply_async(async_method,args=(str(index),))

    print('Waiting for all subprocesses done...')
    p.close()##这里是必须先close,不让新的进程继续加入
    p.join()
    print('All subprocesses done.')
