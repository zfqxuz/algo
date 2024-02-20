from multiprocessing import Pool
import threading



class MyProcessThreadPool:
    def __init__(self, processes=4):
       pass


    def thread_task(self,*args, **kwargs):
        # 实例方法，作为线程要执行的任务
        print(f"Thread task args: {args}, kwargs: {kwargs}")

    def task_with_threads(self):
        num_threads=4
        threads = [threading.Thread(target=self.thread_task, args=(i,),kwargs={"msg":"114514"}) for i in range(num_threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def turn_on(self):
        pool=Pool(4)
        for i in range(4):
            pool.apply(self.task_with_threads)
        self.close(pool)

    def print_err(self,e):
        print(e)

    def close(self,pool):
        # 关闭进程池，不再接受新的任务
        pool.close()
        pool.join()


def task_with_threads():
    num_threads=4
    threads = [threading.Thread(target=thread_task, args=(i,),kwargs={"msg":"114514"}) for i in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def thread_task(*args, **kwargs):
    # 实例方法，作为线程要执行的任务
    print(f"Thread task args: {args}, kwargs: {kwargs}")

if __name__ == '__main__':

    MyProcessThreadPool().turn_on()