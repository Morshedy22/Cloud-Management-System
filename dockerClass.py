import subprocess
class docker:
    def __init__(self,directoryoffile=None,workdirectory=None,dependencies=None,port=None,filerunname=None,imageused=None):
        self.directoryoffile=directoryoffile
        self.workdirectory= workdirectory
        self.dependencies= dependencies
        self.port=port
        self.filerunname=filerunname
        self.imageused=imageused
        self.extra_comments=''


    def buildrawfile(self,content ,directory):
        try:
            full_path= directory + "/Dockerfile"
            with open(full_path, "w") as dockerfile:
                    dockerfile.write(content)
                
            return True
        except:
                return False
        
    def buildfile(self,case_number):
        
            
        command="RUN pip install --no-cache-dir"
        if case_number=="1" or case_number=="3":
            try:
                self.dependencies=self.dependencies.split()
                txt=''
                for i in self.dependencies:
                    txt= txt+ command
                    txt= txt + ' '+i
                    txt+='\n'
            except:
                txt=''
        run_command=self.filerunname.split()
        final_list=[]
        for item in run_command:
            final_list.append(item.replace("'", '"'))

        

            
        if case_number=="1":
            try:
                content=f"""\
                FROM {self.imageused}

                WORKDIR {self.workdirectory}

                COPY . {self.workdirectory}

                {txt}

                EXPOSE {self.port}
                {self.extra_comments}
            
                CMD {final_list}
                """ 
                full_path= self.directoryoffile + "/Dockerfile"
                with open(full_path, "w") as dockerfile:
                    dockerfile.write(content)
                
                return True
            except:
                return False
        elif case_number=="2":
            try:
                content=f"""\
                FROM {self.imageused}

                WORKDIR {self.workdirectory}

                COPY . {self.workdirectory}

                RUN pip install --no-cache-dir -r requirements.txt

                EXPOSE {self.port}

                {self.extra_comments}
                CMD {final_list}
                """ 
                full_path= self.directoryoffile + "/Dockerfile"
                with open(full_path, "w") as dockerfile:
                    dockerfile.write(content)
                
                return True
            except:
                return False
        elif case_number=="3":
            try:
                content=f"""\
                FROM {self.imageused}

                WORKDIR {self.workdirectory}

                COPY . {self.workdirectory}

                {txt}
                {self.extra_comments}

            
                CMD {final_list}
                """ 
                full_path= self.directoryoffile + "/Dockerfile"
                with open(full_path, "w") as dockerfile:
                    dockerfile.write(content)
                
                return True
            except:
                return False
        elif case_number=="4":
            try:
                content=f"""\
                FROM {self.imageused}

                WORKDIR {self.workdirectory}

                COPY . {self.workdirectory}

                RUN pip install --no-cache-dir -r requirements.txt
                {self.extra_comments}
                

            
                CMD {final_list}
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
        cmd = f"docker build -t {imgname} \"{directory}\""
        
        output=''

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in iter(process.stdout.readline, ""):
            output+=line # Auto-scroll to the end

        process.stdout.close()
        return_code = process.wait()
        return output
          # Auto-scroll to the end

       

    def list_images(self):
        cmd="docker images"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result
    
    def run_image_with_container(self,imgname,containername):
        cmd= f"docker run -d --name {containername} {imgname}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result

    def list_containers(self):
      command= f"docker ps"
      result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
      return result
    def stop_container(self,name):
        command= f"docker stop {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result
    def search_image(self,name):
        command= f"docker search {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result
    def pull_image(self,name):
        command=f"docker pull {name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result
    def list_all_containers(self):
        command= "docker ps -a"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
