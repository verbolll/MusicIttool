import win32gui
import win32console
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
import os
print(os.getcwd())
import warnings
warnings.filterwarnings('ignore')
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import os
from pitch_visualizer import gen_pitch
import time
import librosa
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip
import shutil
import datetime
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QMessageBox, QSystemTrayIcon
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap, QIcon
from Ui_guideFrom import Ui_guideFrom
from Ui_untitled import Ui_MainWindow
from Ui_ToneMakesure import Ui_ToneMakesure
from Ui_tonewarning import Ui_tone
from Ui_themeguide import Ui_themeguide
from toolsUi.Ui_introductionFrom import Ui_introductionFrom
from toolsUi.Ui_From1 import Ui_Form1
from toolsUi.Ui_From2 import Ui_Form2
from toolsUi.Ui_From3 import Ui_Form3
from toolsUi.Ui_From4 import Ui_Form4
from toolsUi.Ui_From5 import Ui_Form5
from toolsUi.Ui_From6 import Ui_Form6
from toolsUi.Ui_From7 import Ui_Form7
from toolsUi.Ui_From8 import Ui_Form8
from toolsUi.Ui_toolsMainGuide import Ui_toolsMainGuide
from toolspy import toolscore
from batetools.Ui_Audioseparation import Ui_audioSPForm
from batetools.Ui_bateToolguide import Ui_bateToolguide
from batetools.Ui_mvForm import Ui_mvForm
from batetools.Ui_openMvFrom import Ui_openmvForm
from batetools import addmv
from batetools import MvPic
from qt_material import apply_stylesheet, QtStyleTools
temp_break = 1
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
tone = ''
savefilename = ''
with open('./pitch_visualizer/introduction.json', 'r', encoding='utf-8') as file:
    introductionText = list(json.load(file).values())
temp_theme_json = {"themekey": 0}
try:
    with open('userset.json', 'r', encoding='utf-8') as usersetting:
        themekey = json.load(usersetting)
        ThemKey = themekey['themekey']
except:
    with open('userset.json', 'w', encoding='utf-8') as usersetting:
        json.dump(temp_theme_json, usersetting)
        ThemKey = 0
class WorkThread(QThread):
    signal = Signal(object)
    def __init__(self, name, loading):
        super().__init__()
        self.name = name
        self.loading = loading
    def run(self):
        from spleeter.separator import Separator
        separator = Separator('spleeter:2stems', multiprocess=False)
        input_audio_file = self.name
        separator.separate_to_file(input_audio_file, './output/')
        try:
            self.loading.clear()
        except:
            pass
        def estimate_key(audio_path):
            y, sr = librosa.load(audio_path)
            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            chroma_mean = np.mean(chroma_stft, axis=1)
            estimated_key = np.argmax(chroma_mean)
            key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            estimated_key_name = key_names[estimated_key]
            return estimated_key_name
        global tone
        tone = estimate_key('./output/' + self.name.split('.')[0] + '/vocals.wav')
