<div align="center">
    <img src="./image/icon.png" width="256px"/>
</div>
<div align="center">
    富强、民主、文明、和谐、合规
</div>
<div align="center">
    自由、平等、公正、法治、合法
</div>
<div align="center">
    爱国、敬业、诚信、友善、合理
</div>

# ComfyUI_Coze

## 功能简述

一个调用扣子机器人的ComfyUI插件.

## 使用图例

![img.png](image%2Fimg.png)

![img_1.png](image%2Fimg_1.png)

如果想每次生成都不一样，那么请增加随机数

![img_3.png](image%2Fimg_3.png)

## Coze的限额

![img_2.png](image%2Fimg_2.png)

## 使用手册

1. 需要在Coze里创建一个Bot，可以参考BOT：https://www.coze.cn/s/i61kcb1L/；

![img_5.png](image%2Fimg_5.png)

2. 需要创建Token；

在 https://www.coze.cn/open/api 上添加令牌，保存好，以便后续使用。

3. 需要发布Bot，并勾选Bot API；

![img_4.png](image%2Fimg_4.png)

4. 需要获取Bot的ID，保存好，以便后续使用。

![img_6.png](image%2Fimg_6.png)

5. 可以在ComfyUI中使用啦。

## Bot配置举例

![img_9.png](image%2Fimg_9.png)

## 输入举例

1. “给我个有创意的提示词”；
2. “转换为chibi风格的提示词：xxxxxxxx”；
3. “优化下我的提示词：xxxxxxxx”；
4. “精简下我的提示词：xxxxxxxx”；
5. “从下面文章，帮我提炼出提示词：xxxxxxxx”；

### 举例 - 风格转换

> 使用的模型为： https://www.liblib.art/modelinfo/386109978c19484298d810d6f2830780

#### 原始提示词

A hyperrealism abstract photography with a chilling atmosphere. A Chinese teenage girl with braided black hair and wearing a red dress is the role portrait. A misty veil shrouds the scene,making it sinister and morbid. She has a baffled expression as she attempts to unravel a complex web of lies. The proportions are precise,adding to the suspense. The background is a dimly lit forest,enhancing the eerie mood.,

出图：

![img_7.png](image%2Fimg_7.png)

#### 风格转换

转换为chibi风格的提示词：A hyperrealism abstract photography with a chilling atmosphere. A Chinese teenage girl with braided black hair and wearing a red dress is the role portrait. A misty veil shrouds the scene,making it sinister and morbid. She has a baffled expression as she attempts to unravel a complex web of lies. The proportions are precise,adding to the suspense. The background is a dimly lit forest,enhancing the eerie mood.,

出图：

![img_8.png](image%2Fimg_8.png)