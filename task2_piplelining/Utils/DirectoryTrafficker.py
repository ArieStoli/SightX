"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirectoryTrafficker:
    
    def __init__(target_path: str):
        self.__path = target_path
        self.__event_handler = FileSystemEventHandler()
        self.__observer = Observer()
        
    def init_observer(self, on_created_func):
        self.__event_handler.on_created = on_created_func
        self.__observer.schedule(self.__event_handler, self.__pat, recursive=False)
        self.__observer.start()
        
    def shutdown(self):
        self.__observer.stop()
    
    def copy_file(src, dst):
        shutil(src, dst)
        
    