import cv2

# Open the video file
video = cv2.VideoCapture('/home/user/Desktop/Complete_fitness_tracker/Push_up_counter/walking.mp4')

# Get the frames per second (fps) of the video
fps = video.get(cv2.CAP_PROP_FPS)

# Define the output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('slow_motion_video.mp4', fourcc, fps/2, (int(video.get(3)),int(video.get(4))))

# Loop through the frames of the video
while True:
    # Read a frame from the video
    ret, frame = video.read()
    
    # Break the loop if there are no more frames
    if not ret:
        break
    
    # Write the frame to the output video writer twice to slow it down
    output_video.write(frame)
    output_video.write(frame)

# Release the video objects
video.release()
output_video.release()
