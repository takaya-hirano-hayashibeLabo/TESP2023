import mujoco
import numpy as np
from pathlib import Path
import glfw
import os

# モデルとデータのロード
model = mujoco.MjModel.from_xml_path(str(Path(__file__).parent / "src/snake.xml"))
data = mujoco.MjData(model)

# シーンとカメラの初期化
scene = mujoco.MjvScene(model, maxgeom=1000)
camera = mujoco.MjvCamera()

# GLFWの初期化とウィンドウの作成
if not glfw.init():
    print("Could not initialize GLFW")
    exit()

window = glfw.create_window(1200, 900, "Snake Simulation", None, None)
if not window:
    glfw.terminate()
    print("Could not create GLFW window")
    exit()

glfw.make_context_current(window)

# コンテキストの初期化
context = mujoco.MjrContext(model, mujoco.mjtFontScale.mjFONTSCALE_150)



# シミュレーションの実行
timestep_sim=0.005
step=0
while not glfw.window_should_close(window) and data.time < 5.0:
    
    step+=1

    # 各関節の目標角度に基づいて制御信号を設定
    for i in range(1, 13):

        # 目標角度の設定（例として、各関節の目標角度をランダムに設定）
        omega=3
        amplitude=0.3
        t=step*timestep_sim
        target_angle = amplitude*np.sin( omega*t + np.pi/4*i)
        print(target_angle)

        joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, f"Actuator{i}")
        data.qpos[joint_id] = target_angle
        
    
    
    mujoco.mj_step(model, data)

    # シーンの更新
    mujoco.mjv_updateScene(model, data, mujoco.MjvOption(), None, camera, mujoco.mjtCatBit.mjCAT_ALL, scene)

    # ビューポートの定義
    viewport = mujoco.MjrRect(0, 0, 1200, 900)
    mujoco.mjr_render(viewport, scene, context)

    # ウィンドウの更新
    glfw.swap_buffers(window)
    glfw.poll_events()

# GLFWの終了処理
glfw.destroy_window(window)
glfw.terminate()