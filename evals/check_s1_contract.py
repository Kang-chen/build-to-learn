from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


skill = read("SKILL.md")
planning = read("references/1-立项.md")
building = read("references/2-施工.md")
passing = read("references/3-通关.md")
notes = read("references/4-笔记.md")
active_instructions = "\n".join([skill, planning, building, passing, notes])

required_skill_rules = [
    "自主执行上的学习层",
    "默认 Quick",
    "信息不完整但低风险、可撤销时，不阻断 Quick",
    "Quick 的一轮围绕一个判断问题推进",
    "用户掌判断，AI 扛执行",
]

for rule in required_skill_rules:
    assert rule in skill, f"missing unified routing rule: {rule}"

retired_absolute_rules = [
    "预测 / 改 / 跑 / 看」这几个动作，**主语永远是用户",
    "一条回复里只推进一个动作，给完就交棒等用户",
    "下一个动手的是用户，不是我",
]

retired_absolute_rules.append("手是用户的手 / 一次一步讲完就停")

for rule in retired_absolute_rules:
    assert rule not in active_instructions, f"retired absolute rule still active: {rule}"

reference_contracts = {
    "planning": (planning, "八步仍是思考检查表，不等于八轮对话"),
    "building": (building, "互动单位 = 一个判断问题"),
    "passing": (passing, "Quick 不增加题量"),
    "notes": (notes, "深度跟认知增量走"),
}

for name, (content, marker) in reference_contracts.items():
    assert marker in content, f"{name} reference does not consume the routing contract"

print("S1 contract checks passed: unified Quick routing overrides retired action-sized rules.")
