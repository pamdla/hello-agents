
> 声明：本仓库为Datawhale学习小组打卡所用，记录学习进度、问题、心得等。
> 
> 也欢迎star、fork等，谢谢关注。
> 
>> 原始地址：[hello-agents](https://github.com/datawhalechina/hello-agents)
>

---

## 项目结构

将按章节创建目录与代码，以及命名任务，便于查找。

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
│   ├── demo.py
│   ├── demo1.py
├── chapter10
│   ├── .env
│   ├── test.py
│   ├── demo1.py
│   ├── demo2.py
│   ├── demo3.py
├── chapter15
│   ├── .env
│   ├── 15-1.png
│   ├── myAnalysis.png
│   ├── miniAgent.png
│   ├── readme.md
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


### Day5 | 智能体通信协议

<details>
<summary>chapter10</summary>

1. 总结对比三种协议

| 协议名称 | 主要用途 | 适用场景 | 提出者 | 设计哲学 | 职责分层 |
| MCP | 智能体-交互->工具 | 数据库查询、文件系统、API访问 | Anthropic团队 | "上下文共享" | 工具连接层 |
| A2A | 智能体<-协作->智能体 | 多智能体协同任务、长流程交互 | Google 团队 | "对等通信" | 智能体协作层 |
| ANP | 智能体网络发现 | 智能体集群服务发现、负载均衡 | 开源社区维护 | "去中心化服务发现" | 网络发现层 |

2. 之前主要是MCP的认识、开发和使用，但经验甚少。在这门课里面了解了A2A和 ANP协议的设计理念、任务与消息结构后，对于构建多智能体系统有更全面的认识。

3. 认识到单靠MCP无法解决智能体之间的协作与任务分配问题，而A2A、ANP是构建完整agent生态的关键协议。

4. 跑通示例1,2,3并录屏

5. 以前只用MCP的多，目前对于A2A和ANP有了直观和实操，更加相信MCP+A2A+ANP能实现很多业务遇到的问题。期待下一步就是：要将本课程的思想和案例方法应用到工作当中，提高生产力和智能化水平啊。

6. 共勉、共进。

</details>


### Day6 | 综合案例进阶

<details>
<summary>chapter15 - 构建赛博小镇</summary>

1. 选择这个课程（另外两个是：智能旅行助手、自动化深度研究智能体）的动机是想了解如何构建一个数字世界，里面可以有员工，可以有或能够增加其它角色；这个系统是一个具有3个AI的agent系统

2. 演示的时候，需要下载解压*Helloagents-AI-Town*到chapter10目录下

3. 为了加快体验，可以修改`NPC_UPDATE_INTERVAL=10`

3. [代码分析和体会](chapter15/readme.md)

</details>

### Day7 | 毕业设计

<details>
<summary>chapter16 - 毕业设计</summary>
情绪驱动的音乐推荐智能体，用AI感知心情，用音乐温暖心灵。
> 目前它是一个基于 hello-agents 框架构建的情绪音乐推荐智能体。

1. 毕业设计地址：[🧠🎵MindEchoAgent · 心境回响](https://github.com/pamdla/MindEchoAgent.git)
2. 开发过程与体会：
    1. 需要基于hello-agents框架进行定制开发自己的agent。因为不那么熟练，导致有些组件使用和组合不太自然。以及想增加更多能力agent和外部接口，因为没找到合适的音乐搜索接口，甚至想找免费或收费的音乐生成大模型的api等，就暂时没有集成这类接口了。
    2. 为了跑通所有流程，音乐清单使用json记录，本地也没有放置音乐文件，因此页面上没有音乐播放，但留了一个播放位置等。
    3. 整体系统是两个Agents，4个Tools，具备记忆能力，貌似还缺了个MCP调用，后续得补上。
3. 未来期望是将这个与智能家居、穿戴设备，甚至是桌面或移动端做接入，至少可以先根据用户的输入，情绪驱动地改变桌面与交互，升级版可以是智能家居设备的交互等。那么就需要设备API的接入和多厂商的设备类型支持。
4. 保持好奇心，保持关注。
</details>



## 其它资源
1. Makrdown基础：[Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. Datawhale原仓库地址：[hello-agents](https://github.com/datawhalechina/hello-agents)
3. 飞书地址：[Team学习周进度与读书笔记](https://tcn2lptlwqj2.feishu.cn/wiki/MzQDwq7aPimtrXkkfpbc5MW9nMc)
