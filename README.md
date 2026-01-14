
> 声明：本仓库为Datawhale学习小组打卡所用，记录学习进度、问题、心得等。
> 
> 也欢迎star、fork等，谢谢关注。
> 
>> 原始地址：[hello-agents](https://github.com/datawhalechina/hello-agents)
>

---

## 项目结构
```
dwhelloagents
├── .env
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── requirements.txt
└── tasks
    ├── task0.py
    ├── task01_1.py
    ├── task01_2.py
    ├── task01_3.py
    ├── task01_4.py
```

## 使用方法

### Day0 | 创建本地环境
尽可能的使用docker，隔离宿主机环境，避免不可预料的风险，同时便于独立和管理开发/测试/生产等环境，各不冲突。

<details>
<summary>task0</summary>

```bash
mkdir YOUR-PATH
cd YOUR-PATH
git clone https://github.com/pamdla/hello-agents
docker-compose build
docker-compose up -d
docker exec -it helloagents bash
```

进入容器后，可以操作学习内容，比如：添加文件、执行代码文件等。

示例
```
编辑.env文件，使用你自己的大模型配置
保存完后，在容器内执行下面代码
python task0.py
```
</details>


### Day1 | 智能体经典范式构建

<details>
<summary>task01</summary>

```
1. follow教程步骤，了解每一功能；
2. 完成serpAI注册和api_key填充等；
3. 使用已有代码测试并查看结果，及时调试和修复prompt中的bug；
4. 对比小模型qwen3:2.5b和大模型GLM4.7的差异，大模型会回答冗长，小模型计算逻辑会出错；
5. 另外发现，若采用GLM4.7模型，由于修改了prompt的Finish()或Finish[]形式，代码处理结果会报错（无group，即正则匹配不到结果），暂没有尝试解决;
6. 按进程组建代码和引用
```
</details>

## 其它资源
1. Makrdown基础：[Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. Datawhale原仓库地址：[hello-agents](https://github.com/datawhalechina/hello-agents)
