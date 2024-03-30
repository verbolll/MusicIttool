from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
def addmv(inputmv, outmv):
    clip1 = VideoFileClip(inputmv)
    clip2 = VideoFileClip(outmv)
    scale = clip1.size[0]*0.3/clip2.size[0]
    clip3 = clip2.resize(scale)
    video = CompositeVideoClip([clip1,
                                clip3.set_pos((0,0)),
                               ])
    video.write_videofile("my_stack.mp4")