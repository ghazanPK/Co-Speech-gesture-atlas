(async function () {
  const nf = new Intl.NumberFormat('en');
  const date = value => new Date(value + 'T12:00:00').toLocaleDateString('en-GB', {day:'numeric',month:'short',year:'numeric'});
  function bar(parent, label, count, max) {
    const row = document.createElement('div'); row.className = 'bar-row';
    const caption = document.createElement('div'); caption.className = 'bar-caption';
    const name = document.createElement('span'); name.textContent = label;
    const number = document.createElement('b'); number.textContent = nf.format(count);
    caption.append(name, number);
    const track = document.createElement('div'); track.className = 'bar-track';
    const fill = document.createElement('div'); fill.className = 'bar-fill'; fill.style.width = `${count / max * 100}%`;
    track.append(fill); row.append(caption,track); parent.append(row);
  }
  try {
    const response = await fetch('overview.json'); if (!response.ok) throw new Error('Snapshot unavailable');
    const data = await response.json();
    document.querySelectorAll('[data-stat]').forEach(el => {
      const key = el.dataset.stat;
      const value = key === 'year-range' ? data.years.join('–') : key.split('.').reduce((v,k) => v[k],data);
      el.textContent = typeof value === 'number' ? nf.format(value) : value;
    });
    document.getElementById('snapshot').textContent = `Snapshot built ${date(data.snapshot_date)}. Live totals update with reviewed repository changes.`;
    document.getElementById('record-date').textContent = `Latest paper-record addition: ${date(data.latest_record_added)}. This is an addition date, not a certified literature-search cutoff.`;
    document.getElementById('audit-date').textContent = `Application audit: ${date(data.audit_date)}.`;
    const labels = {'Cassell / Vilhjalmsson / Bickmore: BEAT and REA':'BEAT / REA','Marsella / USC ICT: NVBG, Cerebella and learned gestures':'NVBG / Cerebella / USC ICT','Meena / WikiTalk':'WikiTalk','Ali / Hwang and collaborators: rule-map lineage':'Ali / Hwang rule-map lineage','Tuyen / Chong / Celiktutan: cGAN lineage':'Tuyen / Chong / Celiktutan cGAN'};
    data.usage_groups.slice(0,5).forEach(g => bar(document.getElementById('reuse-bars'), labels[g.family] || g.family, g.functional, data.usage_groups[0].functional || 1));
    [['full-text','Full text'],['abstract','Abstract'],['metadata','Bibliographic metadata']].forEach(([key,label]) => bar(document.getElementById('reading-bars'),label,data.reading[key],data.papers));
  } catch (error) {
    document.getElementById('snapshot').textContent = 'Snapshot unavailable';
    document.getElementById('load-error').hidden = false;
  }
})();
fetch('citation-findings.json').then(response=>{if(!response.ok)throw new Error('No analysis');return response.json();}).then(data=>{document.getElementById('citation-share').textContent=data.generation.top10_share_percent+'%';}).catch(()=>{document.getElementById('citation-share').textContent='Unavailable';});
