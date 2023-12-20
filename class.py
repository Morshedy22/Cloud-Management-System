import tkinter as tk
from tkinter import filedialog

class VMManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("VM Manager and Dockerfile Generator")

        # Set a color scheme
        background_color = "#162447"  # Dark blue
        frame_color = "#1F4068"  # Teal
        button_color = "#F9A03F"  # Orange

        master.configure(bg=background_color)

        # Create VM Frame
        self.vm_frame = tk.Frame(master, bg=frame_color
        self.vm_frame.pack(pady=20)

        self.vm_label = tk.Label(self.vm_frame, text="Create Virtual Machine", font=("Helvetica", 20, "bold"), bg=frame_color, fg="white")
        self.vm_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.memory_label = tk.Label(self.vm_frame, text="Memory (GB):", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.memory_label.grid(row=1, column=0, pady=10)

        self.memory_entry = tk.Entry(self.vm_frame, font=("Helvetica", 12))
        self.memory_entry.grid(row=1, column=1, pady=10)

        self.disk_label = tk.Label(self.vm_frame, text="Disk (GB):", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.disk_label.grid(row=2, column=0, pady=10)

        self.disk_entry = tk.Entry(self.vm_frame, font=("Helvetica", 12))
        self.disk_entry.grid(row=2, column=1, pady=10)

        self.create_vm_button = tk.Button(self.vm_frame, text="Create VM", command=self.create_vm, bg=button_color, fg="white", font=("Helvetica", 14))
        self.create_vm_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Create Dockerfile Frame
        self.docker_frame = tk.Frame(master, bg=frame_color)
        self.docker_frame.pack(pady=20)

        self.docker_label = tk.Label(self.docker_frame, text="Create Dockerfile", font=("Helvetica", 20, "bold"), bg=frame_color, fg="white")
        self.docker_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.save_path_label = tk.Label(self.docker_frame, text="Save Path:", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.save_path_label.grid(row=1, column=0, pady=10)

        self.save_path_entry = tk.Entry(self.docker_frame, font=("Helvetica", 12))
        self.save_path_entry.grid(row=1, column=1, pady=10)

        self.dockerfile_label = tk.Label(self.docker_frame, text="Dockerfile Content:", font=("Helvetica", 12), bg=frame_color, fg="white")
        self.dockerfile_label.grid(row=2, column=0, pady=10)

        self.dockerfile_entry = tk.Entry(self.docker_frame, font=("Helvetica", 12))
        self.dockerfile_entry.grid(row=2, column=1, pady=10)

        self.create_dockerfile_button = tk.Button(self.docker_frame, text="Create Dockerfile", command=self.create_dockerfile, bg=button_color, fg="white", font=("Helvetica", 14))
        self.create_dockerfile_button.grid(row=3, column=0, columnspan=2, pady=15)

    def create_vm(self):
        memory = self.memory_entry.get()
        disk = self.disk_entry.get()

        # Implement logic to create VM based on memory and disk parameters

        # For now, print the parameters
        print(f"Creating VM with Memory: {memory} GB, Disk: {disk} GB")

    def create_dockerfile(self):
        save_path = self.save_path_entry.get()
        dockerfile_content = self.dockerfile_entry.get()

        # Implement logic to create Dockerfile based on user input

        # For now, print the parameters
        print(f"Saving Dockerfile to: {save_path}\nDockerfile Content: {dockerfile_content}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Set a larger size
    app = VMManagerGUI(root)
    root.mainloop()

