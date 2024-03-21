import threading
import time

def thread_function(name):
    print("Thread",name,'started')
    time.sleep(2)
    print("Thread",name,'finished')

def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target= thread_function,args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have been finished")

if __name__ == '__main__':
    main()                
