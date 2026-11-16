# claude-skills

A small set of generic [Claude Code](https://code.claude.com) skills for small-business marketing research and planning, with routing eval suites that check each skill fires on the right prompts and stays quiet on the wrong ones.

All three skills are draft-only: they write one local markdown file and never post, send or publish anything.

## Skills

| Skill | What it does |
| --- | --- |
| `seo-brief` | Researches a target query by reading the top results, then writes a brief: recommended keyword and intent, related keywords, an H1/H2 outline, meta title and description, and what competing pages cover or miss. Never invents search volume. |
| `competitor-research` | Researches a competitor from public pages only and writes a cited brief: overview, dated recent moves, positioning, a SWOT table and 3-5 recommendations. Never contacts the competitor. |
| `content-calendar` | Plans a week or month of site posts, newsletters and social posts as a dated list with draft copy and what each item needs from you. Ends with an approval list. |

Each skill asks for your business, and can read a brand voice or positioning notes file if you give it a path.

## Install

Skills are folders containing a `SKILL.md`. Copy or symlink the ones you want into your personal skills directory:

```bash
git clone https://github.com/gmcluckie1/claude-skills.git
mkdir -p ~/.claude/skills
ln -s "$PWD/claude-skills/skills/seo-brief" ~/.claude/skills/seo-brief
ln -s "$PWD/claude-skills/skills/competitor-research" ~/.claude/skills/competitor-research
ln -s "$PWD/claude-skills/skills/content-calendar" ~/.claude/skills/content-calendar
```

Or install into one project only by placing them under `<project>/.claude/skills/`. Restart Claude Code, then ask for example "write an SEO brief for my bakery's catering page".

## Evals

`evals/marketing/` is a plugin-shaped eval suite (`.claude-plugin/`, `evals/`, `skills/`). Its `skills/` entries are relative symlinks back to `skills/`, so it always tests the current skill text. Cases cover prompts that should fire a skill, near misses that should not, and general prompts.

```bash
python3 evals/marketing/gen.py        # regenerate cases
python3 scripts/check.py              # smoke test: frontmatter + cases in sync
claude plugin eval evals/marketing --trust-plugin --no-publish --ablation none --runs 3 --json run.json
```

Running the model-backed eval uses your own Claude Code access and may incur usage.

## Credits and license

MIT, see [LICENSE](LICENSE). The three skills are adapted from [marcosmodly/marketing-skill](https://github.com/marcosmodly/marketing-skill) (MIT); its license is in `third-party-licenses/`.
