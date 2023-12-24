import tkinter as tk
from tkinter import filedialog
import qemuClass as qemu

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
        self.vm = qemu.VirtualMachine()

        # Create VM Frame
        self.vm_frame = tk.Frame(master, bg=self.frame_color)
        self.vm_frame.pack(pady=50)

        self.vm_label = tk.Label(self.vm_frame, text="Create Virtual Machine", font=("Helvetica", 20, "bold"), bg=self.frame_color, fg="white")
        self.vm_label.grid(row=0, column=0, columnspan=2, pady=15)

        """
        self.memory_label = tk.Label(self.vm_frame, text="Memory (GB):", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.memory_label.grid(row=1, column=0, pady=10)

        self.memory_entry = tk.Entry(self.vm_frame, font=("Helvetica", 12))
        self.memory_entry.grid(row=1, column=1, pady=10)

        self.disk_label = tk.Label(self.vm_frame, text="Disk (GB):", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.disk_label.grid(row=2, column=0, pady=10)

        self.disk_entry = tk.Entry(self.vm_frame, font=("Helvetica", 12))
        self.disk_entry.grid(row=2, column=1, pady=10)
        """
        
        self.create_vm_button = tk.Button(self.vm_frame, text="Create VM", command=self.create_vm, bg=self.button_color, fg="white", font=("Helvetica", 14))
        self.create_vm_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Create Dockerfile Frame
        self.docker_frame = tk.Frame(master, bg=self.frame_color)
        self.docker_frame.pack(pady=20)

        self.docker_label = tk.Label(self.docker_frame, text="Create Dockerfile", font=("Helvetica", 20, "bold"), bg=self.frame_color, fg="white")
        self.docker_label.grid(row=0, column=0, columnspan=2, pady=15)

        """
        self.save_path_label = tk.Label(self.docker_frame, text="Save Path:", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.save_path_label.grid(row=1, column=0, pady=10)

        self.save_path_entry = tk.Entry(self.docker_frame, font=("Helvetica", 12))
        self.save_path_entry.grid(row=1, column=1, pady=10)

        self.dockerfile_label = tk.Label(self.docker_frame, text="Dockerfile Content:", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.dockerfile_label.grid(row=2, column=0, pady=10)

        self.dockerfile_entry = tk.Entry(self.docker_frame, font=("Helvetica", 12))
        self.dockerfile_entry.grid(row=2, column=1, pady=10
        """

        self.create_dockerfile_button = tk.Button(self.docker_frame, text="Create Dockerfile", command=self.create_dockerfile, bg=self.button_color, fg="white", font=("Helvetica", 14))
        self.create_dockerfile_button.grid(row=3, column=0, columnspan=2, pady=15)

    def create_vm(self):
        self.vmWindow = tk.Toplevel(self.master)
        self.vmWindow.title("Create Virtual Machine")
        self.vmWindow.geometry("300x300")
        self.vmWindow.resizable(False, False)
        self.vmWindow.transient(self.master)
        
        self.vmWindow.configure(bg=self.background_color)


        # Create Disk Frame
        self.disk_fram = tk.Frame(self.vmWindow, bg = self.frame_color)
        self.disk_fram.pack(pady=20)

        self.disk_label = tk.Label(self.disk_fram, text="Create Disk Image", font=("Helvetica", 15, "bold"), bg=self.frame_color, fg="white")
        self.disk_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.create_disk_button = tk.Button(self.disk_fram, text="Create Image", command=self.createDisk, bg=self.button_color, fg="white", font=("Helvetica", 14))
        self.create_disk_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Create Boot Frame
        self.boot_fram = tk.Frame(self.vmWindow, bg = self.frame_color)
        self.boot_fram.pack(pady=30)

        self.boot_label = tk.Label(self.disk_fram, text="Boot Menu", font=("Helvetica", 15, "bold"), bg=self.frame_color, fg="white")
        self.boot_label.grid(row=5, column=0, columnspan=2, pady=15)

        self.create_boot_button = tk.Button(self.disk_fram, text="Boot Menu", command=self.bootVM, bg=self.button_color, fg="white", font=("Helvetica", 14))
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
        self.bootWindow.title("Create Disk Image")
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


    def create_dockerfile(self):
        save_path = self.save_path_entry.get()
        dockerfile_content = self.dockerfile_entry.get()

        # Implement logic to create Dockerfile based on user input

        # For now, print the parameters
        print(f"Saving Dockerfile to: {save_path}\nDockerfile Content: {dockerfile_content}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")  # Set a larger size
    app = VMManagerGUI(root)
    root.mainloop()

