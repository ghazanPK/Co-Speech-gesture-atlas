(async function(){
 const fmt=new Intl.NumberFormat('en');
 const text=(id,value)=>document.getElementById(id).textContent=value;
 function row(parent, values){const tr=document.createElement('tr');values.forEach(v=>{const td=document.createElement('td'); if(v instanceof Node)td.append(v);else td.textContent=v??'Not estimable';tr.append(td);});document.getElementById(parent).append(tr);}
 try{const response=await fetch('citation-findings.json');if(!response.ok)throw new Error('No data');const d=await response.json();
 text('snapshot',`Analysis snapshot: ${d.snapshot_date}. Internal graph counts; not a literature-search cutoff.`);
 text('leader-count',d.generation.top10.length+' / '+d.generation.records);text('leader-fraction',(100*d.generation.top10.length/d.generation.records).toFixed(1)+'% of generation-research records');text('top-share',d.generation.top10_share_percent+'%');text('all-share',d.all.top10_share_percent+'%');text('edges',fmt.format(d.unique_edges));
 d.generation.top10.forEach(p=>{const a=document.createElement('a');a.href='explorer.html#tab=generation&q='+encodeURIComponent(p.title);a.textContent=p.title;row('leaders',[a,p.year,p.venue,p.citations,p.code_link?'Recorded':'Not recorded']);});
 const c=d.code_groups;text('code-summary',`Across generation research, records with code links have a median of ${c.code_link.median} internal citations (n=${c.code_link.records}), versus ${c.no_code_link_recorded.median} without a recorded code link (n=${c.no_code_link_recorded.records}).`);
 d.cohorts.forEach(c=>row('cohorts',[c.years,c.code_link.records,c.code_link.median,c.no_code_link_recorded.records,c.no_code_link_recorded.median]));
 d.venues.forEach(v=>row('venues',[v.venue,v.records,v.years.join('–'),v.median,v.code_links]));
 const a=d.author_visibility;text('author-summary',`Author names are available for ${a.records_with_authors} of ${a.generation_records} generation records. The rank correlation between prior author publication presence and internal citations is ${a.spearman_rho} overall.`);
 a.cohorts.forEach(c=>row('author-cohorts',[c.years,c.records,c.spearman_rho]));
 text('sensitivity',`${d.generation.records_with_outgoing} of ${d.generation.records} generation records have at least one recorded outgoing edge. ${d.chronology_conflicts} edges have a cited publication year later than the citing year. Excluding these edges changes the generation top-ten share from ${d.generation.top10_share_percent}% to ${d.chronology_sensitivity.top10_share_percent}%. Such conflicts may reflect publication/preprint dates or record errors; this check does not validate the remaining graph.`);
 d.limitations.forEach(value=>{const li=document.createElement('li');li.textContent=value;document.getElementById('limits').append(li);});
 }catch(error){document.getElementById('load-error').hidden=false;text('snapshot','Snapshot unavailable');}
})();
