import os
import tempfile
import warnings
from functools import partial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import parselmouth
import tqdm
from pitch_visualizer import magic
FRAME_PER_SEC = 15
TONES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', "A", "A#", "B"]
class Tonality:
    base_diff = [0, 2, 4, 5, 7, 9, 11]
    tone_freq_map = {
        f"{t}{i}": 2 ** (TONES.index(t) / 12 + i) * 16.3516
        for t in TONES for i in range(0, 8)
    }
    def __init__(self, tone):
        assert tone in TONES
        self.tone = tone
        self.scale = [TONES[(TONES.index(self.tone) + diff) % len(TONES)] for diff in self.base_diff]
    @classmethod
    def normalize_to_freq(cls, tone_or_freq):
        if isinstance(tone_or_freq, (float, int)):
            return tone_or_freq
        return cls.tone_freq_map[tone_or_freq]
    def get_tone_and_freq(self, min_freq=0, max_freq=4186):
        min_freq = self.normalize_to_freq(min_freq)
        max_freq = self.normalize_to_freq(max_freq)
        ret = []
        for i in range(0, 8):
            for base_tone in self.scale:
                tone = f"{base_tone}{i}"
                freq = self.tone_freq_map[tone]
                if min_freq <= freq <= max_freq:
                    ret.append((tone, freq))
        ret.sort()
        return ret
def draw_standard(tone, min_freq, max_freq):
    labels = []
    for tone, f in Tonality(tone).get_tone_and_freq(min_freq, max_freq):
        plt.axline((0, f), (1, f), lw=2)
        label = plt.text(1.01, f, tone, ha='left', va='bottom', fontsize=18)
        label.set_visible(False)
        labels.append(label)
    return labels
def animate(frame, pitch, ln, mid_ln, progress_bar, labels):
    m = magic.magic()
    progress_bar.update(1)
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    curr_time = frame / FRAME_PER_SEC
    time_start = curr_time - 2.5
    time_end = curr_time + 2.5
    pitch_in_range = [p for p in zip(pitch.xs(), pitch_values) if time_start <= p[0] <= time_end]
    pitch_xs = [p[0] for p in pitch_in_range]
    pitch_vals = [p[1] for p in pitch_in_range]
    assert 0 not in pitch_vals
    ln.set_data(pitch_xs, pitch_vals)
    mid_ln.set_data([[curr_time, curr_time], [0, 1]])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        avr_pitch = np.nanmean(pitch_vals[len(pitch_vals) // 3: len(pitch_vals) * 2 // 3])
    if not np.isnan(avr_pitch):
        pitch_low, pitch_high = (avr_pitch * (m[2233] ** (-m[41]/m[1823])), avr_pitch * (m[72] ** (m[1795]/m[1823])))
        getattr(plt, "".join(chr(m[i]) for i in [490, 403, 343, 367]))(pitch_low, pitch_high)
        for label in labels:
            _, y = label.get_position()
            if pitch_low <= y <= pitch_high:
                label.set_visible(True)
            else:
                label.set_visible(False)
    for label in labels:
        _, y = label.get_position()
        label.set_position((time_start + 0.01, y))
    getattr(plt, "".join(chr(m[i]) for i in [190, 275, 135, 193]))(time_start, time_end)
def generate_pitch_video(path, output, tone, min_freq, max_freq):
    snd = parselmouth.Sound(path)
    pitch = snd.to_pitch_ac(pitch_floor=min_freq, pitch_ceiling=max_freq)
    plt.rcParams.update({'font.size': 15})
    fig = plt.figure(figsize=(19.2, 10.8), layout="tight")
    labels = draw_standard(tone, min_freq, max_freq)
    ln, = plt.plot([0], [0], '.', markersize=10, color="orange")
    mid_ln = plt.axvline(0, color="red")
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.yscale('log')
    plt.ylabel("fundamental frequency [Hz]")
    render_time = snd.xmax
    print("Generating pitch video")
    with tqdm.tqdm(total=int(render_time * FRAME_PER_SEC), unit="frame", ncols=100,file=open('log.log', 'w')) as progress_bar:
        print(int(render_time * FRAME_PER_SEC))
        ani = animation.FuncAnimation(
            fig,
            partial(animate, pitch=pitch, ln=ln, mid_ln=mid_ln, progress_bar=progress_bar, labels=labels),
            frames=range(int(render_time * FRAME_PER_SEC)))
        FFWriter = animation.FFMpegWriter(fps=FRAME_PER_SEC)
        ani.save('output.mp4', writer=FFWriter)
    plt.xlim(8, 10)
def piyvis(audio, tone):
    magic.magic()
    try:
        min_freq = Tonality.normalize_to_freq("D2")
        max_freq = Tonality.normalize_to_freq("G5")
    except Exception:
        print(f"Invalid min/max pitch {'D2'}/{'G5'}")
        exit(1)
    plt.rcParams['animation.ffmpeg_path'] = "ffmpeg.exe"
    audio = audio
    tone = tone
    with tempfile.TemporaryDirectory() as tmpdir:
        pitch_video_path = os.path.join(tmpdir, "pitch.mp4")
        generate_pitch_video(audio, pitch_video_path, tone, min_freq, max_freq)