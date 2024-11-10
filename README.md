
## keyboard_publisher

使用 ROS 2 在 Ubuntu 系统上发布键盘按键事件。

## 先决条件

在安装和运行该项目之前，请确保您的系统已满足以下条件：

- **Ubuntu 22.04**
- **ROS 2 Humble/Rolling** 或其他兼容版本
- **Colcon** 构建工具

## 安装步骤

1. **克隆仓库**

   在工作空间（例如 `~/ros2_ws/src`）中克隆此仓库：

   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/plkdz/keyboard_publisher.git
   ```

2. **安装依赖项**

   使用 `rosdep` 安装项目依赖项：

   ```bash
   cd ..
   rosdep update
   rosdep install --from-paths src --ignore-src -r -y
   ```

3. **编译项目**

   使用 `colcon` 构建工作空间：

   ```bash
   colcon build --packages-select keyboard_publisher
   ```

4. **设置环境**

   编译完成后，使用以下命令加载工作空间的环境：

   ```bash
   source ./install/setup.bash
   ```

## 运行节点

使用以下命令启动 `keyboard_publisher` 节点：

```bash
ros2 run keyboard_pub KeyboardStatePublisher
```

## 使用方法

一旦节点启动，它将自动检测并发布键盘事件。请确保节点已启动并监控相关的 ROS 2 主题，以接收并处理键盘按键事件。

## 许可证

该项目采用 [BSD-2-Clause](LICENSE) 许可证。

确保安装的 ROS 2 版本支持 Ubuntu 22.04，其他步骤与前述版本相同。
