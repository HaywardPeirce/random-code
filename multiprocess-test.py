from multiprocessing import Process
import subprocess

# encodeTestFileName = "jellyfish-20-mbps-hd-h264.mkv"
encodeTestFileName = "jellyfish-10-mbps-hd-hevc-10bit.mkv"
# encodeTestFileName = "jellyfish-20-mbps-hd-h264.mkv"

# Number of instances you want to run at the same time
processCount = 4

encodeCommand = ["ffmpeg", "-i", encodeTestFileName, "-benchmark", "-threads", "0", "-preset", "superfast", "-s", "1280x720", "-aspect", "16:9", "-b", "4M", "-bt", "4.5M", "-vcodec", "libx264", "-f", "null", "-"] 

def cmd_func():
    
    p = subprocess.Popen(encodeCommand)

    output, errors = p.communicate()

    print(output)

if __name__ == "__main__":  # confirms that the code is under main function
    procs = []
    proc = Process(target=cmd_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for _ in range(processCount - 1):
        proc = Process(target=cmd_func)
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()