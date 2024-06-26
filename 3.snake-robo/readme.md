# 3. snake-robo
ヘビの実機を動かすコード  

ここでのゴールは、PCからラズパイに制御信号を送れるようになること  

## ヘビの準備
まずは、ヘビに搭載されたラズパイの中のコードを起動する  
このコードを起動すると、socket通信（UDP）で角度を受取り、その目標角度に各モータを制御するプログラムが走る

### ヘビにSSH
ヘビと制御信号を送信するPCのを同じネットワークに繋いでSHHする  
ここでは、林部研のWifiに繋いだ場合を例にあげる（ルータがあればそれでもいい）  

1. ヘビにSSH  
パスワードは`hayashibelab`    
※IPは固定してあるが、研究室のルータが変わったときは適宜IPを変更して(特にホストアドレスが変わった時に注意)  
    ~~~
    ssh pi@10.240.77.116
    ~~~
    ~~~
    hayashibelab #password
    ~~~~

**これ以降はラズパイ側で行う**
1. 仮想環境をactivate
    ~~~
    source hirano-dev/envs/snake-robot-env/bin/activate
    ~~~

2. 実行ディレクトリに移動
   ~~~
    cd hirano-dev/projects/snake-robot-project/
   ~~~

3. 信号受信&制御プログラムの実行
    ~~~
    python app/snake_control_by_signal.py
    ~~~

この一連の流れで、ヘビロボット側でやることは終了


## 制御信号送信側プログラム
こんどは、PCから制御信号を送信するプログラムを実行する  
**これ以降は制御用PC側で行う**

### ライブラリのインストール
キーボード入力読み取り用のライブラリをインストール
~~~
pip install keyboard
~~~

### 実行
キーボードの`a`or`d`を押すと、先頭のサーボの角度が変化する
~~~
python 3.snake-robo/test_control_snake.py
~~~

### プログラムについて
#### 蛇側ラズパイのポート&IP設定
ここの設定は基本変えなくていい  
ただ、研究室のホストアドレスが変わったときは、ラズパイの中身を開けてIPを設定し直す必要がある  
（とりあえず平野に言えばできるが...）
~~~python
PORT=5000
CLIENT="10.240.77.116" #snake robot IP address
~~~

### ラズパイに送る制御信号
ラズパイ側に送る信号は、文字列のカンマ区切りになっている  
また、それぞれの数字がそれぞれのサーボの角度 [radian]に対応する  
ここで、**サーボはpi/4 radianくらいまでしか受け付けない**ので注意  
それ以上の角度を送信しても最大値でクリッピングされてしまう 
~~~python
msg="0,0,0,0,0,0,0,0,0,0,0,0" #それぞれの要素がサーボの角度 [radian]に対応
~~~