import tensorflow as tf

# 设置提示信息的等级 menu['1','2','3'] 默认'1'显示所有信息,'2'只显示 warning 和 Error,'3'只显示 Error
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 创建变量，初始化为0
state = tf.Variable(0, name="counter")

# 创建一个 op , 其作用是时 state 增加 1
one = tf.constant(1) # 直接用 1 也就行了
update = tf.assign(state, state+1)
# new_value = tf.add(state, 1)
# update = tf.assign(state, new_value)


# 启动图之后， 运行 update op
with tf.Session() as sess:
    # 创建好图之后，变量必须经过‘初始化’ 
    sess.run(tf.global_variables_initializer())
    # 查看state的初始化值
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)  # 这样子每一次运行state 都还是1
        print(sess.run(state))