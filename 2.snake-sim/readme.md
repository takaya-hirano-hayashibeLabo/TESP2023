# 2. snake sim
mujocoを使ってヘビロボットをシミュレーション上で動かすフェーズ

## ヘビロボットの動かし方

```
data.ctrl[:] = Target_q(t)
```
ここで１２関節分の目標角度を投げる


## ヘビロボットの角度と速度の取得

```
print(data.qpos[:])
print(data.qvel[:])
```