class WorkThread0(QThread):
    signal = Signal(object)
    def __init__(self, name, loading, backmusic, openvideobtn, savemovie, filename, makesuretone, newtone):
        super().__init__()
        self.name = name
        self.loading = loading
        self.backmusic = backmusic
        self.openvideobtn = openvideobtn
        self.savemovie = savemovie
        self.filename = filename
        self.makesuretone = makesuretone
        self.newtone = newtone
    def run(self):
        self.workThread1 = WorkThread1(self.loading)
        self.workThread1.start()
        self.workThread1.finished.connect(lambda : self.workThread1.deleteLater())
        gen_pitch.piyvis('./output/' + self.name.split('.')[0] + '/vocals.wav', self.newtone)
        global temp_break
        temp_break = 0
        self.loading.setText('视频合成中')
        video = VideoFileClip("output.mp4")
        audio = AudioFileClip(self.backmusic)
        video = video.set_audio(audio)
        print(audio, video, self.filename)
        video.write_videofile(filename=self.filename, codec="libx264", audio_codec="aac")
        self.loading.setText('已生成音准视频')
        def delete_contents(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
        delete_contents('output')
        os.remove(self.name)
        self.openvideobtn.setEnabled(True)
        self.savemovie.setEnabled(True)
class WorkThread00(QThread):
    signal = Signal(object)
    def __init__(self, name, newtone, openMV):
        super().__init__()
        self.name = name
        self.newtone = newtone
        self.openmv = openMV
    def run(self):
        gen_pitch.piyvis('./output/' + self.name.split('.')[0] + '/vocals.wav', self.newtone)
        addmv.addmv(self.name, 'output.mp4')
        self.openmv.openMVbtn.setEnabled(True)
        self.openmv.saveMVbtn.setEnabled(True)
        self.openmv.MvViewNamelab.setText('分析完成')
        MvPic.extract_frames('my_stack.mp4', 1)
        MvPic.resize_image('frame.png', 'viewpic.png', 500)
        pic = QPixmap('viewpic.png')
        self.openmv.MvViewPiclab.setPixmap(pic)
class WorkThread1(QThread):
    signal = Signal(object)
    def __init__(self, loading):
        super().__init__()
        self.loading = loading
    def run(self):
        time.sleep(1)
        while temp_break:
            try:
                with open('log.log', 'r', encoding='gbk') as file:
                    lines = file.readlines()
                    if lines:
                        print(lines[-1].split('|')[0])
                        if '%' in lines[-1].split('|')[0]:
                            self.loading.setText(lines[-1].split('|')[0])
            except:
                self.loading.setText('请稍后……')
        file.close()
class WorkThreadFrom1(QThread):
    signal = Signal(object)
    def __init__(self, musicname, overpic, savebtn, bigbtn, key):
        super().__init__()
        self.musicname = musicname
        self.overpic = overpic
        self.savebtn = savebtn
        self.bigbtn = bigbtn
        self.key = key
    def run(self):
        global savefilename
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
        savefilename = toolscore.from1(self.musicname, formatted_time, self.key)
        pic = QPixmap(savefilename)
        self.overpic.setPixmap(pic)
        self.savebtn.setEnabled(True)
        self.bigbtn.setEnabled(True)
class WorkThread2(QThread):
    signal = Signal(object)
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        from spleeter.separator import Separator
        separator = Separator('spleeter:5stems', multiprocess=False)
        input_audio_file = self.name
        separator.separate_to_file(input_audio_file, './output/')
class MyWindows(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_music()
        self.click_do_btn()
        self.click_opvideo_btn()
        self.save_movie()
        self.makesuretonewindow = MakeSureToneWindow()
        self.tonewaring = tone_waring()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
        self.__trayicon = QSystemTrayIcon(self)
        self.__trayicon.setIcon(QIcon(':/icon.ico'))
    def choose_music(self):
        self.selectButton.clicked.connect(lambda: self.click_choosebtn())
    def click_choosebtn(self):
        self.song = QFileDialog.getOpenFileName()
        if self.song != ('', ''):
            print(self.song[0].split('/')[-1])
            self.selectsong.setText(self.song[0].split('/')[-1])
            self.loading.clear()
            self.OpenVideoBtn.setEnabled(False)
            self.Savemovie.setEnabled(False)
            global temp_break
            temp_break = 1
            current_directory = os.getcwd()
            destination_file = os.path.join(current_directory, os.path.basename(self.song[0]))
            shutil.copy(self.song[0], destination_file)
    def click_do_btn(self):
        self.doButton.clicked.connect(lambda: self.silence())
    def silence(self):
        def delete_contents(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
        delete_contents('output')
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
        self.filename = "output" + str(formatted_time) + ".mp4"
        self.workThread = WorkThread(self.song[0].split('/')[-1], self.loading)
        self.workThread.start()
        self.workThread.finished.connect(lambda: self.finish_spleeter())
        self.loading.setText('消音中……')
    def finish_spleeter(self):
        self.makesuretonewindow.show()
        self.workThread.deleteLater()
        self.makesuretonewindow.ChooseTone.setCurrentText(tone)
        self.makesuretonewindow.SmartTone.setText('此音乐的调性识别为' + tone)
        self.makesuretonewindow.ToneBtn.clicked.connect(lambda : self.surebtn())
    def surebtn(self):
        if self.makesuretonewindow.ChooseTone.currentText() == tone:
            print('yes, it is True')
            newtone = tone
            self.workThread0 = WorkThread0(self.song[0].split('/')[-1], self.loading, self.song[0], self.OpenVideoBtn,
                                           self.Savemovie, self.filename, self.makesuretonewindow, newtone)
            self.workThread0.start()
            self.workThread0.finished.connect(lambda: self.workThread0.deleteLater())
        elif self.makesuretonewindow.ChooseTone.currentText() != tone:
            self.tonewaring.label.setText('调性将被更改为' + self.makesuretonewindow.ChooseTone.currentText())
            self.tonewaring.label_2.setText('这和识别的调性' + tone + '不符')
            self.tonewaring.label_3.setText('如果您不确定您所选择的' + self.makesuretonewindow.ChooseTone.currentText() +
                                            '是否正确建议维持' + tone)
            self.tonewaring.show()
            self.tonewaring.pushButton.clicked.connect(lambda : self.userTrue())
            self.tonewaring.pushButton_2.clicked.connect(lambda : self.smartTrue())
            print('确当您所提供的调性是正确的吗？调性错误会使生成的音准视频不准确')
        self.makesuretonewindow.deleteLater()
        self.makesuretonewindow = MakeSureToneWindow()
        # self.makesuretonewindow.close()
    def smartTrue(self):
        newtone = tone
        self.tonewaring.close()
        print(newtone)
        self.workThread0 = WorkThread0(self.song[0].split('/')[-1], self.loading, self.song[0], self.OpenVideoBtn,
                                     self.Savemovie, self.filename, self.makesuretonewindow, newtone)
        self.workThread0.start()
        self.workThread0.finished.connect(lambda : self.workThread0.deleteLater())
    def userTrue(self):
        newtone = self.makesuretonewindow.ChooseTone.currentText()
        self.tonewaring.close()
        print(newtone)
        self.workThread0 = WorkThread0(self.song[0].split('/')[-1], self.loading, self.song[0], self.OpenVideoBtn,
                                     self.Savemovie, self.filename, self.makesuretonewindow, newtone)
        self.workThread0.start()
        self.workThread0.finished.connect(lambda : self.workThread0.deleteLater())
    def click_opvideo_btn(self):
        self.OpenVideoBtn.setEnabled(False)
        self.Savemovie.setEnabled(False)
        self.OpenVideoBtn.clicked.connect(lambda: os.popen(self.filename))
    def save_movie(self):
        self.Savemovie.clicked.connect(lambda: self.choose_savepath())
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(self.filename))
        shutil.copy(self.filename, destination_file)
class MakeSureToneWindow(QWidget, Ui_ToneMakesure):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
class tone_waring(QWidget, Ui_tone):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
class introductionWindow(QWidget, Ui_introductionFrom):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
class from1(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda : self.intwindowshow())
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('介绍波形图')
        self.intwdon.label.setText('    ' + introductionText[0])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 1)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from2(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('频谱图（Spectogram）')
        self.intwdon.label.setText('    ' + introductionText[1])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 2)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from3(QWidget, Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('梅尔频率倒谱系数（MFCC）')
        self.intwdon.label.setText('    ' + introductionText[2])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 3)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from4(QWidget, Ui_Form4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('过零率（zero-crossing rate，ZCR）')
        self.intwdon.label.setText('    ' + introductionText[3])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 4)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from5(QWidget, Ui_Form5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('频谱质心（Spectral Centroid）')
        self.intwdon.label.setText('    ' + introductionText[4])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 5)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from6(QWidget, Ui_Form6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('频谱带宽（Spectral Bandwidth）')
        self.intwdon.label.setText('    ' + introductionText[5])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 6)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from7(QWidget, Ui_Form7):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('频谱滚降')
        self.intwdon.label.setText('    ' + introductionText[6])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 7)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class from8(QWidget, Ui_Form8):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def band(self):
        self.choosemusic1btn.clicked.connect(lambda : self.music())
        self.savepicbtn1.clicked.connect(lambda : self.choose_savepath())
        self.bigpic1btn.clicked.connect(lambda : os.popen(savefilename))
        self.intbtn.clicked.connect(lambda: self.intwindowshow())  # 打开介绍界面
    def intwindowshow(self):
        self.intwdon = introductionWindow()
        self.intwdon.setWindowTitle('色度特征（Chroma Feature）')
        self.intwdon.label.setText('    ' + introductionText[7])
        self.intwdon.show()
    def music(self):
        self.musicpath = QFileDialog.getOpenFileName()
        if self.musicpath != ('', ''):
            self.choosedmusic1.setText(self.musicpath[0].split('/')[-1])
            self.workThread1From = WorkThreadFrom1(self.musicpath[0], self.overpic1, self.savepicbtn1, self.bigpic1btn, 8)
            self.workThread1From.start()
            self.workThread1From.finished.connect(lambda : self.workThread1From.deleteLater())
            self.savepicbtn1.setEnabled(False)
            self.bigpic1btn.setEnabled(False)
    def choose_savepath(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        destination_file = os.path.join(path, os.path.basename(savefilename))
        shutil.copy(savefilename, destination_file)
class toolsMainGuide(QWidget, Ui_toolsMainGuide):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.from1 = from1()
        self.toolsbtn1.clicked.connect(lambda : self.from1.show())
        self.from2 = from2()
        self.toolsbtn2.clicked.connect(lambda : self.from2.show())
        self.from3 = from3()
        self.toolsbtn3.clicked.connect(lambda : self.from3.show())
        self.from4 = from4()
        self.toolsbtn4.clicked.connect(lambda : self.from4.show())
        self.from5 = from5()
        self.toolsbtn5.clicked.connect(lambda : self.from5.show())
        self.from6 = from6()
        self.toolsbtn6.clicked.connect(lambda : self.from6.show())
        self.from7 = from7()
        self.toolsbtn7.clicked.connect(lambda : self.from7.show())
        self.from8 = from8()
        self.toolsbtn8.clicked.connect(lambda : self.from8.show())
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
theme_list = ['light_blue.xml', 'light_red.xml', 'light_pink.xml', 'light_purple.xml',
              'dark_blue.xml', 'dark_red.xml', 'dark_pink.xml', 'dark_purple.xml']
class guideThemeWindow(QWidget, Ui_themeguide, QtStyleTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnTheme()
        self.setTheme()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def btnTheme(self):
        apply_stylesheet(self.Lblue_btn, theme=theme_list[0], invert_secondary=True)
        apply_stylesheet(self.Lred_btn, theme=theme_list[1], invert_secondary=True)
        apply_stylesheet(self.Lpink_btn, theme=theme_list[2], invert_secondary=True)
        apply_stylesheet(self.Lpurple_btn, theme=theme_list[3], invert_secondary=True)
        apply_stylesheet(self.Dblue_btn, theme=theme_list[4])
        apply_stylesheet(self.Dred_btn, theme=theme_list[5])
        apply_stylesheet(self.Dpink_btn, theme=theme_list[6])
        apply_stylesheet(self.Dpurple_btn, theme=theme_list[7])
    def setTheme(self):
        self.Lblue_btn.clicked.connect(lambda : self.themeSet_click(0))
        self.Lred_btn.clicked.connect(lambda : self.themeSet_click(1))
        self.Lpink_btn.clicked.connect(lambda : self.themeSet_click(2))
        self.Lpurple_btn.clicked.connect(lambda : self.themeSet_click(3))
        self.Dblue_btn.clicked.connect(lambda : self.themeSet_click(4))
        self.Dred_btn.clicked.connect(lambda : self.themeSet_click(5))
        self.Dpink_btn.clicked.connect(lambda : self.themeSet_click(6))
        self.Dpurple_btn.clicked.connect(lambda : self.themeSet_click(7))
    def themeSet_click(self, key):
        global themekey
        if key < 4:
            self.apply_stylesheet(app, theme_list[key], invert_secondary=True)
        else:
            self.apply_stylesheet(app, theme_list[key])
        themekey = key
        with open('userset.json', 'r', encoding='utf-8') as userSet:
           userData = json.load(userSet)
        userData['themekey'] = key
        with open('userset.json', 'w', encoding='utf-8') as userSet:
            json.dump(userData, userSet)
class audioSeparationWindow(QWidget, Ui_audioSPForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openfile()
        self.openAsaveFinalsong()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def openfile(self):
        self.choosemusicbtn.clicked.connect(lambda : self.getfile())
    def getfile(self):
        self.setmusic = QFileDialog.getOpenFileName()
        print(self.setmusic)
        if self.setmusic != ('', ''):

            def delete_contents(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        os.remove(os.path.join(root, file))
                    for dir in dirs:
                        shutil.rmtree(os.path.join(root, dir))

            delete_contents('output')
            self.musiclocal = self.setmusic[0]
            self.musicname = self.musiclocal.split('/')[-1]
            print(self.setmusic)
            print(self.musiclocal)
            print(self.musicname)
            self.loadinglab.setText(self.musicname + '\n正在处理中，请稍后……')
            self.workThread2 = WorkThread2(self.musiclocal)
            self.workThread2.start()
            self.workThread2.finished.connect(lambda: self.finish_spleeter())
            self.openvolacebtn.setEnabled(False)
            self.openBassbtn.setEnabled(False)
            self.openDrambtn.setEnabled(False)
            self.openPianobtn.setEnabled(False)
            self.savevolacsbtn.setEnabled(False)
            self.saveBassbtn.setEnabled(False)
            self.saveDrambtn.setEnabled(False)
            self.savePianobtn.setEnabled(False)
    def openAsaveFinalsong(self):
        self.openvolacebtn.clicked.connect(lambda : self.clickOpenBtn(0))
        self.openDrambtn.clicked.connect(lambda : self.clickOpenBtn(1))
        self.openBassbtn.clicked.connect(lambda : self.clickOpenBtn(2))
        self.openPianobtn.clicked.connect(lambda : self.clickOpenBtn(3))
        self.savevolacsbtn.clicked.connect(lambda : self.clickSaveBtn(0))
        self.saveDrambtn.clicked.connect(lambda : self.clickSaveBtn(1))
        self.saveBassbtn.clicked.connect(lambda : self.clickSaveBtn(2))
        self.savePianobtn.clicked.connect(lambda : self.clickSaveBtn(3))
    def finish_spleeter(self):
        for i in os.listdir('./output/'+ self.musicname.split('.')[0]):
            os.rename('./output/' + self.musicname.split('.')[0] + '/' + i,
                      './output/' + self.musicname.split('.')[0] + '/' + self.musicname.split('.')[0] + i)
        self.loadinglab.setText(self.musicname + '\n处理完成')
        self.openvolacebtn.setEnabled(True)
        self.openBassbtn.setEnabled(True)
        self.openDrambtn.setEnabled(True)
        self.openPianobtn.setEnabled(True)
        self.savevolacsbtn.setEnabled(True)
        self.saveBassbtn.setEnabled(True)
        self.saveDrambtn.setEnabled(True)
        self.savePianobtn.setEnabled(True)
        self.workThread2.deleteLater()
    def clickOpenBtn(self, key):
        moon_list = ['vocals', 'drums', 'bass', 'piano']
        print('./output/' + self.musicname.split('.')[0] + '/' + self.musicname.split('.')[0] +
                moon_list[key] + '.wav')
        os.popen(self.musicname.split('.')[0] + moon_list[key] + '.wav')
    def clickSaveBtn(self, key):
        savePath = QFileDialog.getExistingDirectory()
        moon_list = ['vocals', 'drums', 'bass', 'piano']
        destination_file = os.path.join(savePath, self.musicname.split('.')[0] + moon_list[key] + '.wav')
        shutil.copy(self.musicname.split('.')[0] + moon_list[key] + '.wav', destination_file)
class openMvWindow(QWidget, Ui_openmvForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
class MvOneWindow(QWidget,Ui_mvForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selMVbtn.clicked.connect(lambda : self.select())
        self.starbtn.clicked.connect(lambda : self.toneMakeSure())
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def select(self):
        self.mv = QFileDialog.getOpenFileName()
        if self.mv != ('', ''):
            print(self.mv[0].split('/')[-1])
            self.MvViewNamelab.setText(self.mv[0].split('/')[-1])
            current_directory = os.getcwd()
            destination_file = os.path.join(current_directory, os.path.basename(self.mv[0]))
            shutil.copy(self.mv[0], destination_file)
            MvPic.extract_frames(self.mv[0].split('/')[-1], 1)
            MvPic.resize_image('frame.png', 'viewpic.png', 500)
            pic = QPixmap('viewpic.png')
            self.MvViewPiclab.setPixmap(pic)
            self.starbtn.setEnabled(True)
    def toneMakeSure(self):
        self.workThread = WorkThread(self.mv[0].split('/')[-1], None)
        self.workThread.start()
        self.workThread.finished.connect(lambda: self.finish_spleeter())
        self.ToneMakesure = MakeSureToneWindow()
        self.starbtn.setText('请稍后……')
        self.starbtn.setEnabled(False)
    def finish_spleeter(self):
        self.workThread.deleteLater()
        self.starbtn.setText('开始分析')
        self.close()
        self.ToneMakesure = MakeSureToneWindow()
        self.ToneMakesure.show()
        self.ToneMakesure.ChooseTone.setCurrentText(tone)
        self.ToneMakesure.SmartTone.setText('此MV的调性识别为' + tone)
        self.ToneMakesure.ToneBtn.clicked.connect(lambda : self.clickToneSurebtn())
    def clickToneSurebtn(self):
        self.ToneMakesure.close()
        self.openmv = openMvWindow()
        if self.ToneMakesure.ChooseTone.currentText() == tone:
            print('True')
            self.newtone = tone
            self.workThread00 = WorkThread00(self.mv[0].split('/')[-1], self.newtone, self.openmv)
            self.workThread00.start()
            self.workThread00.finished.connect(lambda: self.workThread00.deleteLater())
            self.openmv.show()
            self.openmv.MvViewNamelab.setText('分析中……')
            self.openmv.openMVbtn.clicked.connect(lambda: os.popen('my_stack.mp4'))
            self.openmv.saveMVbtn.clicked.connect(lambda: self.saveaddmv())
        else:
            self.tonewaring = tone_waring()
            self.tonewaring.label.setText('调性将被更改为' + self.ToneMakesure.ChooseTone.currentText())
            self.tonewaring.label_2.setText('这和识别的调性' + tone + '不符')
            self.tonewaring.label_3.setText(
                '如果您不确定您所选择的' + self.ToneMakesure.ChooseTone.currentText() +
                '是否正确建议维持' + tone)
            self.tonewaring.show()
            self.tonewaring.pushButton.clicked.connect(lambda: self.userTrue())
            self.tonewaring.pushButton_2.clicked.connect(lambda: self.smartTrue())
            print('确当您所提供的调性是正确的吗？调性错误会使生成的音准视频不准确')
    def saveaddmv(self):
        savePath = QFileDialog.getExistingDirectory()
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
        destination_file = os.path.join(savePath,'my_stack' + formatted_time + '.mp4')
        shutil.copy('my_stack.mp4', destination_file)
    def userTrue(self):
        self.newtone = self.ToneMakesure.ChooseTone.currentText()
        self.tonewaring.close()
        print(self.newtone)
        self.workThread00 = WorkThread00(self.mv[0].split('/')[-1], self.newtone, self.openmv)
        self.workThread00.start()
        self.workThread00.finished.connect(lambda : self.workThread00.deleteLater())
        self.openmv.show()
        self.openmv.MvViewNamelab.setText('分析中……')
        self.openmv.openMVbtn.clicked.connect(lambda: os.popen('my_stack.mp4'))
        self.openmv.saveMVbtn.clicked.connect(lambda: self.saveaddmv())
    def smartTrue(self):
        self.newtone = tone
        self.tonewaring.close()
        print(self.newtone)
        self.workThread00 = WorkThread00(self.mv[0].split('/')[-1], self.newtone, self.openmv)
        self.workThread00.start()
        self.workThread00.finished.connect(lambda: self.workThread00.deleteLater())
        self.openmv.show()
        self.openmv.MvViewNamelab.setText('分析中……')
        self.openmv.openMVbtn.clicked.connect(lambda: os.popen('my_stack.mp4'))
        self.openmv.saveMVbtn.clicked.connect(lambda: self.saveaddmv())
class bateToolguideWindow(QWidget, Ui_bateToolguide):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.audioSeparationWindow = audioSeparationWindow()
        self.pushButton.clicked.connect(lambda : self.audioSeparationWindow.show())
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
        self.MvOneWindow = MvOneWindow()
        self.mvbtn.clicked.connect(lambda : self.MvOneWindow.show())
class guideWindow(QWidget, Ui_guideFrom, QtStyleTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.guidemaintoolbtn = MyWindows()
        self.maintoolbtn.clicked.connect(lambda : self.guidemaintoolbtn.show())
        self.toolsMainGuide = toolsMainGuide()
        self.toolsbtn.clicked.connect(lambda : self.toolsMainGuide.show())
        self.themeMume = guideThemeWindow()
        self.themebtn.clicked.connect(lambda : self.themeMume.show())
        self.helpbtn.clicked.connect(lambda : os.popen('help.pdf'))
        self.batewindow = bateToolguideWindow()
        self.batetoolbtn.clicked.connect(lambda : self.batewindow.show())
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
if __name__ == "__main__":
    app = QApplication([])
    window = guideWindow()
    if ThemKey < 4:
        apply_stylesheet(app, theme_list[ThemKey], invert_secondary=True)
    else:
        apply_stylesheet(app, theme_list[ThemKey])
    window.show()
    app.exec()
    def delete_contents(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
    delete_contents('output')
    current_directory = os.getcwd()
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            try:
                if file.endswith('.mp4'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                if file.endswith('.wav'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                if file.endswith('.m4a'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                if file.endswith('.png'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            except:
                pass