"""Regenerate the routing eval cases under evals/marketing/evals/."""
import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evals")
S = {
    "seo": ("seo-brief", [
        "Write me an SEO brief for a plumbing company's page targeting 'water heater replacement Denver'.",
        "I need a content brief for a blog post about Terraform consulting for small IT shops. Keyword plan and outline please.",
        "Give me a blog outline with a keyword plan for 'EV charger installation cost' for a local electrician's landing page. Target keyword and meta title/description included.",
        "Here is what we already have for our bakery's catering page: H1 'Fresh Catering in Portland', services are breakfast trays, wedding cakes and office lunches. Put together the SEO brief for this page, with the keyword and an outline.",
    ], [
        "Fix the typo in this meta description: 'We offer licnsed plumbing for water heaters and repiping.' Just give me the corrected line.",
        "What is SEO, in two sentences? I keep mixing it up with SEM.",
    ]),
    "comp": ("competitor-research", [
        "Research a competitor to my landscaping business: GreenEdge Lawn Care in the Austin area. What are they offering and what have they done lately?",
        "Who are the closest alternatives to a small-business cloud consultancy like mine? Dig into one of them and tell me how they position themselves.",
        "Can you look into how Bright Spark Electric is positioning against my electrical company over the last 60 days?",
        "Competitor context: Acme Cloud Partners sells fixed-price Terraform migrations, their homepage says 'Infrastructure in 2 weeks', they posted a pricing page last month. Do a competitor research brief on them versus my consultancy.",
    ], [
        "Rewrite this tagline to sound more confident: 'We do electrical work in Columbus.' Keep it short.",
        "In general, what is a SWOT analysis and when is it useful?",
    ]),
    "cal": ("content-calendar", [
        "Plan a month of content for my electrical company: site posts, a newsletter, and social.",
        "I want a week of content ideas for my consulting business. Posts and a newsletter, drafts included.",
        "Put together a content calendar for my HVAC company for next month, mostly seasonal stuff like furnace tune-ups and filter changes.",
        "Facts for my electrical company this month: we're busy with EV charger installs, storm season is starting, and we just finished a big rewire in an old farmhouse. Plan out the next four weeks of content from that.",
    ], [
        "Write one tweet announcing that my consultancy now offers Packer image pipeline reviews. Only the one tweet.",
        "What are good general metrics for judging whether a newsletter is working?",
    ]),
}
GEN = [
    "Write a Python function that parses an ISO 8601 date string and returns a datetime, with type hints.",
    "Explain the difference between a Terraform workspace and a Terraform module.",
    "What does git rebase --onto do? Short answer.",
]


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def case(name, prompt, tags, fire_skill=None):
    d = f"{root}/{name}"
    w(f"{d}/prompt.md", f"---\nname: {name}\ntags: [{', '.join(tags)}]\nruns: 3\nmax_turns: 3\ntimeout_seconds: 120\nallowed_tools: [Skill]\n---\n{prompt}\n")
    if fire_skill:
        w(f"{d}/graders/fires.md", f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{fire_skill}\"'\narm: both\n---\n")
    else:
        w(f"{d}/graders/no-skill.md", "---\ntype: tool_used\ntool: Skill\nmin: 0\nmax: 0\narm: both\n---\n")


for k, (sk, fires, nears) in S.items():
    for i, p in enumerate(fires, 1):
        case(f"{k}-fire-{i}" + ("-easy" if i == 4 else ""), p, [sk, "should-fire"] + (["easy"] if i == 4 else []), sk)
    for i, p in enumerate(nears, 1):
        case(f"{k}-near-{i}", p, [sk, "near-miss"])
for i, p in enumerate(GEN, 1):
    case(f"gen-{i}", p, ["general"])
