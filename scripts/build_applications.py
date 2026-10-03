#!/usr/bin/env python3
"""Build public adoption findings from data/application_usages.json.

python scripts/build_applications.py [--check]
No private inputs are required. The snapshot is curated, not inferred from titles.
"""
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT/'data/application_usages.json'

def load_audit():
 data=json.loads(DATA.read_text(encoding='utf-8'))
 rows=data['records']; coverage=data['coverage']
 assert len(rows)==coverage['method_paper_records']
 assert len({r['audit_id'] for r in rows})==len(rows)
 assert len({r['paper_key'] for r in rows})==coverage['paper_identities']
 assert len({r['method_id'] for r in rows})==coverage['method_records']
 assert len({r['family'] for r in rows})==coverage['method_groups']
 for r in rows:
  assert r['generation_mode'] in {'online','prepared','unknown'}
  assert r['source_url'].startswith(('https://','http://'))
  if r['counts_as_functional_generator_adoption']:
   assert r['category']=='functional_interactive' and r['technical_reuse_supported']
   assert r['method_role'] in {'generator_or_planner','adapted_generator'}
 return data

def summarize(data):
 rows=data['records']
 groups=[]
 for name in sorted({r['family'] for r in rows}):
  rs=[r for r in rows if r['family']==name]
  def count(pred): return len({r['paper_key'] for r in rs if pred(r)})
  years=sorted({r['method_year'] for r in rs if r['method_year']})
  groups.append({'family':name,'years':str(years[0]) if len(years)==1 else f'{years[0]}–{years[-1]}','functional':count(lambda r:r['counts_as_functional_generator_adoption']),'online':count(lambda r:r['counts_as_functional_generator_adoption'] and r['generation_mode']=='online'),'prepared':count(lambda r:r['counts_as_functional_generator_adoption'] and r['generation_mode']=='prepared'),'timing_unknown':count(lambda r:r['counts_as_functional_generator_adoption'] and r['generation_mode']=='unknown'),'author_online':count(lambda r:r['counts_as_functional_generator_adoption'] and r['generation_mode']=='online' and r['generation_evidence']=='author clarification'),'other_applications':count(lambda r:r['category'] in {'offline','live_content_application','presentation_application'} and r['technical_reuse_supported'] and r['method_role'] in {'generator_or_planner','adapted_generator'}),'comparison':count(lambda r:r['category']=='interactive_comparison' and r['technical_reuse_supported'] and r['method_role'] in {'generator_or_planner','adapted_generator'}),'candidates':count(lambda r:r['category']=='functional_candidate' and r['technical_reuse_supported'] and r['method_role']=='generator_or_planner'),'platform':count(lambda r:r['category']=='platform' and r['technical_reuse_supported'] and r['method_role']=='generator_or_planner'),'components':count(lambda r:r['method_role'] not in {'generator_or_planner','adapted_generator'}),'unresolved':count(lambda r:r['category']=='unresolved' or not r['technical_reuse_supported'])})
 groups.sort(key=lambda g:(-g['functional'],-g['candidates'],g['family']))
 matched=[r for r in rows if r['counts_as_functional_generator_adoption']]
 stats={'methods':len({r['method_id'] for r in matched}),'groups':len({r['family'] for r in matched}),'papers':len({r['paper_key'] for r in matched}),'online':len({r['paper_key'] for r in matched if r['generation_mode']=='online'}),'author_online':len({r['paper_key'] for r in matched if r['generation_mode']=='online' and r['generation_evidence']=='author clarification'})}
 applications=[r for r in rows if r['counts_as_functional_generator_adoption'] or (r['category'] in {'offline','live_content_application','presentation_application'} and r['technical_reuse_supported'] and r['method_role'] in {'generator_or_planner','adapted_generator'})]
 stats.update(application_methods=len({r['method_id'] for r in applications}),application_groups=len({r['family'] for r in applications}),application_papers=len({r['paper_key'] for r in applications}))
 repeated={}
 for r in rows:
  if r['counts_as_functional_generator_adoption'] or (r['category'] in {'offline','live_content_application','presentation_application','interactive_comparison'} and r['technical_reuse_supported'] and r['method_role'] in {'generator_or_planner','adapted_generator'}):
   repeated.setdefault(r['method_id'],set()).add(r['paper_key'])
 mids={mid for mid,papers in repeated.items() if len(papers)>=2}
 stats.update(repeated_methods=len(mids),repeated_groups=len({r['family'] for r in rows if r['method_id'] in mids}),repeated_method_ids=sorted(mids))
 return groups,stats

