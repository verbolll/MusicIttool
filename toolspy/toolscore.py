import librosa.display
import matplotlib.pyplot as plt
import matplotlib
from sklearn import preprocessing
import sklearn
from PIL import Image
matplotlib.rcParams['font.family']= 'SimHei'
matplotlib.rcParams['axes.unicode_minus']=False
def from1(audio_path, formatted_time, key):
    print(audio_path)
    plt.close()
    x, sr = librosa.load(audio_path)
    spectral_centroids = librosa.feature.spectral_centroid(y=x, sr=sr)[0]
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)
    def normalize(x, axis=0):
        return sklearn.preprocessing.minmax_scale(x, axis=axis)
    if key == 1:
        librosa.display.waveshow(x, sr=sr, color='b')
        plt.title(audio_path.split('/')[-1] + '波形图')
        name = audio_path.split('/')[-1] + '波形图' + formatted_time + '.png'
    elif key == 2:
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
        name = audio_path.split('/')[-1] + '频谱图' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '频谱图')
        plt.colorbar()
    elif key == 3:
        mfccs = librosa.feature.mfcc(y=x, sr=sr)
        librosa.display.specshow(mfccs, sr=sr, x_axis='time')
        name = audio_path.split('/')[-1] + '梅尔频率倒谱系数' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '梅尔频率倒谱系数')
    elif key == 4:
        zcrs = librosa.feature.zero_crossing_rate(x)
        name = audio_path.split('/')[-1] + '过零率（ZCR）' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '过零率（ZCR）')
        plt.plot(zcrs[0])
    elif key == 5:
        plt.plot(t, normalize(spectral_centroids), color='r')
        name = audio_path.split('/')[-1] + '频谱质心（Spectral Centroid）' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '频谱质心（Spectral Centroid）')
    elif key == 6:
        spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(y=x+0.01, sr=sr, p=2)[0]
        plt.plot(t, normalize(spectral_bandwidth_3), color='g')
        name = audio_path.split('/')[-1] + '频谱带宽（Spectral Bandwidth）' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '频谱带宽（Spectral Bandwidth）')
    elif key == 7:
        spectral_rolloff = librosa.feature.spectral_rolloff(y=x + 0.01, sr=sr)[0]
        plt.plot(t, normalize(spectral_rolloff), color='r')
        name = audio_path.split('/')[-1] + '频谱滚降' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '频谱滚降')
    elif key == 8:
        chromagram = librosa.feature.chroma_stft(y=x, sr=sr, hop_length=512)
        librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=512, cmap='coolwarm')
        name = audio_path.split('/')[-1] + '色度特征（Chroma Feature）' + formatted_time + '.png'
        plt.title(audio_path.split('/')[-1] + '色度特征（Chroma Feature）')
    def resize_image(input_image_path, output_image_path, new_width):
        image = Image.open(input_image_path)
        width_percent = (new_width / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_image_path)
    plt.savefig(name)
    resize_image(name, name, 640)
    plt.close()
    return name