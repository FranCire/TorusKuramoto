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
    
if __name__ == "__main__":
    get_planar_torus_screenshot("videos/oneone_planar.mp4",0,"screenshots/oneone_0")
    get_planar_torus_screenshot("videos/oneone_planar.mp4",111,"screenshots/oneone_11")
    get_planar_torus_screenshot("videos/vertical_planar.mp4",0,"screenshots/vertical_0")
    get_planar_torus_screenshot("videos/vertical_planar.mp4",111,"screenshots/vertical_11")
    get_planar_torus_screenshot("videos/horizontal_planar.mp4",0,"screenshots/horizontal_0")
    get_planar_torus_screenshot("videos/horizontal_planar.mp4",111,"screenshots/horizontal_11")
    get_planar_torus_screenshot("videos/twoone_planar.mp4",0,"screenshots/twoone_0")
    get_planar_torus_screenshot("videos/twoone_planar.mp4",8,"screenshots/twoone_0.7")
    get_planar_torus_screenshot("videos/twoone_planar.mp4",41,"screenshots/twoone_4")
    get_planar_torus_screenshot("videos/twozero_planar.mp4",0,"screenshots/twozero_0")
    get_planar_torus_screenshot("videos/twozero_planar.mp4",141,"screenshots/twozero_14")
    get_planar_torus_screenshot("videos/onethree_planar.mp4",0,"screenshots/onethree_0")
    get_planar_torus_screenshot("videos/onethree_planar.mp4",8,"screenshots/onethree_0.4")
    get_planar_torus_screenshot("videos/onethree_planar.mp4",121,"screenshots/onethree_12")
    get_planar_torus_screenshot("videos/tenzero_planar.mp4",0,"screenshots/tenzero_0")
    get_planar_torus_screenshot("videos/tenzero_planar.mp4",21,"screenshots/tenzero_2")
    get_planar_torus_screenshot("videos/tenzero_planar.mp4",147,"screenshots/tenzero_14.6")
    get_planar_torus_screenshot("videos/fourzero_planar_extended.mp4",0,"screenshots/fourzero_0")
    get_planar_torus_screenshot("videos/fourzero_planar_extended.mp4",17,"screenshots/fourzero_1.6")
    get_planar_torus_screenshot("videos/fourzero_planar_extended.mp4",147,"screenshots/fourzero_14.6")