def readme_summary(data=None, citation_prefix='', generation_papers=None):
 data=data or load_audit(); groups,s=summarize(data)
 if generation_papers is None:
  catalogue=json.loads((ROOT/'docs/data.json').read_text(encoding='utf-8'))['papers']
  generation_papers=sum(p['category']!='theory' and p['type']!='thesis' for p in catalogue)
 lines=[f"Across the atlas’s **{generation_papers} gesture-generation papers**, our audit identifies only **{s['repeated_methods']} method papers across {s['repeated_groups']} groups** with repeated reuse in applications and related studies, including **museum guides, healthcare counselors and conversational robots**. The strongest documented interactive reuse remains concentrated in older **BEAT/REA** pipelines, showing why application uptake matters alongside the number of new methods published. [Where and how are they used? →](APPLICATIONS.md#method-group-counts)",'', '| Method group / papers with ≥2 uses | Method years | Functional interactive papers | Adjacent usage papers¹ |','|---|---|---:|---:|']
 short={'Cassell / Vilhjalmsson / Bickmore: BEAT and REA':'BEAT / REA','Marsella / USC ICT: NVBG, Cerebella and learned gestures':'NVBG / Cerebella / USC ICT','Meena / WikiTalk':'WikiTalk','Ali / Hwang and collaborators: rule-map lineage':'Ali / Hwang Hybrid rule-map lineage','Tuyen / Chong / Celiktutan: cGAN lineage':'Tuyen / Chong / Celiktutan cGAN'}
 short.update({'Pelachaud / Greta and collaborators':'Greta / Pelachaud','TalkSHOW / MPI and collaborators':'TalkSHOW / MPI'})
 qualifying=set(s['repeated_method_ids'])
 for g in groups:
  methods=sorted({(r['method_year'],r['method_id']) for r in data['records'] if r['family']==g['family'] and r['method_id'] in qualifying})
  if not methods: continue
  citations=' · '.join(f'[{year}]({citation_prefix}#paper-{mid})' for year,mid in methods)
  lines.append(f"| {short.get(g['family'],g['family'])}<br><sub>{citations}</sub> | {g['years']} | **{g['functional']}** | {g['other_applications']+g['comparison']} |")
 lines+=['','¹ Live comparisons, content/presentation applications and prepared-stimulus studies. Counts cover each group; linked papers individually meet the two-use threshold.']
 return '\n'.join(lines)

def column_definitions():
 return [
 ('Method group','Author/lab family or technical lineage; grouped methods need not be equivalent.'),
 ('Method years','First to last catalogue publication year of the represented methods, not the application papers.'),
 ('Functional','Distinct papers demonstrating supported generator/planner reuse in a separate responsive application.'),
 ('Runtime','Functional papers with evidence that gestures are generated during use, including labelled author clarification; whole-utterance generation qualifies.'),
 ('Prepared','Functional papers whose utterance gestures were computed before interaction and then selected or played.'),
 ('Timing unknown','Functional papers that establish interaction and reuse but do not establish when gestures are computed.'),
 ('Other applications','Supported live script-driven content, presentation, offline animation and prepared-stimulus uses, outside the functional interactive count.'),
 ('Live comparisons','Live interactive studies where animation or gesture alternatives are the central comparison, kept separate from functional adoption.'),
 ('Candidates','Supported technical reuse in a plausible functional application, with insufficient interaction or application-purpose evidence.'),
 ('Platform','Generator integration into a platform or architecture without an established separate functional application.'),
 ('Components','Specification, realization or partial-channel reuse, rather than adoption of a full gesture generator/planner; can overlap scope categories.'),
 ('Unresolved','Insufficient or conflicting evidence about implementation, identity or usage; excluded from functional totals.'),
 ]

