# coding=utf-8
#视频抽帧
# 全局变量
VIDEO_PATH = 'E:\\VideoSource\\test15.mp4' # 视频地址
EXTRACT_FOLDER = 'E:\\CutVedio' # 存放帧图片的位置
EXTRACT_FREQUENCY = 3 # 帧提取频率
def extract_frames(video_path, dst_folder, index):
    # 主操作
    import cv2
    video = cv2.VideoCapture()
    try:
        if not video.open(video_path):
            print("can not open the video")
            exit(1)
        count = 1
        while True:
            _, frame = video.read()
            if frame is None:
                break
            elif count % EXTRACT_FREQUENCY == 0:
                save_path = "{}/{:>1}.jpg".format(dst_folder, index)#{:>03d}
                cv2.imwrite(save_path, frame)
                print(str(index) + "导入中...")
                index += 1
            count += 1
        video.release()
        # 打印出所提取帧的总数
        print("导入成功 {:d} 张".format(index-1))
    except Exception as e:
        print(e)
def main():
    # 递归删除之前存放帧图片的文件夹，并新建一个
    """import shutil
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass"""
    import os
    os.mkdir(EXTRACT_FOLDER)
    # 抽取帧图片，并保存到指定路径
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()





