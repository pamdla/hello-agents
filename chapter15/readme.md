
# 项目学习过程拆解

## chapter15 - 构建赛博小镇

1. 本项目主要概念有：

|概念|功能|备注|
|---|---|---|
| NPC | 游戏角色 | 不同的身份（张三，李四，王五）|
|聊天 | 基于大模型生成| |
|记忆 |存储NPC的历史事件 | 前课程chapter8和chapter9里面涉及，需要安装qdrant|
| 好感系统|NPC互动的好感评价等| |
|状态| NPC的对话与其它动作的更新等||


2. 多智能体【agents.py】：每个NCP = 大模型+人设提示词（参考原始代码），有记忆系统且是不同类型的记忆（working、episodic）；其中working类型是记忆当下发生的事情，而episodic是历史印象；这个对后面的好感度系统是必需的

3. 好感度系统【】relationship_manager.py】：不是if-else，而是另一个AI主导的，有相应的提示词：“你是一个情感分析专家,负责分析对话中的情感倾向,判断是否应该改变NPC对玩家的好感度。。。。”。使用大模型（一个情感AI）来分析判断NPC们的对话情感，而不是规则判断。实现了AI管理或分析AI

4. 状态管理【state_manager.py】：NPC们的状态管理器，输出对话与状态等

5. 后端服务【main.py】：由FastAPI创建，启动赛博校长服务端，实现了下面的功能

> "features": ["AI对话", "NPC记忆系统", "好感度系统", "批量状态更新"],
> "endpoints": {
>     "docs": "/docs",
>     "chat": "/chat",
>     "npcs": "/npcs",
>     "npcs_status": "/npcs/status",
>     "npc_memories": "/npcs/{npc_name}/memories",
>     "npc_affinity": "/npcs/{npc_name}/affinity",
>     "all_affinities": "/affinities"

## 画一个架构图

为了帮助理解，原课有一个框架图如下：

![图 15.1 赛博小镇技术架构](15-1.png)

下面是一个从代码分析的角度输出的流程图：

```
flowchart TB
    subgraph Client
        UI[Web / Game Client]
    end

    subgraph API["FastAPI API Layer"]
        Router[API Router]
        Schemas[Pydantic Models]
    end

    subgraph AgentCore["Agent Orchestration"]
        NPCMgr[NPC Agent Manager]
        NPCAgent[NPC Agents]
        AffinityMgr[Relationship Manager]
        MemoryMgr[Memory Manager]
    end

    subgraph World["World / Environment Layer"]
        StateMgr[NPC State Manager]
        BatchGen[Batch Dialogue Generator]
    end

    subgraph Infra["Infra / Observability"]
        Logger[Dialogue Logger]
    end

    subgraph LLM["LLM Layer"]
        LLMCore[HelloAgentsLLM]
        Analyzer[Affinity Analyzer Agent]
    end

    UI --> Router
    Schemas --> Router

    Router --> NPCMgr
    Router --> StateMgr

    NPCMgr --> NPCAgent
    NPCAgent --> MemoryMgr
    NPCMgr --> AffinityMgr

    AffinityMgr --> Analyzer
    Analyzer --> LLMCore
    NPCAgent --> LLMCore

    StateMgr --> BatchGen
    BatchGen --> LLMCore

    NPCMgr --> Logger
    AffinityMgr --> Logger

```

原作的赛博小镇系统（一个精炼的MVP级别虚拟世界）设计覆盖了下面几个要素：

> 💬 对话开始
> 🧠 检索记忆
> 🤖 生成回复
> 📊 分析好感度
> 💾 写入记忆

结合上面两个图，应该能对开发多智能体很有启发和帮助。

## 体会与感受

很多时候大家看各种教学视频或文档，产生的感受是：
> 眼睛会了，手还是抖擞。

但从本次课程看，很多步骤去follow去实践，作为一个小型系统，需要从系统设计思路去理解，动手coding或交给AICoding也是可取的。AI或Agent时代，思想更加重要，代码很便宜，tokens相对便宜，但是对于大型Agent系统，tokens很贵！

换句话说，任何Agent本质上可以归结为：
> 感知 → 记忆 → 决策 → 行动 → 继续/结束 [loop]

比如下面的框架示例一个最小的Agent系统：

```python

class Workplace:
    def __init__(self):
        # 资源设定
        self.resources = {}
        # 初始化
        self.initialized = False

class MiniAgent:
    def perceive(self, env):
        pass

    def decide(self, state):
        pass

    def act(self, action):
        pass

    def step(self, env):
        obs = self.perceive(env)
        action = self.decide(obs)
        self.act(action)

class LLMAgent(MiniAgent):
    def decide(self, obs):
        prompt = f"""
        当前状态: {obs}
        你可以选择:
        - initialize
        - mining_resource
        - building_houses
        """
        return call_llm(prompt)


class Memory:
    def __init__(self):
        self.items = []

    def add(self, event):
        self.items.append(event)

    def retrieve(self, context):
        return relevant_items


class World:
    def tick(self):
        self.time += 1


agents = [agent1, ...]

```

从上面架构设计方式看，Agent系统可以独立于LLM，所以Agent的好坏评价可能与LLM评价高低是独立的。

要给出一个框架图：

```
flowchart LR
    Env[Environment]
    Agent[Agent]
    Memory[Memory]
    Policy[Policy / LLM]
    Tools[Tools]

    Env -->|observation| Agent
    Agent --> Memory
    Memory --> Policy
    Agent --> Policy
    Policy --> Agent
    Agent -->|action| Tools
    Tools --> Env

```

## 总结

从本课看，需要习得的结论应该有：

> 状态有哪些
> 决策是什么
> 时间如何变
> 边界在哪里

下一步行动可能是找一个场景实现一个最小化的Multi-Agent系统。

我会更新的。
