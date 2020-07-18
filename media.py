Method 1

方法 1 是最简单的，用 FFmpeg 工具来完成。

具体的网上有很多这方面的资料，本人只是简单了解了一下如何使用。如下图，有一个名为 ffmpeg_test.avi 的视频：

在当前目录打开终端，输入如下命令：

$ffmpeg -i ffmpeg_test.avi frames_%03d.jpg -hide_banner

以上我没有指定太多的参数，实际上有很多参数可以指定，如起止的时间，几秒钟取一帧等等。

输入即可获得每一帧。
Method 2

下面就是可以用 cv2 模块中的 VideoCapture、VideoWriter 来提取了，具体代码如下：

#! encoding: UTF-8

import os

import cv2
import cv

videos_src_path = '/home/ou-lc/chenxp/Downloads/Youtube/youtube_select'
videos_save_path = '/home/ou-lc/chenxp/Downloads/Youtube/youtube_frames'

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('avi'), videos)

for each_video in videos:
    print each_video

    # get the name of each video, and make the directory to save frames
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)               

    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap  = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    while(success):
        success, frame = cap.read()
        print 'Read a new frame: ', success

        params = []
        params.append(cv.CV_IMWRITE_PXM_BINARY)
        params.append(1)
        cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.ppm" % frame_count, frame, params)

        frame_count = frame_count + 1

cap.release()

在最后，我将每一帧保存为 PPM 格式。因为我需要调用之前的 optical flow 论文中的 of 程序，来提取 optical flow image（光流图）。

保存时，根据 opencv 的 Doc：OpenCV 2.4.9 cv2.imwrite，其参数的指定方式如上。一开始在这里跌了好几个跟头，因为不知道如何将参数正确的指定。
