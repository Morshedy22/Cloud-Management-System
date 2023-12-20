import subprocess
class docker:
    def __init__(self,directoryoffile=None,workdirectory=None,dependencies=None,port=None,filerunname=None,imageused=None):
        self.directoryoffile=directoryoffile
        self.workdirectory= workdirectory
        self.dependencies= dependencies
        self.port=port
        self.filerunname=filerunname
        self.imageused=imageused
        

    def buildfile(self):
        try:
            content=f"""\
            FROM {self.imageused}

            WORKDIR {self.workdirectory}

            COPY {self.directoryoffile} {self.workdirectory}

            RUN pip install --no-cache-dir {self.dependencies}

            EXPOSE {self.port}

        
            CMD ["python", "{self.filerunname}"]
            """ 
            full_path= self.directoryoffile + "/Dockerfile"
            with open(full_path, "w") as dockerfile:
                dockerfile.write(content)
            
            return True
        except:
            return False
        
    def build_image(self,imgname,directory):
        #input locate a file first
        second_direct=directory[:-12] + "\""
        cmd = f"docker build -t {imgname} -f {directory} {second_direct}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result
    def list_images():
        cmd="docker images"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result
    
    def run_image_with_container(imgname,containername):
        cmd= f"docker run --name {containername} {imgname}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result

    def list_containers():
      command= f"docker images"
      result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
      return result
    def stop_container(name):
        command= f"docker stop {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result
    def search_image(name):
        command= f"docker search {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result
    def pull_image(name):
        command=f"docker pull {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result

