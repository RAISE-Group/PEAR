## @package pipeline
#  全链路(Full PEAR)推荐薄封装
#  职责：对外暴露与旧版一致的 run_pipeline 入口（签名不变），内部委托
#  Pipeline.engine.run_recommender 的 'full_pear' 模式执行。逻辑历史见 engine 的
#  _run_full_pear（BFS 演化追踪 + 剪枝 + 路径连乘排序 + 完整 trace）；
#  本模块仅保留兼容接口，不再承载实现。

from typing import Optional

from Pipeline.engine import MODES, run_recommender
from Tool.model import KnowledgeBase, Result, Task
from Tool.tool import SourceProvider


def run_pipeline(task: Task, kb: KnowledgeBase, cache_dir: str = 'CodeCache',
                 provider: Optional[SourceProvider] = None) -> Result:
    """BFS 迭代展开演化链并汇总最终推荐（Full PEAR 全机制，委托统一引擎）。

    输入参数：
        task (Task)：分析任务（Vs/Vt/old_api_fqn/top_k/lib_repo_path）。
        kb (KnowledgeBase)：内存知识库。
        cache_dir (str)：完整定义缓存根目录，默认 'CodeCache'。
        provider (Optional[SourceProvider])：外部传入的 SourceProvider（复用场景）。
            None 时内部创建并关闭。
    返回值：
        Result：status 见模型注释；Full PEAR 保留完整 trace 与候选演化路径。
    异常：
        ValueError：Vs/Vt 不在知识库版本序列中，或 worktree 失败。
    """
    return run_recommender(task, kb, cache_dir=cache_dir, provider=provider,
                           mode=MODES['full_pear'])