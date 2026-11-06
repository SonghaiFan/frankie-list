// Unsaved adaptation of getComparisonBuckets in src/lib/app-selectors.ts.
const data=JSON.parse(document.querySelector('#demo-data').textContent);
const inputs=[...document.querySelectorAll('input[data-owner]')];
function render(){
 const buckets=[[],[],[],[]];
 data.items.forEach((item,i)=>{const me=inputs.find(x=>x.dataset.owner==='me'&&+x.dataset.index===i).checked;const them=inputs.find(x=>x.dataset.owner==='them'&&+x.dataset.index===i).checked;buckets[me?(them?0:1):(them?2:3)].push(item);});
 document.querySelector('#buckets').replaceChildren(...buckets.map((items,i)=>{const article=document.createElement('article'),h=document.createElement('h3'),p=document.createElement('p');h.textContent=data.labels[i];p.textContent=items.length?items.join(' / '):'−';article.append(h,p);return article;}));
}
inputs.forEach(x=>x.addEventListener('change',render));document.querySelector('#reset').addEventListener('click',()=>{inputs.forEach(x=>x.checked=x.dataset.owner==='me'?[0,1].includes(+x.dataset.index):[0,2].includes(+x.dataset.index));render();});render();
