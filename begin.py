import subprocess
import sys

def get_input_blender_file_name() -> str:
    return str(sys.argv[sys.argv.index('--') + 1])

def get_output_file_name() -> str:
    return str(sys.argv[sys.argv.index('--') + 2])


def get_output_file_format() -> str:
    return str(sys.argv[sys.argv.index('--') + 3])


def get_resolution_percentage() -> int:
    return int(sys.argv[sys.argv.index('--') + 4])


def get_num_samples() -> int:
    return int(sys.argv[sys.argv.index('--') + 5])

    

result = subprocess.Popen('blender --background {} --log "wm.*" --log-file log.txt --python script.py --render-frame 1 -- {} {} {} {}'.format(get_input_blender_file_name(),get_output_file_name(), get_output_file_format(), get_resolution_percentage(), get_num_samples()), shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output,error = result.communicate()

f = open('log.txt','w')

f.write(output.decode("utf-8"))

print('Rendering is completed successfully')