import edge_tts  # 导入edge_tts库，用于文本转语音
import asyncio
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip
from PIL import Image


# 调整图片尺寸的函数
def resize_images(image_folder, output_folder, target_size=(1920, 1080)):
    for i in range(1, 14):
        input_path = f"{image_folder}img{i}.png"
        output_path = f"{output_folder}img{i}.png"

        # 打开图片
        img = Image.open(input_path)

        # 调整图片尺寸
        img_resized = img.resize(target_size)

        # 保存调整后的图片
        img_resized.save(output_path)


# 异步生成语音的函数
async def dubbingVoice():
    TEXT = ""
    with open("./2-解说素材/黑天鹅.txt", "rb") as f:
        data = f.read()
        TEXT = data.decode("utf-8")
    # print(TEXT)
    voice = "zh-CN-YunxiNeural"
    output = "./2-解说素材/黑天鹅.mp3"
    rate = "-4%"
    volume = "+0%"
    tts = edge_tts.Communicate(text=TEXT, voice=voice, rate=rate, volume=volume)
    await tts.save(output)


# 生成视频的函数
def videoCreate():
    # 设置文件路径
    image_folder = "./1-图像素材/"  # 13张图片所在文件夹
    background_music_file = "./3-配乐素材/天鹅湖.mp3"
    voiceover_file = "./2-解说素材/黑天鹅.mp3"
    output_file = "./4-生成结果/黑天鹅.mp4"

    # 读取图片序列
    image_files = [f"{image_folder}/img{i}.png" for i in range(1, 14)]

    # 自定义每张图片的显示时长（单位：秒）
    durations = [15, 10, 19, 17, 14, 10, 7, 13, 12, 13, 8, 4, 10]

    clip = ImageSequenceClip(image_files, fps=None, durations=durations)

    # 添加背景音乐
    background_music = AudioFileClip(background_music_file)

    # 如果背景音乐的长度小于视频长度，循环播放直至与视频长度相等
    background_music = background_music.audio_loop(duration=clip.duration)

    # 添加解说配音
    voiceover = AudioFileClip(voiceover_file)

    # 将背景音乐与解说配音混合
    mixed_audio = CompositeAudioClip(
        [background_music.audio_fadein(1).audio_fadeout(1), voiceover]
    )

    # 将图像序列与混合音频合并
    final_clip = clip.set_audio(mixed_audio)

    # 导出视频
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=60)


# 主程序入口
if __name__ == "__main__":
    # 异步生成语音（如果需要，取消注释以下行）
    asyncio.run(dubbingVoice())

    # 调整图片尺寸（如果需要，取消注释以下行）
    image_folder = "./1-图像素材/"  # 13张图片所在文件夹
    output_folder = "./1-图像素材/"  # 调整后的图片保存文件夹
    resize_images(image_folder, output_folder)

    # 生成视频
    videoCreate()
