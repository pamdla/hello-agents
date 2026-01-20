# quick.py
from hello_agents import SimpleAgent, HelloAgentsLLM, ToolRegistry
from hello_agents.tools import MemoryTool
from typing import List, Any

# 创建具有记忆能力的Agent
llm = HelloAgentsLLM()
agent = SimpleAgent(name="记忆助手", llm=llm)

# 创建记忆工具
# memory_tool = MemoryTool(user_id="neo4j")

# 注入search
class MyMemoryTool(MemoryTool):
    def _search_memory(
        self,
        query: str,
        limit: int = 5,
        memory_types: List[str] = None,
        memory_type: str = None,
        min_importance: float = 0.1
    ) -> str:
        """搜索记忆"""
        try:
            # 参数标准化处理
            if memory_type and not memory_types:
                memory_types = [memory_type]

            results = self.memory_manager.retrieve_memories(
                query=query,
                limit=limit,
                memory_types=memory_types,
                min_importance=min_importance
            )

            if not results:
                return f"🔍 未找到与 '{query}' 相关的记忆"

            # 格式化结果
            formatted_results = []
            formatted_results.append(f"🔍 找到 {len(results)} 条相关记忆:")

            for i, memory in enumerate(results, 1):
                memory_type_label = {
                    "working": "工作记忆",
                    "episodic": "情景记忆",
                    "semantic": "语义记忆",
                    "perceptual": "感知记忆"
                }.get(memory.memory_type, memory.memory_type)

                content_preview = memory.content[:80] + "..." if len(memory.content) > 80 else memory.content
                formatted_results.append(
                    f"{i}. [{memory_type_label}] {content_preview} (重要性: {memory.importance:.2f})"
                )

            return "\n".join(formatted_results)

        except Exception as e:
            return f"❌ 搜索记忆失败: {str(e)}"
    #
    def _forget(self, strategy: str = "importance_based", threshold: float = 0.1, max_age_days: int = 30) -> str:
        """遗忘记忆（支持多种策略）"""
        try:
            count = self.memory_manager.forget_memories(
                strategy=strategy,
                threshold=threshold,
                max_age_days=max_age_days
            )
            return f"🧹 已遗忘 {count} 条记忆（策略: {strategy}）"
        except Exception as e:
            return f"❌ 遗忘记忆失败: {str(e)}"
    #
    def _consolidate(self, from_type: str = "working", to_type: str = "episodic", importance_threshold: float = 0.7) -> str:
        """整合记忆（将重要的短期记忆提升为长期记忆）"""
        try:
            count = self.memory_manager.consolidate_memories(
                from_type=from_type,
                to_type=to_type,
                importance_threshold=importance_threshold,
            )
            return f"🔄 已整合 {count} 条记忆为长期记忆（{from_type} → {to_type}，阈值={importance_threshold}）"
        except Exception as e:
            return f"❌ 整合记忆失败: {str(e)}"


memory_tool = MemoryTool(user_id="neo4j")

#
tool_registry = ToolRegistry()
tool_registry.register_tool(memory_tool)
agent.tool_registry = tool_registry
 
# 体验记忆功能
print("=== 添加多个记忆 ===")

# 添加第一个记忆
result1 = memory_tool.execute("add", content="用户张三是一名Python开发者，专注于机器学习和数据分析", memory_type="semantic", importance=0.8)
print(f"记忆1: {result1}")

# 添加第二个记忆
result2 = memory_tool.execute("add", content="李四是前端工程师，擅长React和Vue.js开发", memory_type="semantic", importance=0.7)
print(f"记忆2: {result2}")

# 添加第三个记忆
result3 = memory_tool.execute("add", content="王五是产品经理，负责用户体验设计和需求分析", memory_type="semantic", importance=0.6)
print(f"记忆3: {result3}")

print("\n=== 搜索特定记忆 ===")
# 搜索前端相关的记忆
print("🔍 搜索 '前端工程师':")
result = memory_tool.execute("search", query="前端工程师", limit=3)
print(result)

print("\n=== 记忆摘要 ===")
result = memory_tool.execute("summary")
print(result)
