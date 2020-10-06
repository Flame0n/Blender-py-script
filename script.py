import bpy
import sys


def get_output_file_name() -> str:
    return str(sys.argv[sys.argv.index('--') + 1])


def get_output_file_format() -> str:
    return str(sys.argv[sys.argv.index('--') + 2])


def get_resolution_percentage() -> int:
    return int(sys.argv[sys.argv.index('--') + 3])


def get_num_samples() -> int:
    return int(sys.argv[sys.argv.index('--') + 4])


if __name__ == "__main__":

    # Set scene
    scene = bpy.context.scene

    # Set render
    scene.render.engine = 'RPR'

    # Set threads mode
    scene.render.threads_mode = 'AUTO'

    # Set file format
    scene.render.image_settings.file_format = get_output_file_format()

    # Set render resolution
    scene.render.resolution_percentage = get_resolution_percentage()

    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080

    # Set number of samples
    scene.rpr.limits.max_samples = get_num_samples()

    # Set output file name
    FILE_NAME = get_output_file_name()

    # Set output file path
    scene.render.filepath = '//out\{}_'.format(FILE_NAME)
