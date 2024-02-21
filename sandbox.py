from multiprocessing import Pool
import threading
from queue import Queue

class MyProcessThreadPool:
    def __init__(self, processes=4,thread_num=4):
        self.process_num=processes
        self.thread_num=thread_num


    def thread_task(self,*args, **kwargs):

        print(f"ProcessID: {args[0]}, ThreadID: {args[1]}, kwargs: {kwargs}")
        result=args[2]
        result[args[1]]=args[0]*10+args[1]

    def task_with_threads(self,process_id):

        results=[0]*self.thread_num
        threads=[threading.Thread(target=self.thread_task, args=(process_id,i,results),kwargs={"msg":"114514"})for i in range(self.thread_num)]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        print(results)
        return results

    def turn_on(self):
        pool=Pool(self.process_num)
        rst=[pool.apply_async(self.task_with_threads,args=(i,)) for i in range(4)]

        output=[item.get() for  item in rst]
        print(output)

        pool.close()
        pool.join()

    def print_err(self,e):
        print(e)

if __name__ == '__main__':

    MyProcessThreadPool().turn_on()