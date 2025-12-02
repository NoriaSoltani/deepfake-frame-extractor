import cv2
import os

def video_to_frames(video_path, output_folder, prefix="frame", size=(224, 224)):
    """
    Extract frames from a video, resize them, and save them to a folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Could not open video: {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_resized = cv2.resize(frame, size)

        frame_file = os.path.join(output_folder, f"{prefix}_{frame_count:05d}.jpg")
        cv2.imwrite(frame_file, frame_resized)
        frame_count += 1

    cap.release()
    print(f"✅ {frame_count} frames saved to {output_folder}")


def extract_frames_single_folder(video_folder, output_root, size=(224, 224)):
    """
    Extract frames from all videos inside ONE folder.
    Each video gets its own subfolder for frames.
    """

    video_extensions = (".mp4", ".avi", ".mov", ".mkv")

    for filename in os.listdir(video_folder):
        if filename.lower().endswith(video_extensions):
            video_path = os.path.join(video_folder, filename)
            video_name = os.path.splitext(filename)[0]

            # Output folder: output_root/video_name/
            output_folder = os.path.join(output_root, video_name)

            print(f"Processing video: {filename}")
            video_to_frames(video_path, output_folder, size=size)




# Replace the paths below with YOUR OWN local paths.
#
# Examples:
#   Mac: /Users/username/Desktop/MyVideos
#   Windows: C:/Users/username/Desktop/MyVideos


# Folder containing your videos:
video_folder = "/full/path/to/your/video_folder"

# Folder where extracted frames will be saved:
output_root = "/full/path/where/frames_will_be_saved"

extract_frames_single_folder(video_folder, output_root, size=(224, 224))