def markdown(data,groups,s):
 lines=['# From Methods to Applications','',readme_summary(data,citation_prefix='README.md'),'','## What this audit finds','', 'Published downstream reuse is concentrated in a small subset of the methods represented in this audit. The BEAT/REA family has 32 functional interactive application papers. Learned generators also reach interactive applications, including HumanoidBot, elder-care services and collaborative robot storytelling. The findings support examining transfer into applications; they do not establish that other methods are unusable or that research without documented adoption is wasted.','', '**Application scenario and generation timing must be recorded separately.** A script, recorded speech, or presentation study does not by itself establish precomputed gestures or an offline-only method. A runtime-capable generator may be evaluated in a presentation, while an interactive agent may play prepared utterance animations.','', '## Method-group counts','', f"The headline identifies **{s['repeated_methods']} method papers across {s['repeated_groups']} groups**, each with at least two distinct downstream usage papers. Adjacent uses include live comparisons, presentations, live script-driven content, offline animation and prepared stimuli. Platform-only, component-only, candidate and unresolved records do not contribute to this threshold. This is a finding within the audited collection, not a field-wide adoption rate.",'',f"In total, this audit records functional interactive reuse for **{s['methods']} method papers across {s['groups']} groups** in **{s['papers']} distinct application papers**. **{s['online']}** functional papers have runtime evidence, including **{s['author_online']}** based on author clarification. Counts below are distinct paper reports within each group; they are not deployment counts, and groups can share papers.",'','Column meanings:','']
 lines += ['- **'+name+'** — '+meaning for name,meaning in column_definitions()]
 lines += ['', '| Method group | Method years | Functional | Runtime | Prepared | Timing unknown | Other applications | Live comparisons | Candidates | Platform | Components | Unresolved |','|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
 for g in groups: lines.append('| '+' | '.join(str(g[k]) for k in ['family','years','functional','online','prepared','timing_unknown','other_applications','comparison','candidates','platform','components','unresolved'])+' |')
 lines+=['', '## Evidence and counting','']
 lines += ['- '+note for note in data['counting_notes']]
 lines+=['', 'The 2020 telepresence cache year conflicts with an available 2022 author PDF. The multilingual rule-map method has a 2025 journal record but was cited as a 2023 preprint in the 2024 physician paper. Historical metadata is retained with these conflicts visible in the relevant entries.','', 'Application papers sit in this separate audit: the main method catalogue excludes application-only papers that do not contribute a generation method. The audit does not change that catalogue scope.','', '## Complete usage list','', 'All 302 reviewed method–paper links are retained, including components and unknowns. Rows describe evidence available at the audit date. Source links permit checking the judgement; corrections supported by an implementation section or author statement are welcome.','']
 for g in groups:
  lines+=['### '+g['family'],'', '| Year / usage paper | Method | Application / timing / role | Counted functional? | Evidence and explanation |','|---|---|---|---|---|']
  for r in sorted((r for r in data['records'] if r['family']==g['family']),key=lambda r:(-(r['paper_year'] or 0),r['paper_title'],r['method_id'])):
   e=lambda x:str(x or '—').replace('|','/').replace('\n',' ')
   evidence='; '.join(f"[{e(x['level'])}]({x['url']})" for x in r['evidence'])
   if r['author_clarification']: evidence+='; author clarification (3 October 2026; not independently verified)'
   lines.append(f"| {r['paper_year'] or '?'} — [{e(r['paper_title'])}]({r['source_url']}) | {r['method_id']} | {r['category']} / {r['generation_mode']} / {r['method_role']} | {'Yes' if r['counts_as_functional_generator_adoption'] else 'No'} | {e(r['decision_rationale'])} {evidence}; {e(r['relationship'])}; system: {e(r['system_cluster'])} |")
  lines.append('')
 lines+=['## Reuse the data','', '[Curated JSON](data/application_usages.json) contains bibliography, method attribution, classifications, system links and evidence provenance. Rebuild this page with `python scripts/build_applications.py`; use `--check` to detect stale outputs. No private inputs are required.','']
 return '\n'.join(lines)

def webpage(data,groups,s):
 h=html.escape
 group_rows=''.join('<tr>'+''.join('<td>'+h(str(g[k]))+'</td>' for k in ['family','years','functional','online','prepared','timing_unknown','other_applications','comparison','candidates','platform','components','unresolved'])+'</tr>' for g in groups)
 usage=[]
 for r in data['records']:
  proof='; '.join(f'<a href="{h(e["url"],quote=True)}">{h(e["level"])}</a>' for e in r['evidence'])
  if r['author_clarification']: proof+='; <strong>Author clarification, 3 Oct 2026; not independently verified</strong>'
  search=h(' '.join([r['family'],r['method_id'],r['paper_title'],r['category'],r['decision_rationale']]).lower(),quote=True)
  usage.append(f'<tr data-functional="{str(r["counts_as_functional_generator_adoption"]).lower()}" data-search="{search}"><td>{r["paper_year"] or "?"}<br><a href="{h(r["source_url"],quote=True)}">{h(r["paper_title"])}</a></td><td>{h(r["method_id"])}<br><small>{h(r["family"])}</small></td><td>{h(r["category"].replace("_"," "))}<br>{h(r["generation_mode"])}<br><small>{h(r["method_role"].replace("_"," "))}</small></td><td><details><summary>Evidence and interpretation</summary><p>{h(r["decision_rationale"])}</p><p>{proof}</p><p>{h(r["relationship"])}<br>System: {h(r["system_cluster"] or "Not resolved")}</p></details></td></tr>')
 notes=''.join('<li>'+h(n)+'</li>' for n in data['counting_notes'])
 definitions=''.join('<li><strong>'+h(name)+'</strong> — '+h(meaning)+'</li>' for name,meaning in column_definitions())
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>From Methods to Applications · Co-Speech Gesture Atlas</title><meta name="description" content="Evidence of co-speech gesture methods reused in applications: method groups, usage papers, runtime generation and uncertainty.">
<style>
:root{{--bg:#fbfbf9;--fg:#1d1f23;--muted:#6b7280;--line:#e1e3e8;--accent:#2a6f97;--panel:#fff}}@media(prefers-color-scheme:dark){{:root{{--bg:#14161a;--fg:#e7e9ee;--muted:#a8adb7;--line:#2c3038;--accent:#7fb3d5;--panel:#1c1f25}}}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 system-ui,sans-serif}}header,main{{max-width:1250px;margin:auto;padding:24px}}nav{{display:flex;gap:20px;flex-wrap:wrap}}a{{color:var(--accent)}}h1{{font-size:clamp(30px,4vw,48px);line-height:1.15;margin-bottom:14px}}h2{{margin-top:40px}}.intro{{max-width:850px}}.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}}.metrics div{{border:1px solid var(--line);padding:16px;border-radius:8px;background:var(--panel)}}.metrics strong{{display:block;font-size:30px}}small,.muted{{color:var(--muted)}}.scroll{{overflow:auto}}table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line)}}th{{font-size:12px}}#usage td:first-child{{min-width:240px}}#usage td:last-child{{min-width:260px}}details p{{max-width:650px}}summary{{cursor:pointer}}.controls{{display:flex;gap:20px;align-items:center;flex-wrap:wrap;margin:16px 0}}input[type=search]{{font:inherit;padding:10px;border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:6px;min-width:260px;flex:1}}.finding{{border-left:4px solid var(--accent);padding:8px 20px;background:var(--panel)}}[hidden]{{display:none!important}}@media(max-width:700px){{header,main{{padding:16px}}.metrics{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body><header><nav><a href="index.html">Atlas explorer</a><a href="citations.html">Citation graph</a><a href="https://github.com/ghazanPK/Co-Speech-gesture-atlas/blob/main/APPLICATIONS.md">Repository findings</a><a href="application-usages.json">Download data</a></nav></header><main>
<p class="muted">APPLICATION REUSE AUDIT · 3 OCTOBER 2026</p><h1>From Methods to Applications</h1><p class="intro">How many co-speech gesture methods have been taken into separate, working applications? This audit traces implemented reuse and distinguishes what each application demonstrates from when its gestures are generated.</p>
<div class="metrics"><div><strong>{s['methods']}</strong>method records with functional interactive reuse</div><div><strong>{s['groups']}</strong>method groups with functional interactive reuse</div><div><strong>{s['papers']}</strong>distinct functional application papers</div><div><strong>{s['online']}</strong>functional papers with runtime evidence*</div></div>
<p><strong>Broader application and prepared-stimulus reuse:</strong> {s['application_methods']} method records across {s['application_groups']} groups, reported in {s['application_papers']} distinct papers. Live animation comparisons and component uses are retained separately below.</p><p class="muted">Coverage: 59 method records, 35 groups, 275 paper identities and 302 method–paper links. Counts describe this collection, not field-wide deployment. *{s['author_online']} runtime decisions rely on author clarification.</p>
<div class="finding"><p><strong>BEAT/REA has the largest documented concentration:</strong> 32 functional interactive application papers. Learned generators also reach functional applications. The distinction that matters is demonstrated reuse and its operating constraints, not citations alone.</p><p><strong>A script or presentation is not evidence of offline-only generation.</strong> Record application setting, runtime capability and generation timing independently.</p></div>
<h2>Method-group counts</h2><p>Functional counts exclude unresolved candidates, component-only integration and live animation comparisons. Other application uses remain visible. Groups can share a paper; do not sum their rows as independent deployments.</p>
<p>Column meanings:</p><ul>{definitions}</ul>
<div class="scroll"><table><thead><tr>{''.join('<th>'+x+'</th>' for x in ['Method group','Method years','Functional','Runtime','Prepared','Timing unknown','Other applications','Live comparisons','Candidates','Platform','Components','Unresolved'])}</tr></thead><tbody>{group_rows}</tbody></table></div>
<h2>Evidence and counting</h2><details><summary>Definitions, provenance and interpretation limits</summary><ul>{notes}</ul><p>Runtime includes whole-utterance generation and does not require streaming. Method dates are catalogue publication years for represented methods, not all papers by a lab. Other applications include content/stimulus use, live script-driven content and presentation. Components can overlap application categories. Runtime-capable does not mean conversational interaction was demonstrated.</p><p>Historical year conflicts remain visible: the telepresence entry retains its cached 2020 year despite an available 2022 author PDF; the multilingual method has a 2025 journal record and a cited 2023 preprint.</p></details>
<h2>Trace each usage</h2><p>The full list retains every reviewed link, including uncertain and component uses. Expand an entry to inspect its evidence.</p><div class="controls"><input id="search" type="search" aria-label="Search application usages" placeholder="Search method, application or purpose"><label><input id="functional" type="checkbox" checked> Functional interactive matches only</label><span id="count" aria-live="polite"></span></div>
<div class="scroll"><table id="usage"><thead><tr><th>Application paper</th><th>Adopted method</th><th>Use / timing / role</th><th>Evidence</th></tr></thead><tbody>{''.join(usage)}</tbody></table></div><p id="empty" hidden>No usages match these filters.</p></main>
<script>const rows=[...document.querySelectorAll('#usage tbody tr')], search=document.getElementById('search'), only=document.getElementById('functional');function update(){{const q=search.value.trim().toLowerCase();let n=0;for(const row of rows){{row.hidden=(only.checked&&row.dataset.functional!=='true')||!row.dataset.search.includes(q);if(!row.hidden)n++;}}document.getElementById('count').textContent=n+' method–paper links';document.getElementById('empty').hidden=n!==0;}}search.addEventListener('input',update);only.addEventListener('change',update);update();</script></body></html>\n'''

def main():
 data=load_audit(); groups,s=summarize(data)
 outputs={ROOT/'APPLICATIONS.md':markdown(data,groups,s),ROOT/'docs/applications.html':webpage(data,groups,s),ROOT/'docs/application-usages.json':json.dumps(data,ensure_ascii=False,indent=2)+'\n'}
 for path in [ROOT/'README.md',ROOT/'docs/index.html']:
  import re
  text=path.read_text(encoding='utf-8')
  if path.name=='README.md': body=readme_summary(data)
  else: body=f'<div class="application-finding"><strong>From methods to applications:</strong> {s["methods"]} method records across {s["groups"]} groups have documented functional interactive reuse in {s["papers"]} distinct papers. <a href="applications.html">Explore usages and evidence →</a><br><small>Audited collection, 3 Oct 2026; paper counts are not deployment counts.</small></div>'
  pattern=re.compile(r'(<!-- BEGIN:applications -->\n).*?(<!-- END:applications -->)',re.S)
  assert pattern.search(text),f'Missing applications markers in {path}'
  outputs[path]=pattern.sub(lambda m:m.group(1)+body+'\n'+m.group(2),text)
 stale=[]
 for path,text in outputs.items():
  if path.exists() and path.read_text(encoding='utf-8')==text: continue
  stale.append(str(path.relative_to(ROOT)))
  if '--check' not in sys.argv: path.write_text(text,encoding='utf-8',newline='\n')
 if '--check' in sys.argv and stale:
  print('Stale application outputs: '+', '.join(stale)); return 1
 print('Application findings up to date.' if not stale else 'Built '+', '.join(stale))
 return 0

if __name__=='__main__': sys.exit(main())
