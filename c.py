import threading
import time
import logging

class worker:

   def __init__(self,num):
      self.num=num

   def worker1(self):
      time.sleep(0.03)
      logging.debug("enter - hi my name is eli")
      print("worker ", self.num)
      logging.info("exit")
      return

logging.basicConfig( level=logging.DEBUG,
                     format='[%(levelname)s] (%(threadName)-10s) %(message)s'
                                  )
threads=[]
for i in range(5):
   w1 = worker(i)
   t=threading.Thread(target=w1.worker1())
   print(threading.currentThread().getName())
   threads.append(t)
   t.start()