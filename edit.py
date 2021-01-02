import cv2

def edit_movie(input_path, frame_num, ):
    cap = cv2.VideoCapture(input()_path)
    fps = cap.get(CV2.CAP_PROP_FPS)
    rate = fps // frame_num
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME-HEIGHT))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(path_out, fourcc, frame_num, (w, h))

i = 0
    while True:
        ret, frame = cap.movie.read()
        if i % rate == 0:
            video.write(frame)
        if not ret:
            break
        i += 1
    cap.release()
    return