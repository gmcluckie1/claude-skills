---
name: seo-brief
description: Use when asked for an SEO brief, content brief, keyword plan or blog/landing page outline. Writes a local markdown brief; never publishes.
---
# SEO brief

**Drafts only. Never post, send, or publish. The user approves anything external.** Output is one local markdown file; no webhooks, no platform APIs.

## Steps
1. Ask which business or brand and the one page to brief. If they have a brand voice file, ask for its path, read it first and follow it.
2. Search the web for the target query. Read the top pages actually; note what they cover and miss.
3. Never invent search volume or difficulty numbers. Say "no keyword data" if unknown.
4. Write the brief to ./seo-brief-<slug>.md (or the folder the user names) with these sections:
   - Bottom line: recommended keyword, one or two sentences.
   - Keyword and intent: what the searcher wants.
   - Related keywords: table of keyword and likely intent.
   - Outline: H1 and H2s, each tied to an intent.
   - Meta title (60 characters or fewer) and meta description (155 or fewer).
   - Competing pages: what each covers, what it misses.
   - Sources: URLs read, with date.
5. Only use claims the user has supplied or allowed. Flag anything needing their confirmation.

Adapted from marcosmodly/marketing-skill (MIT): https://github.com/marcosmodly/marketing-skill
