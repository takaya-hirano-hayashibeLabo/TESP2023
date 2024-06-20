# 1. mediapipe
mediapipeは、パソコンのカメラを使って、骨格モデルを認識するライブラリ  
すでにモデルは提供されているので、新たに何かを準備する必要はない  
顔の動きや、手の関節、体の骨格などが検出できる  

## 環境設定
requirementsか直pipで必要なライブラリをインストールする  
python3.10で動作確認済み  
(※3.6以前はおそらく動かないので、3.7以降にしましょう)

### requirementsを使う場合
~~~
pip install -r 1.mediapipe/requirements.txt
~~~

### 直pipの場合
~~~
pip install  opencv-python==4.10.0.84 mediapipe==0.10.14
~~~


## テストプログラム
`test_mediapipe.py`は一番シンプルなサンプルコード  
このコードでは、カメラを起動させ、mediapipeを通して右肩のxy座標をprintしている  
本番では、座標取得を別の位置にし、余弦定理とか使って関節角度を計算するプログラムを書かせればいい  

以下の`mp_pose.PoseLandmark.RIGHT_SHOULDER`部分を変更すると, 別の関節位置の座標がとれる
~~~python
if pose_results.pose_landmarks != None:
    RShoulder = (
        pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, 
        pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        )
    print(RShoulder)
~~~

また、各関節の名前は以下のリンクに一覧になっているので、適宜調べさせればいい  
- [URL : 手の関節名一覧](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer?hl=ja)
- [URL : 体の関節名一覧](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker?hl=ja)
