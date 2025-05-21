import subprocess
from typing import Union
from typing import Any
import time
import psutil

from libLog import Log
import time
from concurrent.futures import ThreadPoolExecutor

#----------------------------------------------------------------
class ProcessAsync():
    def __init__(self):
        super().__init__()
        self.pid = 0
        self.funcFinal = None
        self.funcPolling = None
        self.process = None
        self.command = ""

    def polling(self):
        while True:
            buff = []
            for proc in psutil.process_iter():
                buff += {proc.pid}

            if self.pid in buff:
                if self.funcPolling is not None:
                    self.funcPolling(self.process)
                else:
                    time.sleep(3)
                buff.clear()
            else:
                break

        if self.funcPolling is not None:
            self.funcPolling()


    def execAsync(self, command:str, pollingFunc = None, finalFunc = None) -> bool:
        # バックグラウンド実行
        self.command = command
        #Log.message(command)
        #process = subprocess.Popen(command,stdout=subprocess.PIPE)
        self.process = subprocess.Popen(self.command)
        if self.process.stderr is not None:
            return False
        
        self.pid = self.process.pid
        return True

    def execCommand(self, command:str, f) -> None:
        result = subprocess.run(command)
        f()
    
    def execAsync2(self, command:str, finalFunc:str) -> bool:
        with ThreadPoolExecutor(max_workers=10) as executor:
            a = executor.submit(self.execCommand, command, finalFunc)
            #a.add_done_callback(finalFunc)
        
#----------------------------------------------------------------