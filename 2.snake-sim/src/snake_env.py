import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.spaces import Box

from math import cos, sin, acos, asin, atan, pi
import numpy as np
from gym.envs.registration import register
import os



class SnakeEnv(mujoco_env.MujocoEnv, utils.EzPickle):

    metadata = {
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
        "render_fps": 20,
    }

    def __init__(self,**kwargs):
        utils.EzPickle.__init__(self,**kwargs)
        xml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snake.xml')
        
        obs_space=Box(
            low=-np.pi,high=np.pi,shape=(12,),dtype=np.float64
        )
        mujoco_env.MujocoEnv.__init__(self, xml_path,10,observation_space=obs_space,**kwargs)

    def step(self, a):
        
        self.do_simulation(a,10)
        #self.do_simulation(a, self.frame_skip)
        obs = self._get_obs()
        done = False
        reward = 1
        info = {}
        return obs, reward,done,info,{}

    
    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 0

    
    def reset_model(self):
        qpos = self.init_qpos
        "-------- change here -------------------------------------------------------------------------------------"
        for i in range(12):
            qpos[8+2*i] = 0
        "-----------------------------------------------------------------------------------------------------------"
        self.set_state(qpos,self.init_qvel)
        return self._get_obs()

    def _get_obs(self):
        obs =[]
        for i in range(12):
            obs.append(self.data.qpos[8+2*i])
        #print(self.sim.data.qpos)
        #print("obs",obs)
        return np.concatenate([obs])


register(
id='Snake-v0',
entry_point='snake:SnakeEnv',
max_episode_steps=1000000000,
)