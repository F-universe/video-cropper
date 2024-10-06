Video Cropper
This Python script allows you to crop videos by specifying a rectangular area using coordinates. The script leverages the moviepy library to handle video processing. After setting the desired coordinates, the script automatically crops all videos in a specified directory to the defined area.

Features
Crop videos based on specified coordinates.
Processes all videos in a given folder.
Supports multiple video formats (e.g., .mp4, .avi, .mkv).
Saves cropped videos with a new name, keeping the original file intact.
Requirements
Python 3.x
moviepy library (for video processing)
To install moviepy, use the following command:

bash
Copia codice
pip install moviepy
How it Works
Set the Coordinates: You define the top-left and bottom-right coordinates of the area you want to crop. The script calculates the width and height of the cropping area based on these coordinates.

Video Processing: Using moviepy, the script opens each video file from the specified directory and crops the video using the defined area.

Automatic Batch Cropping: The script will automatically process every video in the input directory, cropping them according to the given coordinates. Cropped videos will be saved with a new filename (cropped_<original_filename>.mp4).

Usage
Clone or download this repository.
Ensure you have all dependencies installed (Python and moviepy).
Open the inst.py script and modify the following section to specify the coordinates for the cropping area:
python
Copia codice
# Define the coordinates of the cropping area
x1, y1 = 127, 275  # Top-left corner
x2, y2 = 414, 809  # Bottom-right corner
Set the directory containing the videos you want to crop:
python
Copia codice
video_directory = r"C:\Users\fabio\OneDrive\Desktop\F-universe\instagram(1)\videos"
Run the script:
bash
Copia codice
python inst.py
The script will process each video in the specified folder, cropping them based on the defined coordinates, and saving the cropped videos with the prefix cropped_.

Example
If you set the cropping area like this:

Top-left corner: (127, 275)
Bottom-right corner: (414, 809)
The script will crop a rectangle of that size from each video and save the result as a new video.

Notes
Ensure that the input videos are compatible with the moviepy library.
If you encounter issues with the video codecs, you may need to modify the output codec in the script. By default, the script uses libx264 for video encoding and aac for audio encoding.
python
Copia codice
cropped_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
License
This project is licensed under the MIT License.

