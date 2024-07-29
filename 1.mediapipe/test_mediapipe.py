import cv2
import mediapipe as mp


def main():

    ## initialize pose estimator ###################################################
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)
    ###############################################################################

    
    while cap.isOpened():
        try:
            ## mediapipe #######################################################################################
            _, frame = cap.read() # read frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert to RGB
            pose_results = pose.process(frame_rgb) # process the frame for pose detection
            mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS) # draw skeleton on the frame
            frame = cv2.flip(frame, 1) # Flip horizontal
            ####################################################################################################

            ## openCV #####################################################################################
            #text
            cv2.putText(frame,"enter text here",(10,60), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,0),3,cv2.LINE_AA)
            
            # display the frame
            cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Output', 900, 500)
            cv2.imshow('Output', frame)
            ###############################################################################################
            


            #>> ここで関節の位置を取得できる. 実際は, ここの部分を書き換えてもらう>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            # 現在は, 右肩のxy座標を取得してprintしている (mp_pose.PoseLandmark.RIGHT_SHOULDERで位置を指定している)
            #以下リンクに各関節の名前が一覧になっている
            #手：https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer?hl=ja
            #体：https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker?hl=ja
            "------ change here -------------------------------------------------------------------------------------"
            if pose_results.pose_landmarks != None:
                RShoulder = (
                    pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, 
                    pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
                    )
                print(RShoulder)

            else:
                RShoulder = ("None","None")
            "--------------------------------------------------------------------------------------------------------"
            #<< ここで関節の位置を取得できる. 実際は, ここの部分を書き換えてもらう<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#



        except:
            break
            
        if cv2.waitKey(1) == 27: #press esc to close
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()