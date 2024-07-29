import numpy as np
import mujoco
import mujoco.viewer
import os
import time

#>> いじるのはこの関数の部分 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 出力としてヘビの目標関節角度を返すようにする
def Target_q(t):
    omega = 2
    amplitude = 1.0
    target_q = np.array([amplitude * np.sin(omega * t + np.pi / 6 * i) for i in range(12)])
    return target_q
#<< いじるのはこの関数の部分 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



if __name__ == "__main__":
    
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model = mujoco.MjModel.from_xml_path(f"{script_dir}/src/scene.xml")
    data = mujoco.MjData(model)
    
    with mujoco.viewer.launch_passive(model, data) as viewer:

        # setting camera
        viewer.cam.type = 1 # 0:free 1:track 2:fixed
        viewer.cam.trackbodyid = 0
        viewer.cam.distance = 2
                    
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(2)
        
        
        start = time.time()
        
        while viewer.is_running():
            step_start = time.time()
            t = step_start - start
            
            # position control
            data.ctrl[:] = Target_q(t)
            
            # get joint angle
            print("joint angle: ", data.qpos[:])
            # get joint velocity
            print("joint velocity: ", data.qvel[:])
            
            mujoco.mj_step(model, data)
            viewer.sync()
            
            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)