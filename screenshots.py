import cv2

def get_screenshot(video_name,frame_number,save_name,row_start,row_end,column_start,column_end):
    cap = cv2.VideoCapture(video_name)
    cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number - 1)
    res,frame = cap.read()
    crop_frame = frame[row_start:row_end,column_start:column_end]
    cv2.imshow("Frame",frame)
    cv2.imshow("Crop",crop_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"{save_name}.jpg",crop_frame)

def get_planar_torus_screenshot(video_name,frame_number,save_name):
    get_screenshot(video_name,frame_number,save_name,58,430,140,515)

def get_3d_torus_screenshot(video_name,frame_number,save_name):
    get_screenshot(video_name,frame_number,save_name,120,370,200,460)

    
if __name__ == "__main__":
    get_planar_torus_screenshot("videos/oneone_planar.mp4",0,"screenshots/oneone_planar_0")
    get_planar_torus_screenshot("videos/oneone_planar.mp4",31,"screenshots/oneone_planar_3")
    get_planar_torus_screenshot("videos/oneone_planar.mp4",111,"screenshots/oneone_planar_11")
    get_planar_torus_screenshot("videos/vertical_planar.mp4",0,"screenshots/vertical_planar_0")
    get_planar_torus_screenshot("videos/vertical_planar.mp4",21,"screenshots/vertical_planar_2")

    get_planar_torus_screenshot("videos/vertical_planar.mp4",111,"screenshots/vertical_planar_11")
    get_planar_torus_screenshot("videos/horizontal_planar.mp4",0,"screenshots/horizontal_planar_0")
    get_planar_torus_screenshot("videos/horizontal_planar.mp4",31,"screenshots/horizontal_planar_5")
    get_planar_torus_screenshot("videos/horizontal_planar.mp4",111,"screenshots/horizontal_planar_11")
    get_planar_torus_screenshot("videos/twozero_planar.mp4",0,"screenshots/twozero_planar_0")
    get_planar_torus_screenshot("videos/twozero_planar.mp4",51,"screenshots/twozero_planar_5")
    get_planar_torus_screenshot("videos/twozero_planar.mp4",141,"screenshots/twozero_planar_14")
    get_3d_torus_screenshot("videos/oneone_3d.mp4",0,"screenshots/oneone_3d_0")
    get_3d_torus_screenshot("videos/oneone_3d.mp4",31,"screenshots/oneone_3d_3")
    get_3d_torus_screenshot("videos/oneone_3d.mp4",111,"screenshots/oneone_3d_11")
    get_3d_torus_screenshot("videos/vertical_3d.mp4",0,"screenshots/vertical_3d_0")
    get_3d_torus_screenshot("videos/vertical_3d.mp4",21,"screenshots/vertical_3d_2")

    get_3d_torus_screenshot("videos/vertical_3d.mp4",111,"screenshots/vertical_3d_11")
    get_3d_torus_screenshot("videos/horizontal_3d.mp4",0,"screenshots/horizontal_3d_0")
    get_3d_torus_screenshot("videos/horizontal_3d.mp4",31,"screenshots/horizontal_3d_5")
    get_3d_torus_screenshot("videos/horizontal_3d.mp4",111,"screenshots/horizontal_3d_11")
    get_3d_torus_screenshot("videos/twozero_3d.mp4",0,"screenshots/twozero_3d_0")
    get_3d_torus_screenshot("videos/twozero_3d.mp4",51,"screenshots/twozero_3d_5")

    get_3d_torus_screenshot("videos/twozero_3d.mp4",141,"screenshots/twozero_3d_14")













