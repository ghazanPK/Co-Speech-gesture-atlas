#!/usr/bin/env python3
"""Descriptive concentration and association analysis of the recorded citation graph.

Uses the catalogue and internal edge list, not global citation counts. No causal
effects or author self-citation rates are inferred. Re-run after build_site.py.
"""
import collections
import csv
import datetime
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def analyze(papers):
    catalogue = {p['id']: p for p in papers}
    raw = list(csv.DictReader((ROOT / 'data/citations.csv').open(encoding='utf-8')))
    edges = {(r['citing'], r['cited']) for r in raw}
    assert all(a in catalogue and b in catalogue for a, b in edges)
    incoming = collections.Counter(b for a, b in edges)
    outgoing = collections.Counter(a for a, b in edges)
    generation = [p for p in papers if p['category'] != 'theory' and p['type'] != 'thesis']

    def record(p):
        return {'id': p['id'], 'title': p['title'], 'year': p['year'],
                'venue': p['venue'], 'category': p['category'],
                'code_link': bool(p.get('links', {}).get('code')),
                'citations': incoming[p['id']]}

    def population(rows):
        ranked = sorted(rows, key=lambda p: (-incoming[p['id']], p['id']))
        total = sum(incoming[p['id']] for p in rows)
        return {'records': len(rows), 'incoming_edges': total,
                'records_with_incoming': sum(incoming[p['id']] > 0 for p in rows),
                'records_with_outgoing': sum(outgoing[p['id']] > 0 for p in rows),
                'top10_edges': sum(incoming[p['id']] for p in ranked[:10]),
                'top10_share_percent': round(100 * sum(incoming[p['id']] for p in ranked[:10]) / total, 2) if total else 0,
                'top10': [record(p) for p in ranked[:10]]}

    def group_summary(rows):
        counts = [incoming[p['id']] for p in rows]
        return {'records': len(rows), 'median': statistics.median(counts) if counts else None,
                'mean': round(statistics.mean(counts), 2) if counts else None,
                'with_outgoing': sum(outgoing[p['id']] > 0 for p in rows)}

    code = lambda p: bool(p.get('links', {}).get('code'))
    def ranks(values):
        ordered = sorted(enumerate(values), key=lambda pair: pair[1])
        ranked = [0.0] * len(values)
        i = 0
        while i < len(ordered):
            j = i + 1
            while j < len(ordered) and ordered[j][1] == ordered[i][1]:
                j += 1
            for original, value in ordered[i:j]:
                ranked[original] = (i + 1 + j) / 2
            i = j
        return ranked

    named = [p for p in generation if p.get('authors')]
    prior = []
    for p in named:
        count = max(sum(a in q.get('authors', []) and q['year'] < p['year'] for q in generation) for a in p['authors'])
        prior.append(count)
    def rho(xs, ys):
        return round(statistics.correlation(ranks(xs), ranks(ys)), 3) if len(xs) > 2 and len(set(xs)) > 1 and len(set(ys)) > 1 else None
    author_cohorts = []
    for lo, hi in [(2015, 2019), (2020, 2022), (2023, 2026)]:
        selected = [(p, n) for p, n in zip(named, prior) if lo <= p['year'] <= hi]
        author_cohorts.append({'years': f'{lo}-{hi}', 'records': len(selected),
                              'spearman_rho': rho([n for p, n in selected], [incoming[p['id']] for p, n in selected])})
    clean_incoming = collections.Counter(b for a, b in edges if catalogue[b]['year'] <= catalogue[a]['year'])
    clean_generation_total = sum(clean_incoming[p['id']] for p in generation)
    clean_ranked = sorted((clean_incoming[p['id']] for p in generation), reverse=True)
    cohorts = []
    for lo, hi in [(1965, 2009), (2010, 2014), (2015, 2019), (2020, 2022), (2023, 2026)]:
        rows = [p for p in generation if lo <= p['year'] <= hi]
        cohorts.append({'years': f'{lo}-{hi}', 'code_link': group_summary([p for p in rows if code(p)]),
                        'no_code_link_recorded': group_summary([p for p in rows if not code(p)])})
    venues = []
    # Exact catalogue venue labels are deliberately not merged into guessed families.
    for venue, n in collections.Counter(p['venue'] for p in generation).most_common():
        if n < 10:
            continue
        rows = [p for p in generation if p['venue'] == venue]
        venues.append({'venue': venue, **group_summary(rows),
                       'years': [min(p['year'] for p in rows), max(p['year'] for p in rows)],
                       'code_links': sum(code(p) for p in rows)})
    return {'snapshot_date': datetime.date.today().isoformat(),
            'definition': 'Citation concentration measures the share of recorded within-atlas citation edges received by the most-cited records. It does not measure author self-citation or a causal effect.',
            'raw_edges': len(raw), 'unique_edges': len(edges),
            'chronology_conflicts': sum(catalogue[b]['year'] > catalogue[a]['year'] for a, b in edges),
            'all': population(papers), 'generation': population(generation),
            'code_groups': {'code_link': group_summary([p for p in generation if code(p)]),
                            'no_code_link_recorded': group_summary([p for p in generation if not code(p)])},
            'cohorts': cohorts, 'venues': venues,
            'author_visibility': {'records_with_authors': len(named), 'generation_records': len(generation),
                'proxy': 'Maximum number of strictly earlier generation-research publications in the atlas among a paper\'s listed authors, matched by exact recorded name.',
                'spearman_rho': rho(prior, [incoming[p['id']] for p in named]),
                'cohorts': author_cohorts, 'corresponding_author_available': False,
                'limitations': 'Incomplete author lists and name variants are not disambiguated. This proxy measures recorded prior publication presence, not reputation, institutional status, corresponding-author responsibility, or causal influence.'},
            'chronology_sensitivity': {'generation_incoming_edges': clean_generation_total,
                'top10_share_percent': round(100 * sum(clean_ranked[:10]) / clean_generation_total, 2)},
            'limitations': ['Internal graph counts are not global citation counts.',
                            'Reference harvesting and catalogue selection are incomplete; no recorded edge does not establish no citation.',
                            'A recorded code link is not evidence of working code; missing links are not proof of unavailability.',
                            'Year cohorts reduce one exposure difference but do not control topic, paper role, quality, or harvesting coverage.',
                            'Venue labels are used as recorded; variants and unequal publication ages limit comparison.',
                            'Citation concentration does not establish author self-citation or a reason for citation behavior.']}


def write_public(papers):
    result = analyze(papers)
    (ROOT / 'docs/citation-findings.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    result = write_public(json.loads((ROOT / 'docs/data.json').read_text(encoding='utf-8'))['papers'])
    print(json.dumps({k: result[k] for k in ['unique_edges', 'chronology_conflicts', 'code_groups', 'cohorts', 'venues']}, indent=2))
    for key in ['all', 'generation']:
        print(key, json.dumps(result[key], ensure_ascii=True))
