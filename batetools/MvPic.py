from moviepy.editor import VideoFileClip
import imageio
def extract_frames(video_path, num_frames):
    clip = VideoFileClip(video_path)
    frames = []
    for t in range(num_frames):
        frame = clip.get_frame(t+50 / clip.fps)
        frames.append(frame)
    clip.reader.close()
    imageio.imsave('frame.png', frames[0])
    return frames
from PIL import Image
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    if width > height:
        new_width = size
        new_height = int(size * height / width)
    else:
        new_width = int(size * width / height)
        new_height = size
    resized_image = original_image.resize((new_width, new_height))
    resized_image.save(output_image_path)
    return output_image_path