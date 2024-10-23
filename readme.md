运行环境准备
===========

这里使用的Manimgl是1blue3brown作者给自己维护的一个开发版本，文档比较缺失，也没有考虑不同环境下代码库的部署问题，
有很多运行环境问题需要解决。这里记录了MacOS下运行Manimgl的配置。

## MacOS Setup

### 1. Prerequisites

* Install ffmpeg & mactex `brew install ffmpeg mactex`
* Install [uv](https://docs.astral.sh/uv/)

### 2. Install & Setup manim

This setup is using python 3.12

```bash
# setup venv
uv venv
source .venv/bin/activate
uv pip install pip

# install manimlib from source
git clone https://github.com/1b3b/manim.git
cd manim
pip install -e .

# install missing dependencies
uv install setuptools mapbox-earcut

# test drive
manimgl example_scenes.py OpeningManimExample
```

### 3. 处理LaTeX中文字符的问题

* 复制默认配置文件`manim/manimlib/default_config.yml`到项目根目录下，命名为`custom_config.yml`，
* 在`custom_config.yml`中修改`style.tex_template`为`ctex`
* 因为Mac OS中没有tex模版中指定的微软雅黑字体，需要在`manim/manimlib/tex_templates.yml`中搜索`Microsoft Yahei`, 修改为`PingFang SC`

### 4. 交互式运行模式

运行`manimgl`会开启一个IPython终端。

这个环境已经导入了所有的manimlib，并且是在一个Scene的construct函数上下文中，在construct函数中的内容可以直接粘贴到
IPython中执行。

这个终端还提供了一个简便的粘贴代码功能，可以在IPython中输入`checkpoint_paste()`，会自动执行剪贴板复制的代码。
