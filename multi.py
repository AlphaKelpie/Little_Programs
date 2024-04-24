import multiprocessing as mp
from datetime import datetime as dt
from time import sleep

def fun(i) :
  sleep(2)
  with open(f'./{i}.txt', 'w') as file:
    file.write(f'File {i}')

if __name__ == "__main__" :
  NUM = 16
  pool = mp.Pool(NUM)
  START = dt.now()
  pool.map(fun, range(NUM))
  pool.close()
  pool.join()
  END = dt.now()
  TIME = END - START
  print(f"Tempo:\t{TIME}")
