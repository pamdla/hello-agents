
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
├── chapter4
│   ├── task0.py
│   ├── task01_1.py
│   ├── task01_2.py
│   ├── task01_3.py
│   ├── task01_4.py
├── chapter7
│   ├── .env.example
│   ├── my_llm.py
│   ├── my_main.py
│   ├── my_react_agent.py
│   ├── my_simple_agent.py
│   ├── test_simple_agent.py
├── chapter8
│   ├── .env
│   ├── quick.py
│   ├── test.py
├── chapter9
│   ├── .env
│   ├── quick.py
│   ├── test.py
└── final
```

## 使用方法

### Day0 | 创建本地环境
尽可能的使用docker，隔离宿主机环境，避免不可预料的风险，同时便于独立和管理开发/测试/生产等环境，各不冲突。

<details>
<summary>chapter4(1)</summary>

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
<summary>chapter4(2)</summary>

```
1. follow教程步骤，了解每一功能；
2. 完成serpAI注册和api_key填充等；
3. 使用已有代码测试并查看结果，及时调试和修复prompt中的bug；
4. 对比小模型qwen3:2.5b和大模型GLM4.7的差异，大模型会回答冗长，小模型计算逻辑会出错；
5. 另外发现，若采用GLM4.7模型，由于修改了prompt的Finish()或Finish[]形式，代码处理结果会报错（无group，即正则匹配不到结果），暂没有尝试解决;
6. 按进程组建代码和引用
```
</details>


### Day2 | 构建你的Agent框架

将按章节创建目录与代码，以及命名任务。

<details>
<summary>chapter7</summary>
```
1. follow教程步骤，了解每一功能；
2. 修改.env配置
3. 修改my_main.py使其默认使用本地Ollama为provider
4. 测试my_main.py，出现bug：重复输出字符，待修改
5. 测试test_my_simple_agent.py，复现了bug，同时任务计算正确
6. 本地小模型能力有所欠缺，建议使用更大的模型
```
</details>


### Day3 | 记忆与检索

将按章节创建目录与代码，以及命名任务。

<details>
<summary>chapter8</summary>
```
1. follow教程步骤，了解每一功能；
2. 修改.env的模型或服务配置
3. 修复一些能自主修改的bug，比如账户信息，版本或注入函数等
4. 遗留了问题：'QdrantClient' object has no attribute 'search'，'CollectionInfo' object has no attribute 'vectors_count' --- 解决办法是，降级qdrant-client==1.15.1
5. 体会良久~重新认识了之前使用RAG的效果很差等问题的可能原因
```
</details>


### Day4 | 上下文工程

将按章节创建目录与代码，以及命名任务。

<details>
<summary>chapter9</summary>
```
1. follow教程步骤，了解每一功能；
2. 简单修改.env，重构了目录结构，为qdrant和neo4j等
3. memory_data默认会在每个章节目录自动创建，目前就不该了
4. 跑通示例1和2，补充录屏
5. 目前看，follow代码和调试跑通，问题不大
6. 其它案例读完的感受：目前agent的操作都涉及人为的【精心】设计，我觉得这不是最佳的agent设计。限于初衷是agent的课程教学，原作和源码是很好的。可能有了基本的思想和实现，未来可以达到课程的初衷 -- 设计自己的agent。
7. 每学一节，进步一点~~🆙
```
</details>



## 其它资源
1. Makrdown基础：[Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. Datawhale原仓库地址：[hello-agents](https://github.com/datawhalechina/hello-agents)
