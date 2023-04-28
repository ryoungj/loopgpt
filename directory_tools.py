from loopgpt.tools import BaseTool
import os

class CurrentWorkingDir(BaseTool):
    @property
    def args(self):
        return {}
    
    @property
    def resp(self):
        return {"report": "The current working directory"}
    
    @property
    def id(self):
        return "current_directory"

    @property
    def desc(self):
        return "The current working directory/folder"

    def run(self):
        try:
            data = os.getcwd()
            data = {"report": data}
            return data
        except Exception as e:
            return {"report": f"An error occurred while getting the current working directory: {e}."}
        
class ListDirectories(BaseTool): 
    @property
    def args(self):
        return {"path": "path/to/directory"}
    
    @property
    def resp(self):
        return {"report": "The list of directories in the path"}
    
    @property
    def id(self):
        return "list_directories"

    @property
    def desc(self):
        return "List directories in a given path"

    def run(self, path):
        try:
            data = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
            data = {"report": data}
            return data
        except Exception as e:
            return {"report": f"An error occurred while getting directories list: {e}."}

class MakeDirectory(BaseTool): 
    @property
    def args(self):
        return {"newpath": "path/to/directory"}
    
    @property
    def resp(self):
        return {"report": "The path to the directory to be made"}
    
    @property
    def id(self):
        return "make_dir"

    @property
    def desc(self):
        return "Make a directory/folder to the given path"

    def run(self, newpath):
        try:
            def make_dir(newdirpath):
                if not os.path.isdir(newdirpath):
                    os.makedirs(newdirpath)
            make_dir(newpath)
            return {"report": f"Directory '{newpath}' was created" }
        except Exception as e:
            return {"report": f"An error occurred while creating a new directory path: {e}."}

DirectoryTools = [
    CurrentWorkingDir,
    ListDirectories,
    MakeDirectory
]