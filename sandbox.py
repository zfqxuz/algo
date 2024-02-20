from multiprocessing import Pool
import threading

class MyProcessThreadPool:
    def __init__(self, processes=4,thread_num=4):
        self.process_num=processes
        self.thread_num=thread_num


    def thread_task(self,*args, **kwargs):

        print(f"ProcessID: {args[0]}, ThreadID: {args[1]}, kwargs: {kwargs}")

    def task_with_threads(self,process_id):

        threads = [threading.Thread(target=self.thread_task, args=(process_id,i),kwargs={"msg":"114514"}) for i in range(self.thread_num)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def turn_on(self):
        pool=Pool(self.process_num)
        for i in range(4):
            pool.apply(self.task_with_threads,args=(i,))
        pool.close()
        pool.join()
    def print_err(self,e):
        print(e)

if __name__ == '__main__':

    MyProcessThreadPool().turn_on()