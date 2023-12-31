import os

class VirtualMachine:
    
    def __init__(self):
        pass

    def CreateImage(self, name, size, location):
        cmd = "qemu-img create -f qcow2 " + location + "/" + name + ".img " + size + "M"
        os.system(cmd)        

    def boot(self, ram, cores, imagefile, isofile):
        # "qemu-system-x86_64 -enable-kvm -cdrom Manjaro.iso -boot menu=on -drive file=Image.img -m 2G -cpu host -vga virtio -display sdl, gl=on"
        # "sudo qemu-system-x86_64 -m 2 -boot d -enable-kvm -smp 4 -net nic -net user -hda Image.img -cdrom Manajaro.iso"
        cmd = "qemu-system-x86_64 " \
                f"-m {ram} " \
                "-boot d " \
                "-enable-kvm " \
                f"-smp {cores} " \
                f"-hda {imagefile} " \
                "-cpu host " \
                "-vga virtio " \
                "-display sdl,gl=on"
        
        if isofile != "Iso file (leave blank to skip)":
            cmd += f" -cdrom {isofile}"

        print(cmd)
        os.system(cmd)