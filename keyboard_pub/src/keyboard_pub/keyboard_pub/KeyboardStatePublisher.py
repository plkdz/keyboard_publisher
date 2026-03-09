import rclpy
from rclpy.node import Node
from my_msg.msg import KeyboardState  # 确保您的消息包名称正确
import pygame
import sys

class KeyboardStatePublisher(Node):
    def __init__(self):
        super().__init__('keyboard_state_publisher')
        self.publisher_ = self.create_publisher(KeyboardState, 'keyboard_state', 10)
        pygame.init()
        self.screen = pygame.display.set_mode((320, 240))
        pygame.display.set_caption("ROS 2 Keyboard State Publisher")
        self.font = pygame.font.Font(None, 24)
        self.timer_period = 0.05
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.held_keys = {key: False for key in 'abcdefghijklmnopqrstuvwxyz'}


    def timer_callback(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)  # 获取按下的键的名称
                if key in self.held_keys:  # 仅当按下的键在字母范围内时才设置为 True
                    self.held_keys[key] = True
            elif event.type == pygame.KEYUP:
                key = pygame.key.name(event.key)
                if key in self.held_keys:
                    self.held_keys[key] = False

        # 创建并发布 KeyboardState 消息
        msg = KeyboardState()
        for letter in self.held_keys:
            setattr(msg, letter, self.held_keys[letter])
        self.publisher_.publish(msg)
        #self.get_logger().info(f'Publishing keyboard state: {self.held_keys}')

        # 更新 Pygame 显示
        # 创建一个空列表来存储被按下的键
        keys_held_down = []
        for k, v in self.held_keys.items():
            if v:
                keys_held_down.append(k)

        # 将列表转成字符串，并添加到输出文本中
        key_text = "Keys held down: " + ", ".join(keys_held_down)

        self.screen.fill((0, 0, 0))
        text_surface = self.font.render(key_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(160, 120))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardStatePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        pygame.quit()
        print("Shutting down")

if __name__ == '__main__':
    main()
