from astrbot.core import PluginBase, CommandResult
from utils.meihua import generate_hexagram_by_time, generate_hexagram_by_numbers

class MeiHuaPlugin(PluginBase):
    def __init__(self, context):
        super().__init__(context)

    async def on_command(self, command: str, sender):
        if command == "/meihua":
            args = sender.get_args()
            if len(args) == 0:
                result = generate_hexagram_by_time()
            elif len(args) == 3:
                try:
                    nums = list(map(int, args))
                    result = generate_hexagram_by_numbers(*nums)
                except ValueError:
                    return CommandResult.error("请提供三个有效的整数作为参数。")
            else:
                return CommandResult.error("用法：/meihua 或 /meihua num1 num2 num3")
            return CommandResult.success(result)
        elif command == "/help":
            help_text = (
                "梅花易数插件帮助：\n"
                "- /meihua: 自动起卦。\n"
                "- /meihua num1 num2 num3: 使用三数起卦法起卦。\n"
                "- /help: 查看帮助信息。"
            )
            return CommandResult.success(help_text)
        return CommandResult.not_found()

def register():
    return MeiHuaPlugin