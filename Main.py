import tkinter as tk
from tkinter import filedialog
import multiprocess as mp
from qemuClass import*
import subprocess
from dockerClass import *

docker_instance=docker()

class VMManagerGUI:

    def __init__(self, master):
        self.master = master
        master.title("VM Manager and Dockerfile Generator")
        master.resizable(False, False)
        # Set a color scheme
        self.background_color = "#162447"  # Dark blue
        self.frame_color = "#1F4068"  # Teal
        self.button_color = "#F9A03F"  # Orange

        master.configure(bg=self.background_color)
        
        # create object virtual machine
        self.vm = VirtualMachine()
        # create object virtual machine
        

        # Create VM Frame
        self.vm_frame = tk.Frame(master, bg=self.frame_color)
        self.vm_frame.pack(pady=50)
        # Create docker Frame
        self.docker_frame = tk.Frame(master, bg=self.frame_color)
        self.docker_frame.pack(pady=20)

        self.vm_label = tk.Label(self.vm_frame, text="Create Virtual Machine", font=("Helvetica", 20, "bold"),
                                 bg=self.frame_color, fg="white")
        self.vm_label.grid(row=0, column=0, columnspan=2, pady=15)
        self.docker_label = tk.Label(self.docker_frame, text="Create Dockerfile", font=("Helvetica", 20, "bold"),
                                     bg=self.frame_color, fg="white")
        self.docker_label.grid(row=0, column=3, columnspan=2, pady=15)

        self.create_vm_button = tk.Button(self.vm_frame, text="Create VM", command=self.create_vm, bg=self.button_color,
                                          fg="white", font=("Helvetica", 14))
        self.create_vm_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Create Dockerfile Frame


        # Create Dockerfile Frame

        self.dockerfile_label = tk.Label(self.docker_frame, text="Create Dockerfile",
                                         font=("Helvetica", 20, "bold"),
                                         bg=self.frame_color, fg="white")
        self.dockerfile_label.grid(row=0, column=3, columnspan=2, pady=15)

        self.create_dockerfile_button = tk.Button(self.docker_frame, text="Create Dockerfile",
                                                  command=self.create_dockerfile_popup, bg=self.button_color,
                                                  fg="white",
                                                  font=("Helvetica", 14))
        self.create_dockerfile_button.grid(row=5, column=3, columnspan=2, pady=15)

        self.build_docker_button = tk.Button(self.docker_frame, text="Build Docker Image",
                                             command=self.build_docker_image_popup, bg=self.button_color, fg="white",
                                             font=("Helvetica", 14))
        self.build_docker_button.grid(row=5, column=5, columnspan=2, pady=15)

        self.list_images_button = tk.Button(self.docker_frame, text="List Docker Images",
                                            command=self.list_images_popup, bg=self.button_color, fg="white",
                                            font=("Helvetica", 14))
        self.list_images_button.grid(row=7, column=5, columnspan=2, pady=15)

        self.run_image_button = tk.Button(self.docker_frame, text="Run Docker Image with Container",
                                          command=self.run_docker_image_with_container_popup, bg=self.button_color,
                                          fg="white", font=("Helvetica", 14))
        self.run_image_button.grid(row=8, column=1, columnspan=2, pady=15)

        self.list_containers_button = tk.Button(self.docker_frame, text="List Docker Containers",
                                                command=self.show_container_list, bg=self.button_color, fg="white",
                                                font=("Helvetica", 14))
        self.list_containers_button.grid(row=6, column=0, columnspan=2, pady=15)

        self.stop_container_button = tk.Button(self.docker_frame, text="Stop Docker Container",
                                               command=self.ask_container_name_stop, bg=self.button_color,
                                               fg="white", font=("Helvetica", 14))
        self.stop_container_button.grid(row=7, column=0, columnspan=2, pady=15)

        self.search_image_button = tk.Button(self.docker_frame, text="Search Docker Image",
                                             command=self.ask_image_name, bg=self.button_color, fg="white",
                                             font=("Helvetica", 14))
        self.search_image_button.grid(row=8, column=5, columnspan=2, pady=15)

        self.pull_image_button = tk.Button(self.docker_frame, text="Pull Docker Image",
                                           command=self.ask_pullimage_name, bg=self.button_color, fg="white",
                                           font=("Helvetica", 14))
        self.pull_image_button.grid(row=6, column=5, columnspan=2, pady=15)

        self.list_all_container = tk.Button(self.docker_frame, text="List all containers",
                                            command=lambda: self.show_output_popup("List All containers Result",
                                                                                   docker_instance.list_all_containers()),
                                            bg=self.button_color, fg="white",
                                            font=("Helvetica", 14))
        self.list_all_container.grid(row=5, column=0, columnspan=2, pady=15)

    # Qemu Function
    def create_vm(self):
        self.vmWindow = tk.Toplevel(self.master)
        self.vmWindow.title("Create Virtual Machine")
        self.vmWindow.geometry("300x300")
        self.vmWindow.resizable(False, False)
        self.vmWindow.transient(self.master)

        self.vmWindow.configure(bg=self.background_color)

        # Create Disk Frame
        self.disk_frame = tk.Frame(self.vmWindow, bg=self.frame_color)
        self.disk_frame.pack(pady=20)

        self.disk_label = tk.Label(self.disk_frame, text="Create Disk Image", font=("Helvetica", 15, "bold"),
                                    bg=self.frame_color, fg="white")
        self.disk_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.create_disk_button = tk.Button(self.disk_frame, text="Create Image", command=self.createDisk,
                                            bg=self.button_color, fg="white", font=("Helvetica", 14))
        self.create_disk_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Create Boot Frame
        self.boot_frame = tk.Frame(self.vmWindow, bg=self.frame_color)
        self.boot_frame.pack(pady=30)

        self.boot_label = tk.Label(self.disk_frame, text="Boot Menu", font=("Helvetica", 15, "bold"),
                                    bg=self.frame_color, fg="white")
        self.boot_label.grid(row=5, column=0, columnspan=2, pady=15)

        self.create_boot_button = tk.Button(self.disk_frame, text="Boot Menu", command=self.bootVM,
                                            bg=self.button_color, fg="white", font=("Helvetica", 14))
        self.create_boot_button.grid(row=7, column=0, columnspan=2, pady=15)
    def createDisk(self):
        self.diskWindow = tk.Toplevel(self.vmWindow)
        self.diskWindow.title("Create Disk Image")
        self.diskWindow.geometry("180x240")
        self.diskWindow.resizable(False, False)
        self.diskWindow.transient(self.vmWindow)

        self.diskWindow.configure(bg=self.background_color)

        name_label = tk.Label(self.diskWindow, text="Name", bg=self.frame_color, fg="white")
        name_label.grid(row=0, column=0, columnspan=2, pady=15)
        name_label.pack()

        name_input = tk.Entry(self.diskWindow, width=10)
        name_input.pack()

        size_label = tk.Label(self.diskWindow, text="Size (Mb)", bg=self.frame_color, fg="white")
        size_label.pack()

        size_input = tk.Entry(self.diskWindow, width=10)
        size_input.pack()

        location_label = tk.Label(self.diskWindow, text="Location", bg=self.frame_color, fg="white")
        location_label.pack()

        def get_directory():
            directory = filedialog.askdirectory()
            location_label.configure(text=directory)

        location_button = tk.Button(self.diskWindow, text="Choose", command=get_directory, bg=self.button_color)
        location_button.pack()

        space = tk.Label(self.diskWindow, text="")
        space.pack()

        def create():
            name = name_input.get()
            size = size_input.get()
            location = location_label.cget("text")
            self.vm.CreateImage(name, size, location)

        def cancel():
            self.diskWindowwindow.destroy()

        create_button = tk.Button(self.diskWindow, text="Create", command=create, bg=self.button_color)
        create_button.pack()

        cancel_button = tk.Button(self.diskWindow, text="Cancel", command=cancel, bg=self.button_color)
        cancel_button.pack()
    def bootVM(self):

        self.bootWindow = tk.Toplevel(self.vmWindow)
        self.bootWindow.title("boot virtual Machine")
        self.bootWindow.geometry("240x290")
        self.bootWindow.resizable(False, False)
        self.bootWindow.transient(self.vmWindow)

        self.bootWindow.configure(bg=self.background_color)

        cores_label = tk.Label(self.bootWindow, text="Cores", bg=self.frame_color, fg="white")
        cores_label.pack()

        cores_input = tk.Entry(self.bootWindow, width=10)
        cores_input.pack()

        ram_label = tk.Label(self.bootWindow, text="Ram", bg=self.frame_color, fg="white")
        ram_label.pack()

        ram_input = tk.Entry(self.bootWindow, width=10)
        ram_input.pack()

        def get_disk_directory():
            directory = filedialog.askopenfilename()
            disk_label.configure(text=directory)

        disk_label = tk.Label(self.bootWindow, text="Disk Image", bg=self.frame_color, fg="white")
        disk_label.pack()

        disk_button = tk.Button(self.bootWindow, text="Choose", command=get_disk_directory, bg=self.background_color)
        disk_button.pack()

        def get_iso_directory():
            directory = filedialog.askopenfilename()
            iso_label.configure(text=directory)

        iso_label = tk.Label(self.bootWindow, text="Iso file (leave blank to skip)")
        iso_label.pack()

        iso_button = tk.Button(self.bootWindow, text="Choose", command=get_iso_directory)
        iso_button.pack()

        def create():
            ram = ram_input.get()
            cores = cores_input.get()
            disk_directory = disk_label.cget("text")
            iso_directory = iso_label.cget("text")

            self.vm.boot(ram, cores, disk_directory, iso_directory)

        def cancel():
            self.bootWindow.destroy()

        create_button = tk.Button(self.bootWindow, text="Boot", command=create)
        create_button.pack()


        cancel_button = tk.Button(self.bootWindow, text="Cancel", command=cancel)
        cancel_button.pack()

    # --------------------------------------------------------------------------------------------------
    
    #Docker function
    def create_dockerfile_popup(self):
         def select_directory(entry):
            directory = filedialog.askdirectory()
            if directory:
                entry.config(state="normal")
                # Do something with the selected directory (e.g., print it)
                text_to_write = directory
                entry.delete(0, tk.END)  # Clear existing content
                entry.insert(0, text_to_write)
                entry.config(state="readonly")
         def on_dependency_click():
            value = checkbox_dependency_var.get()
            
            if value: # Clear existing content
                dependencies_entry.config(state="normal")
                dependencies_entry.delete(0, tk.END)
                dependencies_entry.config(state="readonly")
                return True
            else:
                dependencies_entry.config(state='normal')
                return False
            
         def on_port_click():
            value = checkbox_port_var.get()
           
            if value: # Clear existing content
                port_entry.config(state="normal")
                port_entry.delete(0, tk.END)
                port_entry.config(state="readonly")
                return True
            else:
                port_entry.config(state='normal')
                return False
         popup = tk.Toplevel(self.docker_frame)
         popup.title("Create Dockerfile")
         popup.geometry("500x300")
         popup.resizable(False, False)
         
         # Entry widgets for Dockerfile information
         image_entry = tk.Entry(popup, width=20)
         image_entry.grid(row=0, column=1, padx=10, pady=10)
         workdir_entry = tk.Entry(popup, width=20)
         workdir_entry.grid(row=1, column=1, padx=10, pady=10)
         dir_entry = tk.Entry(popup, width=20)
         dir_entry.grid(row=2, column=1, padx=10, pady=10)
         dir_entry.config(state="readonly")
         dependencies_entry = tk.Entry(popup, width=20)
         dependencies_entry.grid(row=3, column=1, padx=10, pady=10)
         port_entry = tk.Entry(popup, width=20)
         port_entry.grid(row=4, column=1, padx=10, pady=10)
         runname_entry = tk.Entry(popup, width=20)
         runname_entry.grid(row=5, column=1, padx=10, pady=10)
         checkbox_dependency_var = tk.BooleanVar()
         checkbox_port_var = tk.BooleanVar()

         checkbox_dependency = tk.Checkbutton(popup, text="Requirments.txt", variable=checkbox_dependency_var,command= lambda: on_dependency_click())
         checkbox_dependency.grid(row=3, column=2, padx=10, pady=10)
         checkbox_port = tk.Checkbutton(popup, text="No port", variable=checkbox_port_var,command= lambda: on_port_click())
         checkbox_port.grid(row=4, column=2, padx=10, pady=10)
         # Labels for Entry widgets
         tk.Label(popup, text="Image Used:").grid(row=0, column=0, padx=10, pady=10)
         tk.Label(popup, text="Work Directory in Docker:").grid(row=1, column=0, padx=10, pady=10)
         tk.Label(popup, text="Directory of File:").grid(row=2, column=0, padx=10, pady=10)
         tk.Label(popup, text="Dependencies:").grid(row=3, column=0, padx=10, pady=10)
         tk.Label(popup, text="Port:").grid(row=4, column=0, padx=10, pady=10)
         tk.Label(popup, text="File Run Name:").grid(row=5, column=0, padx=10, pady=10)
         select_button = tk.Button(popup, text="Select Directory",command=lambda: select_directory(dir_entry))
         select_button.grid(row=2,column=2,padx=10,pady=10)
        



         # Function to handle button click
         def create_dockerfile():
             try:
                 image_used = image_entry.get()
                 work_directory = workdir_entry.get()
                 directory_of_file = dir_entry.get()
                 dependencies = dependencies_entry.get()
                 port = port_entry.get()
                 file_run_name = runname_entry.get()
                 case_number="1"
                 if(on_dependency_click()):
                     case_number="2"
                 if(on_port_click()):
                     case_number="3"
                 if(on_dependency_click() and on_port_click()):
                     case_number= "4"
                

                 docker_instance.imageused = image_used
                 docker_instance.workdirectory = work_directory
                 docker_instance.directoryoffile = directory_of_file
                 docker_instance.dependencies = dependencies
                 
                 docker_instance.port = port
                
                 docker_instance.filerunname = file_run_name
                 
                 result = docker_instance.buildfile(case_number)
                 
                 if result:
                     self.show_output_popup("Build Dockerfile Result", "Dockerfile created successfully.")
                 else:
                     self.show_output_popup("Build Dockerfile Error", "Error creating Dockerfile.")

                 popup.destroy()
             except Exception as e:
                 self.show_output_popup("Build Dockerfile Error", str(e))

         # Button to trigger Dockerfile creation
         create_button = tk.Button(popup, text="Create Dockerfile", command=create_dockerfile, bg=self.button_color)
         create_button.grid(row=6, column=0, columnspan=2, pady=10)

    def show_container_list(self):
         try:
             result = docker_instance.list_containers()
             container_list = result.stdout

             self.show_output_popup("Show All running contianers", container_list)

         except subprocess.CalledProcessError as e:
             self.show_output_popup("List Docker Containers Error", e.stderr)
    def ask_pullimage_name(self):
        # Create a simple dialog to get the image name
        ask_pullimage_name = tk.simpledialog.askstring("Input", "Enter image name")

        # Check if the user clicked Cancel or entered an empty string
        if ask_pullimage_name is not None and ask_pullimage_name.strip() != "":
            result = docker_instance.pull_image(ask_pullimage_name)  # Call pull_image as a method
            self.show_output_popup("Pull an image", result.stdout)
            # Handle the result or update the GUI accordingly

    def ask_image_name(self):
        # Create a simple dialog to get the image name
        image_name = tk.simpledialog.askstring("Input", "Enter image name")

        # Check if the user clicked Cancel or entered an empty string
        if image_name is not None and image_name.strip() != "":
            result = docker_instance.search_image(image_name)
            self.show_output_popup("Search for image", result.stdout)
              # Call search_image as a method
            # Handle the result or update the GUI accordingly

    def ask_container_name(self):
        # Create a simple dialog to get the container name
        container_name = tk.simpledialog.askstring("Input", "Enter container name")

        # Check if the user clicked Cancel or entered an empty string
        if container_name is not None and container_name.strip() != "":
            result = docker_instance.list_containers(container_name)
            # Handle the result or update the GUI accordingly
    def ask_container_name_stop(self):
        # Create a simple dialog to get the container name
        container_name = tk.simpledialog.askstring("Input", "Enter container name")

        # Check if the user clicked Cancel or entered an empty string
        if container_name is not None and container_name.strip() != "":
            self.Stop_container_popup(name=container_name)

            # Handle the result or update the GUI accordingly
    def run_docker_image_with_container_popup(self):
        popup = tk.Toplevel(self.docker_frame)
        popup.title("Run Docker Image with Container")
        popup.geometry("300x150")
        popup.resizable(False, False)

        # Create labels and entry widgets for image name and container name
        img_name_label = tk.Label(popup, text="Image Name:", font=("Helvetica", 12), bg=self.frame_color, fg="white")
        img_name_label.grid(row=0, column=0, padx=10, pady=10)

        img_name_entry = tk.Entry(popup, width=20)
        img_name_entry.grid(row=0, column=1, padx=10, pady=10)

        container_name_label = tk.Label(popup, text="Container Name:", font=("Helvetica", 12), bg=self.frame_color,
                                        fg="white")
        container_name_label.grid(row=1, column=0, padx=10, pady=10)

        container_name_entry = tk.Entry(popup, width=20)
        container_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Function to run Docker image with a container using user input
        def run_image_with_container():
            img_name = img_name_entry.get()
            container_name = container_name_entry.get()

            try:
                result = docker_instance.run_image_with_container(img_name, container_name)
                self.show_output_popup("Run Docker Image with Container Result", result.stdout)

            except subprocess.CalledProcessError as e:
                self.show_output_popup("Run Docker Image with Container Error", e.stderr)

            popup.destroy()

        run_button = tk.Button(popup, text="Run", command=run_image_with_container, bg=self.button_color)
        run_button.grid(row=2, column=0, columnspan=2, pady=10)

    def build_docker_image_popup(self):
        def select_directory(entry):
            directory = filedialog.askdirectory()
            if directory:
                entry.config(state="normal")
                # Do something with the selected directory (e.g., print it)
                text_to_write = directory
                entry.delete(0, tk.END)  # Clear existing content
                entry.insert(0, text_to_write)
                entry.config(state="readonly")
        popup = tk.Toplevel(self.docker_frame)
        popup.title("Build Docker Image")
        popup.geometry("400x150")
        popup.resizable(False, False)

        # Create labels and entry widgets for image name and directory
        name_label = tk.Label(popup, text="Image Name:", font=("Helvetica", 12), bg=self.frame_color, fg="white")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        name_entry = tk.Entry(popup, width=20)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        dir_label = tk.Label(popup, text="Directory:", font=("Helvetica", 12), bg=self.frame_color, fg="white")
        dir_label.grid(row=1, column=0, padx=10, pady=10)

        dir_entry = tk.Entry(popup, width=20)
        dir_entry.grid(row=1, column=1, padx=10, pady=10)
        dir_entry.config(state="readonly")
        select_button = tk.Button(popup, text="Select Directory",command=lambda: select_directory(dir_entry))
        select_button.grid(row=1,column=2,padx=10,pady=10)
       
        def run_image():
            name= name_entry.get()
            
            directory = dir_entry.get()

            try:
                output=""
                result = docker_instance.build_image(name, directory)
                try:
                    
                    self.show_output_popup("build Docker Image w Result", result)
                except:
                    self.show_output_popup("build Docker Image w Result", result.stdout)

            except subprocess.CalledProcessError as e:
                self.show_output_popup("build Docker Image Error", e.stderr)

            popup.destroy()

     
        run_button = tk.Button(popup, text="Run", command=run_image, bg=self.button_color)
        run_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.bootWindow = tk.Toplevel(self.vmWindow)
        self.bootWindow.title("Create Disk Image")
        self.bootWindow.geometry("2340x290")
        self.bootWindow.resizable(False, False)
        self.bootWindow.transient(self.vmWindow)

        self.bootWindow.configure(bg=self.background_color)

        cores_label = tk.Label(self.bootWindow, text="Cores", bg=self.frame_color, fg="white")
        cores_label.pack()

        cores_input = tk.Entry(self.bootWindow, width=10)
        cores_input.pack()

        ram_label = tk.Label(self.bootWindow, text="Ram", bg=self.frame_color, fg="white")
        ram_label.pack()

        ram_input = tk.Entry(self.bootWindow, width=10)
        ram_input.pack()

        def get_disk_directory():
            directory = filedialog.askopenfilename()
            disk_label.configure(text=directory)

        disk_label = tk.Label(self.bootWindow, text="Disk Image", bg=self.frame_color, fg="white")
        disk_label.pack()

        disk_button = tk.Button(self.bootWindow, text="Choose", command=get_disk_directory, bg=self.background_color)
        disk_button.pack()

        def get_iso_directory():
            directory = filedialog.askopenfilename()
            iso_label.configure(text=directory)

        iso_label = tk.Label(self.bootWindow, text="Iso file (leave blank to skip)")
        iso_label.pack()

        iso_button = tk.Button(self.bootWindow, text="Choose", command=get_iso_directory)
        iso_button.pack()

        def create():
            ram = ram_input.get()
            cores = cores_input.get()
            disk_directory = disk_label.cget("text")
            iso_directory = iso_label.cget("text")

            self.vm.boot(ram, cores, disk_directory, iso_directory)

        def cancel():
            self.bootWindow.destroy()

        create_button = tk.Button(self.bootWindow, text="Boot", command=create)
        create_button.pack()

        cancel_button = tk.Button(self.bootWindow, text="Cancel", command=cancel)
        cancel_button.pack()

    def list_images_popup(self):
        try:
            result = docker_instance.list_images()
            self.show_output_popup("List Docker Images Result", result.stdout)

        except subprocess.CalledProcessError as e:
            self.show_output_popup("List Docker Images Error", e.stderr)

    def Stop_container_popup(self,name):
        lists=docker_instance.list_containers().stdout.split()
        found=False
        for i in range(19,len(lists),12):
            if lists[i]==name:
                found=True

        if found:
            try:
                docker_instance.stop_container(name)
                
                self.show_output_popup("Stop container", "Container was stopped succesfully")

            except subprocess.CalledProcessError as e:
                self.show_output_popup("Stop container", "There is no running container with this name")
        else:
            self.show_output_popup("Stop container", "There is no running container with this name")
        
    def show_output_popup(self, title, content):
        output_popup = tk.Toplevel(self.master)
        output_popup.title(title)
        output_popup.geometry("1000x600")
        output_popup.resizable(True, True)

        text_widget = tk.Text(output_popup, wrap='word', height=50, width=130)
        text_widget.insert(tk.END, content)
        text_widget.pack(padx=10, pady=10)

        close_button = tk.Button(output_popup, text="Close", command=output_popup.destroy, bg=self.button_color,
                                 fg="white",
                                 font=("Helvetica", 12))
        close_button.pack(pady=10)

    def create_dockerfile(self):
        save_path = self.save_path_entry.get()
        dockerfile_content = self.dockerfile_entry.get()

        # Implement logic to create Dockerfile based on user input

        # For now, print the parameters
        print(f"Saving Dockerfile to: {save_path}\nDockerfile Content: {dockerfile_content}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x700")  # Set a larger size
    app = VMManagerGUI(root)
    root.mainloop()
