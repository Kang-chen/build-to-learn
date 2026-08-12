"""Static contract checks for S2 focused-depth safeguards."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


skill = read("SKILL.md")
construction = read("references/2-施工.md")
passing = read("references/3-通关.md")
notes = read("references/4-笔记.md")

required_skill_terms = [
    "局部放大协议",
    "先存返回锚点",
    "只修最小断点",
    "透明对照预测",
    "三项同时满足才收敛",
    "项目梳理",
]
for term in required_skill_terms:
    assert term in skill, f"SKILL.md missing S2 contract term: {term}"

for term in ["原节奏｜当前判断问题｜原定下一动作｜触发证据", "收敛三证据", "零永久留痕判据"]:
    assert term in construction, f"construction reference missing: {term}"

assert "证据包不是追加考试" in passing
for term in ["判断/原则", "文件或位置", "正反例", "不确定性"]:
    assert term in passing, f"passing evidence packet missing: {term}"

assert "临时放大返回锚点" in notes
assert "三项收敛证据齐全、回到主线后立即清空" in notes
assert "回到主线时删除临时锚点" in notes

# A concrete learner check must test the stage model, not hidden domain recall.
for term in ["场景题输入包", "可由已给证据推出", "参考判断与依据", "不连续换皮重考"]:
    assert term in passing, f"grounded learner check missing: {term}"

# A local zoom must not silently become a whole-project lesson or a permanent stage.
assert "看起来复杂”本身不算触发" in skill
assert "不是新阶段" in skill
assert "不配验收仪式、不编号、不进阶梯" in construction

print("S2 contract checks passed")
