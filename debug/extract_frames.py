# -*- coding: utf-8 -*-
'''
@File    : extract_frames.py
@Time    : 2023/11/09 10:52:36
@Author  : wty-yy
@Version : 1.0
@Blog    : https://wty-yy.xyz/
@Desc    : 
This script is used to extract and save the special frame to image file in one video.
'''
from pathlib import Path
import moviepy.editor as mp
import numpy as np
import constant as const

def extract_frames(path_video: Path, target_idxs: dict):
  """
  Extract `target_idxs` frames from the video at `path_video`, 
  save the frames at `const.logs/extract_frames/video_name_extract_frames/`
  ## Input
  - `path_video`: The path of the extracting video.
  - `target_idxs`: The dict with frame index and saved name, such like:

  ```
    target_idxs = {
      180: "start_frame",
      368 * 30 + 16: "show_king_tower_hp",
      405 * 30 + 22: "start_setting_behind_king_tower",
      406 * 30 + 22: "end_setting_behind_king_tower",
    }
  ```
  """
  file_name = path_video.name[:-4]
  path_save = const.path_logs.joinpath("extract_frames/"+file_name)
  path_save.mkdir(parents=True, exist_ok=True)

  clip = mp.VideoFileClip(str(path_video))
  fps, duration = clip.fps, clip.duration
  print("fps=", fps, ", time:", duration)
  total_frames = int(fps * duration)

  max_idx = np.max(np.array(list(target_idxs.keys())))
  if max_idx > fps*duration:
    raise Exception(f"Error: the idx {max_idx} bigger than total frames {total_frames}")

  from tqdm import tqdm
  from PIL import Image
  bar = tqdm(clip.iter_frames(), total=max_idx)
  for i, img in enumerate(bar):
    if i not in target_idxs.keys(): continue
    image = Image.fromarray(img)
    path = str(path_save.joinpath(f"{target_idxs[i]}.jpg"))
    image.save(path)
    bar.set_description(f"Complete saving {i} frame")
    if i == max_idx: break

def videos1():
  path_video = Path("/home/wty/Coding/datasets/CR/fast_pig_2.6/OYASSU_20230917.mp4")
  target_idxs = {
    4 * 30: "start_episode",
    192 * 30: "end_episode",
    180: "start_frame",
    368 * 30 + 16: "show_king_tower_hp",
    405 * 30 + 22: "start_setting_behind_king_tower",
    406 * 30 + 22: "end_setting_behind_king_tower",
  }
  extract_frames(path_video, target_idxs)

def videos2():
  path_video = Path("/home/wty/Coding/datasets/CR/fast_pig_2.6/OYASSU_20230201.mp4")
  target_idxs = {
    7 * 30 + 15: "start_episode",
    291 * 30: "end_episode",
  }
  extract_frames(path_video, target_idxs)

def videos3():
  path_video = Path("/home/wty/Coding/datasets/CR/fast_pig_2.6/OYASSU_20210528.mp4")
  target_idxs = {
    (4*60+23) * 30: "end_episode1",
    (8*60+33) * 30: "end_episode2",
  }
  extract_frames(path_video, target_idxs)

def videos4():
  path_video = Path("/home/wty/Coding/datasets/CR/fast_pig_2.6/OYASSU_20230211.mp4")
  target_idxs = {
    (7*60+42) * 30 + 15: "end_episode1",
    (12*60+9) * 30 + 15: "end_episode2",
  }
  extract_frames(path_video, target_idxs)

if __name__ == '__main__':
  videos4()