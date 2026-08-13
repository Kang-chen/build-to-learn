"""Static compatibility contract for S3 release preparation."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


skill = read("SKILL.md")
setup = read("references/1-立项.md")
construction = read("references/2-施工.md")
passing = read("references/3-通关.md")
notes = read("references/4-笔记.md")
readme_en = read("README.md")
readme_zh = read("README.zh-CN.md")
evals = read("evals/adaptive-learning-depth.md")
frontmatter = skill.split("---", 2)[1]
assert re.search(r"(?m)^name: build-to-learn$", frontmatter)
assert re.search(r"(?m)^description: >-$", frontmatter), "description must use valid folded YAML"
description_lines = []
collecting_description = False
for line in frontmatter.splitlines():
    if line == "description: >-":
        collecting_description = True
        continue
    if collecting_description:
        if line.startswith("  "):
            description_lines.append(line.strip())
        else:
            break
description = " ".join(description_lines)
assert description.startswith("Use when ")
assert len(description) <= 500, "description should remain trigger-focused"


for term in ["节奏档位和学习目标是两条轴", "Quick", "Standard", "Deep"]:
    assert term in skill, f"SKILL mode contract missing: {term}"

assert "学习目标不等于节奏档位" in setup
assert "深度不能把机械动作重新甩给用户" in construction
assert "风险必验证据不得欠账" in construction
assert "场景题输入包" in passing
assert "深度跟认知增量走" in notes

for banned in [
    "图有疑问吗",
    "动手 → 跑 → 看现象，主语全是用户",
    "要用户跑的命令",
    "用户亲手 build-to-learn",
    "用户认可再开考",
    "用户把现象带回来",
]:
    assert banned not in "\n".join([skill, setup, construction, passing]), f"active instructions retain retired stop: {banned}"

assert "按学习目标选题" in passing
assert "经验连续性" in passing
assert "实际参与过的修改" in passing
assert "题目作废" in passing
assert "能迁移" in passing and "陌生领域" in passing
assert "只要跑通”不是“不想学" in skill
assert "不因“可能存在隐藏边界”预先扩张" in skill
assert "run one focused local check first" in evals
assert "multiple evidence rounds are required" in evals

for term in ["defaults to Quick", "one judgment", "irreplaceable", "unrelated project", "transfer goal"]:
    assert term in readme_en, f"English README missing adaptive behavior: {term}"
for banned in ["those are always yours", "one edge per round", "One small step per turn"]:
    assert banned not in readme_en, f"English README retains retired rule: {banned}"

for term in ["默认从 Quick 开始", "一个判断问题", "不可替代", "无关陌生项目", "能迁移"]:
    assert term in readme_zh, f"Chinese README missing adaptive behavior: {term}"
for banned in ["这些动作永远是你的", "一条边一条边走", "一次只推进一小步"]:
    assert banned not in readme_zh, f"Chinese README retains retired rule: {banned}"

print("S3 compatibility contract passed")
