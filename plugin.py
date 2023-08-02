from nonebot  import on_command
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import ArgPlainText

import json,urllib3

Value = on_command("value", priority=2)

@Value.got("phone", prompt="number?")
async def got_phone(bot: Bot, event: Event, phone: str = ArgPlainText('phone')):
    url = f'https://v.api.aa1.cn/api/api-phone-gj/index.php?phone={phone}'
    
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    try:
        res_data = json.loads(response.data.decode('utf-8'))
        text = res_data.get('money', '未找到相关信息')
    except json.JSONDecodeError:
        text = '解析数据失败'

    await bot.send(event, text)
