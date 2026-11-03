# Builds the ParentRight Korea static site into ./site
import os, textwrap

PREFIX = "/parentright-korea"  # GitHub Pages subpath; set to "" when moving to a custom domain
BASE = "https://intid85.github.io" + PREFIX
KOFI_URL = ""  # e.g. "https://ko-fi.com/yourname" - support buttons appear only when set
UPDATED = {"en": "Last reviewed: November 2026", "vi": "Cập nhật lần cuối: tháng 11/2026", "ko": "최종 검토: 2026년 11월"}

CSS = """
:root{--bg:#f7f8f6;--card:#fff;--ink:#1d2b2a;--muted:#5b6b69;--accent:#0f6b63;--accent-soft:#e3f0ee;--warn:#8a4b0f;--warn-soft:#fbf0e3;--line:#dde5e3}
@media (prefers-color-scheme:dark){:root{--bg:#121816;--card:#1a2321;--ink:#e6eeec;--muted:#9fb1ae;--accent:#5cc0b5;--accent-soft:#1e3330;--warn:#f0b36e;--warn-soft:#332716;--line:#2b3936}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","Noto Sans KR",sans-serif}
a{color:var(--accent)}
header{background:var(--card);border-bottom:1px solid var(--line)}
.wrap{max-width:860px;margin:0 auto;padding:0 16px}
.top{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center;justify-content:space-between;padding:14px 16px}
.brand{font-weight:700;font-size:1.1rem;text-decoration:none;color:var(--ink)}
.brand span{color:var(--accent)}
nav a{margin-right:14px;text-decoration:none;font-size:.95rem}
.lang a{font-size:.9rem;margin-right:10px;text-decoration:none}
.lang a.on{font-weight:700;text-decoration:underline}
.hero{padding:40px 0 16px}
.hero h1{font-size:1.9rem;line-height:1.25;margin:0 0 12px}
.hero p{color:var(--muted);margin:0;font-size:1.05rem}
h2{font-size:1.35rem;margin:40px 0 12px}
h3{font-size:1.08rem;margin:22px 0 6px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin:14px 0}
.step{display:flex;gap:14px}
.num{flex:0 0 34px;height:34px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
.step h3{margin-top:4px}
.note{background:var(--accent-soft);border-radius:10px;padding:14px 16px;margin:14px 0}
.warn{background:var(--warn-soft);border-left:4px solid var(--warn);border-radius:8px;padding:14px 16px;margin:14px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.grid .card{margin:0}
.grid .card a{font-weight:600}
ul{padding-left:22px}li{margin:4px 0}
.small{font-size:.9rem;color:var(--muted)}
footer{border-top:1px solid var(--line);margin-top:48px;padding:24px 0 40px;font-size:.9rem;color:var(--muted)}
footer a{margin-right:14px}
"""

LANG_LINKS = {"en": "/", "vi": "/vi/", "ko": "/ko/"}
LANG_NAMES = {"en": "English", "vi": "Tiếng Việt", "ko": "한국어"}

def page(lang, path, title, desc, body, nav):
    langs = "".join(f'<a href="{LANG_LINKS[l]}" class="{"on" if l==lang else ""}" hreflang="{l}">{LANG_NAMES[l]}</a>' for l in LANG_LINKS)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{LANG_LINKS[l]}">' for l in LANG_LINKS)
    navhtml = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    foot = FOOTER[lang]
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">{alts}
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<style>{CSS}</style></head><body>
<header><div class="wrap top"><a class="brand" href="{LANG_LINKS[lang]}">Parent<span>Right</span> Korea</a>
<nav>{navhtml}</nav><div class="lang">{langs}</div></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">{foot}<p>{UPDATED[lang]}</p></div></footer>
</body></html>"""

FOOTER = {
"en": '<p><a href="/find-help.html">Find help</a><a href="/about.html">About &amp; privacy</a><a href="/philippines.html">Philippines</a><a href="/vietnam.html">Vietnam</a></p><p>ParentRight Korea is an independent information guide. It is not a law firm, does not give legal advice, does not refer cases to lawyers for a fee, and never publishes information about any individual.</p>',
"vi": '<p>ParentRight Korea là trang hướng dẫn thông tin độc lập. Chúng tôi không phải công ty luật, không tư vấn pháp lý, không giới thiệu luật sư để lấy phí và không bao giờ đăng thông tin về bất kỳ cá nhân nào.</p>',
"ko": '<p>ParentRight Korea는 독립 정보 안내 사이트입니다. 법률사무소가 아니며 법률 자문을 하지 않고, 대가를 받고 변호사를 소개하지 않으며, 특정 개인에 관한 정보를 절대 게시하지 않습니다.</p>',
}

# ---------------- ENGLISH ----------------
EN_NAV = [("/find-help.html", "Find help"), ("/#steps", "Steps"), ("/philippines.html", "Philippines"), ("/vietnam.html", "Vietnam"), ("/about.html", "About")]

EN_HOME = """
<section class="hero"><h1>Your child's father is Korean and he stopped supporting you. Here is the legal way forward.</h1>
<p>A step-by-step guide for mothers outside Korea: proving paternity in a Korean court, claiming child support, and your child's right to Korean nationality.</p>
<p style="margin-top:18px"><a href="/find-help.html" style="display:inline-block;background:var(--accent);color:#fff;padding:12px 20px;border-radius:10px;text-decoration:none;font-weight:600">Find where to get help in Korea →</a></p></section>

<div class="note"><strong>You have real rights.</strong> Korean family courts have ruled for foreign mothers and their children. In 2014 the Seoul Family Court recognized two children living in the Philippines as the sons of their Korean father, and later rulings ordered fathers to pay monthly child support and past support.</div>

<div class="warn"><strong>Do not post his name or photos online.</strong> In Korea, publishing true facts that damage someone's reputation can still be a crime (defamation), and posting personal data can break privacy law. It can also warn him, make him hide assets, and weaken your court case. Keep your evidence private and use it in court.</div>

<h2 id="steps">The 6 steps</h2>

<div class="card step"><div class="num">1</div><div><h3>Collect and protect your evidence</h3>
<p>Save everything privately, in two places (phone and cloud or USB):</p>
<ul><li>His full name (in Korean letters if you have it), date of birth, any ID or passport details you were legitimately given</li>
<li>Phone numbers, KakaoTalk, LINE, Facebook or Instagram accounts and the dates they stopped working</li>
<li>Messages, photos together, travel dates, money transfers he sent</li>
<li>Pregnancy and hospital records, especially if he came with you</li>
<li>Your child's birth certificate</li></ul>
<p class="small">Even if you do not know his address, these details help a court and lawyers find him through official channels.</p></div></div>

<div class="card step"><div class="num">2</div><div><h3>Try voluntary acknowledgment first</h3>
<p>If you can still reach him, he can recognize the child voluntarily. This is called <em>voluntary acknowledgment</em> (임의인지). He files it at a Korean local office or a Korean embassy. A private DNA test by agreement can come first. This is the fastest and cheapest route.</p></div></div>

<div class="card step"><div class="num">3</div><div><h3>If he refuses: a paternity case in a Korean Family Court</h3>
<p>Under Article 863 of Korea's Civil Act, a child, or the child's legal representative (usually the mother), can sue the father for <em>acknowledgment</em> (인지청구의 소). You can do this while living abroad.</p>
<ul><li>The case is filed at the family court where the father has his domicile in Korea.</li>
<li>Family cases of this type usually go to mediation first.</li>
<li>If he denies being the father, the court can order a DNA test. If he refuses without good reason, he can be fined up to 10 million won, and if he still refuses, detained for up to 30 days until he complies.</li>
<li>Samples from you and your child can, in some cases, be collected abroad and sent to a Korean lab named by the court.</li>
<li>The child's right to be acknowledged cannot be waived. If the father has died, a case can still be filed against the public prosecutor, but only within 2 years of learning of his death.</li></ul></div></div>

<div class="card step"><div class="num">4</div><div><h3>Claim child support</h3>
<p>You can ask for future monthly support until the child is an adult, and support for past years, often in the same case. Amounts depend on his income and your child's needs. Some fathers settle and pay a lump sum once a case starts.</p></div></div>

<div class="card step"><div class="num">5</div><div><h3>Make the order work</h3>
<p>A Korean judgment is easiest to enforce against money or property in Korea (wages, bank accounts, real estate). If he keeps ignoring court orders, Korea's <strong>Child Support Enforcement Agency</strong> (양육비이행관리원) can pursue sanctions, including asking the Justice Ministry to ban him from leaving Korea. Ask the agency whether it can take your case if you live abroad.</p>
<p class="small">Korea, the Philippines and Vietnam are not, as far as we can find, members of the 2007 Hague Child Support Convention, so treaty enforcement between these countries is generally not available. Check the current status on the HCCH website.</p></div></div>

<div class="card step"><div class="num">6</div><div><h3>Your child's Korean nationality</h3>
<p>Under Article 3 of Korea's Nationality Act, a child acknowledged by a Korean father can acquire Korean nationality by reporting to the Minister of Justice, if the child is still a minor under Korean law and the father was Korean when the child was born.</p></div></div>

<h2 id="help">Free and low-cost help</h2>
<div class="grid">
<div class="card"><a href="https://www.klac.or.kr" rel="noopener">Korea Legal Aid Corporation</a><p class="small">Call 132 in Korea. Free legal advice and court representation for low-income people, including foreign residents in Korea.</p></div>
<div class="card"><a href="https://www.liveinkorea.kr" rel="noopener">Danuri Helpline 1577-1366</a><p class="small">24/7, 13 languages including English, Tagalog and Vietnamese. For migrants and multicultural families in Korea; free lawyer consultations by appointment.</p></div>
<div class="card"><a href="https://www.childsupport.or.kr" rel="noopener">Child Support Enforcement Agency</a><p class="small">Korean government agency, 1644-6621. Helps collect unpaid child support and apply sanctions.</p></div>
<div class="card"><a href="https://www.scourt.go.kr" rel="noopener">Korean courts: litigation aid</a><p class="small">If you cannot afford court costs, you can ask the court to defer fees (소송구조).</p></div>
<div class="card"><strong>Certified document translation</strong><p class="small">Coming soon. Korean courts need translations of birth certificates and other papers. We are preparing a trusted translation partner.</p></div>
</div>
<p>Country guides: <a href="/philippines.html">Philippines</a> · <a href="/vietnam.html">Vietnam</a></p>

{{SUPPORT_EN}}
<h2>Protect yourself</h2>
<ul><li>Never pay a "father finder" in advance. Real NGOs and legal aid do not ask for big upfront fees.</li>
<li>Do not send your child's documents to people you only know online.</li>
<li>If you are threatened, contact your local police and keep the messages.</li></ul>

<h2>Legal sources</h2>
<ul class="small"><li>Civil Act Art. 863 (suit for acknowledgment); Family Litigation Act Arts. 26, 29, 50, 67; Nationality Act Art. 3: <a href="https://www.law.go.kr" rel="noopener">law.go.kr</a> (English versions at <a href="https://elaw.klri.re.kr" rel="noopener">elaw.klri.re.kr</a>)</li>
<li>Act on Securing and Supporting Child Support Payments, Art. 21-4 (travel ban requests)</li>
<li>HCCH 2007 Child Support Convention status: <a href="https://www.hcch.net" rel="noopener">hcch.net</a></li></ul>
<p class="small">This page is general information, not legal advice. Laws change; confirm with legal aid or a lawyer before acting.</p>
"""

EN_PH = """
<section class="hero"><h1>Philippines: help for mothers of Kopino children</h1>
<p>Children of Filipino mothers and Korean fathers (often called Kopino) have won paternity and child-support cases in Korean courts.</p></section>
<div class="note">Follow the <a href="/#steps">6 steps</a>. This page adds what is specific to the Philippines.</div>
<h2>What has worked</h2>
<ul><li>2014: Seoul Family Court recognized two children living in the Philippines as the sons of their Korean father.</li>
<li>Later cases ordered fathers to pay monthly child support until adulthood, and in one case about 20 million won in past support.</li>
<li>Some fathers agreed to a settlement after the case was filed.</li></ul>
<h2>Organizations that have helped Kopino families</h2>
<ul><li><strong>We Love Kopino (WLK)</strong>, a Manila-based NGO that has helped mothers bring cases in Korean courts.</li>
<li><strong>Kopino Children Association</strong>, which runs education and shelter programs.</li>
<li><strong>The Korean Embassy in Manila</strong>, consular section, for questions about acknowledgment and nationality paperwork.</li></ul>
<p class="small">We list organizations for information only and are not paid by or affiliated with them. Contact them through their official pages.</p>
<h2>Documents to prepare</h2>
<ul><li>PSA birth certificate of your child, and an English or Korean translation if requested</li>
<li>Your passport or government ID</li>
<li>Evidence from step 1</li>
<li>If needed later: a certificate of no marriage (CENOMAR) for nationality paperwork</li></ul>
<div class="warn">Old "Kopino father" blogs posted photos and names of men. Do not copy that. It can expose you to defamation claims and does not create a legal duty to pay. A court case does.</div>
"""

EN_VN = """
<section class="hero"><h1>Vietnam: when your child's Korean father disappears</h1>
<p>The same Korean court process applies to Vietnamese mothers, whether you live in Vietnam or in Korea.</p></section>
<div class="note">Follow the <a href="/#steps">6 steps</a>. A Vietnamese version of this guide is <a href="/vi/">here</a>.</div>
<h2>If you live in Korea</h2>
<ul><li>Call <strong>Danuri 1577-1366</strong> and choose Vietnamese. It is free, 24 hours a day, and can connect you to free lawyer consultations.</li>
<li>Low-income foreign residents can apply to the <strong>Korea Legal Aid Corporation (132)</strong> for free representation.</li>
<li>If you were married to him in Korea, the divorce court can decide custody and child support at the same time.</li></ul>
<h2>If you live in Vietnam</h2>
<ul><li>Contact the <strong>Korean Embassy in Hanoi</strong> or the <strong>Consulate General in Ho Chi Minh City</strong> for document questions.</li>
<li>A Korean lawyer can file the case for you; you may not need to travel. Ask whether DNA samples can be collected in Vietnam.</li>
<li>Prepare your child's birth certificate (Giấy khai sinh) with a certified translation.</li></ul>
"""

EN_ABOUT = """
<section class="hero"><h1>About ParentRight Korea</h1></section>
<h2>What we do</h2><p>We explain, in plain language, the official legal routes for children of Korean fathers to be recognized and supported.</p>
<h2>What we never do</h2>
<ul><li>We never publish names, photos, contact details or any information about any person.</li>
<li>We do not accept posts, comments or uploads.</li>
<li>We do not give legal advice and are not a law firm.</li>
<li>We do not refer cases to lawyers for money.</li></ul>
{{SUPPORT_EN}}
<h2>Privacy</h2><p>This site has no accounts and does not collect personal data. {{DONATION_PRIVACY}} The "Find help" questions run only inside your browser; answers are never sent or stored. If analytics or ads are added later, this page will be updated first.</p>
<h2>Corrections</h2><p>If something is wrong or out of date, please tell us at <a href="mailto:contact@parentright.example">contact@parentright.example</a>. Please do not send us personal information about anyone.</p>
"""

EN_FIND = """
<section class="hero"><h1>Find where to get help in Korea</h1>
<p>Answer 6 quick questions. We will show which Korean offices and organizations fit your situation, with phone numbers and links.</p></section>
<div class="note small">Your answers stay in your browser. Nothing is sent, saved or tracked. Do not type anyone's name here; there is no box for it.</div>

<form id="finder" class="card" onsubmit="return false">
<h3>1. Where do you live now?</h3>
<label><input type="radio" name="live" value="kr"> In Korea</label><br>
<label><input type="radio" name="live" value="ph"> Philippines</label><br>
<label><input type="radio" name="live" value="vn"> Vietnam</label><br>
<label><input type="radio" name="live" value="other"> Another country</label>

<h3>2. Were you legally married to him?</h3>
<label><input type="radio" name="married" value="yes"> Yes</label>
<label style="margin-left:16px"><input type="radio" name="married" value="no"> No</label>

<h3>3. Has a court already ordered him to pay child support?</h3>
<label><input type="radio" name="order" value="no"> No, not yet</label><br>
<label><input type="radio" name="order" value="yes"> Yes, but he does not pay</label>

<h3>4. Can you still contact him?</h3>
<label><input type="radio" name="contact" value="yes"> Yes</label>
<label style="margin-left:16px"><input type="radio" name="contact" value="no"> No</label>

<h3>5. Is your household income low?</h3>
<label><input type="radio" name="income" value="low"> Yes</label>
<label style="margin-left:16px"><input type="radio" name="income" value="unsure"> Not sure</label>
<label style="margin-left:16px"><input type="radio" name="income" value="no"> No</label>

<h3>6. Are you being threatened or are you unsafe right now?</h3>
<label><input type="radio" name="danger" value="yes"> Yes</label>
<label style="margin-left:16px"><input type="radio" name="danger" value="no"> No</label>

<p style="margin-top:20px"><button id="go" type="button" style="background:var(--accent);color:#fff;border:0;padding:12px 22px;border-radius:10px;font-size:1rem;font-weight:600;cursor:pointer">Show my help options</button></p>
<p id="missing" class="small" style="display:none;color:var(--warn)">Please answer all 6 questions.</p>
</form>

<div id="result" aria-live="polite"></div>

<script>
(function(){
  var H = {
    police: {kr:["Police (Korea)","112","https://www.police.go.kr/eng/"], ph:["Philippine National Police","911",""], vn:["Vietnam Police","113",""], other:["Local police","Your local emergency number",""]},
    danuri: ["Danuri Helpline","1577-1366 (24/7, 13 languages incl. English, Tagalog, Vietnamese)","https://www.liveinkorea.kr","Free counseling, interpretation, emergency shelter and free lawyer consultations by appointment for migrants and multicultural families in Korea."],
    klac: ["Korea Legal Aid Corporation","132 (in Korea)","https://www.klac.or.kr","Free legal advice and court representation for low-income people, including foreign residents of Korea."],
    kba: ["Korean Bar Association Legal Aid Foundation","","https://www.koreanbar.or.kr","Legal aid programs for migrants, multicultural families and single-parent families."],
    csea: ["Child Support Enforcement Agency (양육비이행관리원)","1644-6621","https://www.childsupport.or.kr","Korean government agency that helps collect unpaid child support and can request sanctions such as a travel ban. Ask whether it can accept your case if you live abroad."],
    aid: ["Court litigation aid (소송구조)","Ask the family court or your lawyer","https://www.scourt.go.kr","If you cannot afford court costs, the court can defer fees for people without means."],
    emb_ph: ["Korean Embassy in the Philippines (consular section)","","https://overseas.mofa.go.kr/ph-en/index.do","Questions about acknowledgment and nationality paperwork."],
    emb_vn: ["Korean Embassy in Vietnam / Consulate General in Ho Chi Minh City","","https://overseas.mofa.go.kr/vn-en/index.do","Questions about acknowledgment and nationality paperwork."],
    emb_other: ["Korean embassy or consulate in your country","","https://overseas.mofa.go.kr","Find your nearest Korean embassy for document questions."],
    ngo_ph: ["Kopino support NGOs","We Love Kopino (WLK), Kopino Children Association","","Have helped Filipino mothers bring cases in Korean courts. Contact them only through their official pages."],
    lawyer: ["A Korean family-law attorney","","","Can file in Korean court on your behalf so you may not need to travel. Ask about fees first and whether DNA samples can be taken in your country."]
  };
  function card(x, why){
    var link = x[2] ? '<a href="'+x[2]+'" rel="noopener" target="_blank">'+x[0]+'</a>' : '<strong>'+x[0]+'</strong>';
    var tel = x[1] ? '<div><strong>'+x[1]+'</strong></div>' : '';
    var desc = x[3] ? '<p class="small" style="margin:6px 0 0">'+x[3]+'</p>' : '';
    var w = why ? '<p class="small" style="margin:6px 0 0"><em>'+why+'</em></p>' : '';
    return '<div class="card">'+link+tel+desc+w+'</div>';
  }
  function val(n){var e=document.querySelector('input[name="'+n+'"]:checked');return e?e.value:null;}
  document.getElementById('go').addEventListener('click', function(){
    var a = {live:val('live'),married:val('married'),order:val('order'),contact:val('contact'),income:val('income'),danger:val('danger')};
    for (var k in a){ if(!a[k]){document.getElementById('missing').style.display='block';return;} }
    document.getElementById('missing').style.display='none';
    var out = [], route;
    if (a.danger==='yes'){ var p=H.police[a.live]; out.push('<div class="warn"><strong>Your safety comes first.</strong> Call '+p[0]+': <strong>'+p[1]+'</strong>. Save threatening messages as evidence.</div>'); if(a.live==='kr') out.push(card(H.danuri,'Danuri can arrange emergency shelter, including with your child.')); }

    if (a.order==='yes'){
      route = 'You already have a court order. Your next step is <strong>enforcement</strong>: collecting from his wages, bank accounts or property in Korea, and applying sanctions if he keeps ignoring the order.';
    } else if (a.contact==='yes'){
      route = 'Because you can still reach him, first ask him to <strong>acknowledge the child voluntarily</strong> at a Korean local office or embassy (a DNA test by agreement can come first). If he refuses, go to court.';
    } else if (a.married==='yes'){
      route = 'Because you were married, a Korean family court can decide <strong>divorce, custody and child support</strong> together. A child born during the marriage is generally presumed to be his.';
    } else {
      route = 'Because you were not married and cannot reach him, the usual route is a <strong>paternity (acknowledgment) case in a Korean family court</strong>, together with a child-support claim. The court can order a DNA test.';
    }
    out.push('<h2>Your likely route</h2><div class="note">'+route+' <a href="/#steps">See all 6 steps</a>.</div><h2>Where to get help</h2>');

    if (a.live==='kr'){
      if (a.danger!=='yes') out.push(card(H.danuri,'You live in Korea: start here for free help in your language.'));
      if (a.income!=='no') out.push(card(H.klac,'You may qualify as a low-income resident.'));
      out.push(card(H.kba));
    } else {
      var e = a.live==='ph'?H.emb_ph:(a.live==='vn'?H.emb_vn:H.emb_other);
      out.push(card(e));
      if (a.live==='ph') out.push(card(H.ngo_ph,'Groups with experience in Kopino cases.'));
      out.push(card(H.lawyer,'You live outside Korea, so a lawyer in Korea can act for you.'));
      out.push(card(H.danuri,'Mainly for people in Korea, but your family or friends in Korea can call for information.'));
    }
    if (a.order==='yes') out.push(card(H.csea,'You have an order he is not following.'));
    if (a.income!=='no') out.push(card(H.aid,'Court fees can be deferred if money is tight.'));

    out.push('<div class="warn small">Do not post his name or photos online, and never pay a "father finder" in advance. This page is general information, not legal advice.</div>');
    var r=document.getElementById('result'); r.innerHTML=out.join(''); r.scrollIntoView({behavior:'smooth'});
  });
})();
</script>
"""

# ---------------- VIETNAMESE ----------------
VI_NAV = [("#cac-buoc", "Các bước"), ("#ho-tro", "Hỗ trợ miễn phí"), ("#gioi-thieu", "Giới thiệu")]
VI_HOME = """
<section class="hero"><h1>Bố của con bạn là người Hàn Quốc và đã ngừng chu cấp? Đây là con đường hợp pháp.</h1>
<p>Hướng dẫn từng bước: xác nhận cha con tại tòa án Hàn Quốc, yêu cầu tiền cấp dưỡng nuôi con và quyền có quốc tịch Hàn Quốc của con bạn.</p></section>

<div class="note"><strong>Bạn có quyền thật sự.</strong> Tòa án gia đình Hàn Quốc đã nhiều lần xử cho mẹ và con người nước ngoài thắng kiện, buộc người cha công nhận con và trả tiền cấp dưỡng hằng tháng.</div>

<div class="warn"><strong>Đừng đăng tên hoặc ảnh của anh ta lên mạng.</strong> Ở Hàn Quốc, đăng cả sự thật làm tổn hại danh dự người khác vẫn có thể bị xử lý hình sự (tội phỉ báng). Việc này còn có thể khiến anh ta trốn tránh, tẩu tán tài sản và làm hồ sơ kiện của bạn yếu đi. Hãy giữ bằng chứng riêng tư và dùng tại tòa.</div>

<h2 id="cac-buoc">6 bước</h2>
<div class="card step"><div class="num">1</div><div><h3>Thu thập và bảo vệ bằng chứng</h3>
<ul><li>Họ tên đầy đủ (bằng chữ Hàn nếu có), ngày sinh, thông tin hộ chiếu mà anh ta đã đưa cho bạn</li>
<li>Số điện thoại, KakaoTalk, Zalo, Facebook và ngày các tài khoản ngừng hoạt động</li>
<li>Tin nhắn, ảnh chụp chung, thời gian đi lại, các lần chuyển tiền</li>
<li>Hồ sơ khám thai, đặc biệt nếu anh ta đi cùng bạn</li>
<li>Giấy khai sinh của con</li></ul>
<p class="small">Lưu ở hai nơi (điện thoại và USB hoặc lưu trữ đám mây).</p></div></div>

<div class="card step"><div class="num">2</div><div><h3>Thử đề nghị anh ta tự nguyện nhận con</h3>
<p>Nếu còn liên lạc được, người cha có thể tự nguyện công nhận con (임의인지) tại cơ quan hành chính Hàn Quốc hoặc Đại sứ quán Hàn Quốc. Có thể xét nghiệm ADN theo thỏa thuận trước. Đây là cách nhanh và rẻ nhất.</p></div></div>

<div class="card step"><div class="num">3</div><div><h3>Nếu anh ta từ chối: kiện yêu cầu công nhận cha con tại Tòa án gia đình Hàn Quốc</h3>
<p>Theo Điều 863 Bộ luật Dân sự Hàn Quốc, người con hoặc người đại diện hợp pháp (thường là mẹ) có thể kiện người cha để yêu cầu công nhận con (인지청구의 소). Bạn có thể kiện khi đang sống ở nước ngoài.</p>
<ul><li>Vụ kiện được nộp tại tòa án gia đình nơi người cha cư trú ở Hàn Quốc.</li>
<li>Thông thường sẽ hòa giải trước.</li>
<li>Nếu anh ta phủ nhận, tòa có thể ra lệnh xét nghiệm ADN. Từ chối không có lý do chính đáng có thể bị phạt đến 10 triệu won, và nếu tiếp tục từ chối có thể bị tạm giữ đến 30 ngày.</li>
<li>Trong một số trường hợp, mẫu ADN của mẹ và con có thể được lấy ở nước ngoài và gửi về phòng xét nghiệm do tòa chỉ định.</li>
<li>Quyền được công nhận của con không thể bị từ bỏ. Nếu người cha đã mất, vẫn có thể kiện nhưng phải trong vòng 2 năm kể từ khi biết tin.</li></ul></div></div>

<div class="card step"><div class="num">4</div><div><h3>Yêu cầu tiền cấp dưỡng</h3>
<p>Bạn có thể yêu cầu tiền cấp dưỡng hằng tháng đến khi con trưởng thành và cả tiền cấp dưỡng cho những năm trước, thường trong cùng một vụ kiện.</p></div></div>

<div class="card step"><div class="num">5</div><div><h3>Thi hành bản án</h3>
<p>Bản án Hàn Quốc dễ thi hành nhất với tiền lương, tài khoản ngân hàng hoặc tài sản ở Hàn Quốc. Nếu anh ta không chấp hành, <strong>Cơ quan Thi hành Cấp dưỡng Nuôi con</strong> (양육비이행관리원, 1644-6621) có thể áp dụng biện pháp chế tài, kể cả đề nghị cấm xuất cảnh. Hãy hỏi cơ quan này xem họ có nhận hồ sơ khi bạn sống ở nước ngoài không.</p></div></div>

<div class="card step"><div class="num">6</div><div><h3>Quốc tịch Hàn Quốc của con</h3>
<p>Theo Điều 3 Luật Quốc tịch Hàn Quốc, con được người cha Hàn Quốc công nhận có thể nhận quốc tịch Hàn Quốc bằng cách khai báo với Bộ trưởng Bộ Tư pháp, nếu con còn là trẻ vị thành niên theo luật Hàn Quốc và người cha là công dân Hàn Quốc khi con sinh ra.</p></div></div>

<h2 id="ho-tro">Hỗ trợ miễn phí</h2>
<div class="grid">
<div class="card"><a href="https://www.liveinkorea.kr" rel="noopener">Tổng đài Danuri 1577-1366</a><p class="small">24/7, có tiếng Việt. Dành cho người nhập cư và gia đình đa văn hóa tại Hàn Quốc; có tư vấn luật sư miễn phí theo lịch hẹn.</p></div>
<div class="card"><a href="https://www.klac.or.kr" rel="noopener">Tổ chức Trợ giúp Pháp lý Hàn Quốc (132)</a><p class="small">Tư vấn và đại diện tại tòa miễn phí cho người thu nhập thấp, kể cả người nước ngoài cư trú tại Hàn Quốc.</p></div>
<div class="card"><a href="https://www.childsupport.or.kr" rel="noopener">Cơ quan Thi hành Cấp dưỡng</a><p class="small">Cơ quan nhà nước Hàn Quốc, 1644-6621.</p></div>
<div class="card"><strong>Đại sứ quán Hàn Quốc tại Hà Nội / Tổng Lãnh sự quán tại TP.HCM</strong><p class="small">Hỏi về giấy tờ công nhận con và quốc tịch.</p></div>
</div>

<h2>Tự bảo vệ bản thân</h2>
<ul><li>Không trả tiền trước cho người hứa "tìm cha giúp".</li>
<li>Không gửi giấy tờ của con cho người chỉ quen trên mạng.</li>
<li>Nếu bị đe dọa, hãy báo công an và giữ lại tin nhắn.</li></ul>

{{SUPPORT_VI}}
<h2 id="gioi-thieu">Giới thiệu và quyền riêng tư</h2>
<p>Chúng tôi chỉ giải thích các con đường pháp lý chính thức. Chúng tôi không bao giờ đăng tên, ảnh hay thông tin của bất kỳ ai, không nhận bài đăng hay bình luận, không tư vấn pháp lý và không giới thiệu luật sư để lấy tiền. Trang này không thu thập dữ liệu cá nhân.</p>
<p class="small">Đây là thông tin chung, không phải tư vấn pháp lý. Luật có thể thay đổi; hãy xác nhận với trợ giúp pháp lý hoặc luật sư.</p>
"""

# ---------------- KOREAN ----------------
KO_NAV = [("#steps", "절차"), ("#help", "무료 지원"), ("#about", "운영 원칙")]
KO_HOME = """
<section class="hero"><h1>한국인 아버지가 연락을 끊었을 때, 아이를 위한 합법적인 길</h1>
<p>해외에 사는 엄마와 아이를 돕는 분들(가족, 다문화센터, 활동가)을 위한 안내입니다. 한국 법원에서 친자관계를 인정받고, 양육비를 청구하고, 아이의 한국 국적을 취득하는 절차를 정리했습니다.</p></section>

<div class="warn"><strong>상대 남성의 이름·사진을 인터넷에 올리지 마세요.</strong> 한국에서는 사실을 적시해도 명예훼손죄가 성립할 수 있고, 개인정보 게시는 개인정보보호법 위반 소지가 있습니다. 상대가 잠적하거나 재산을 숨기는 계기가 되어 소송에도 불리합니다. 증거는 공개하지 말고 법원에서 쓰세요.</div>

<h2 id="steps">6단계 절차</h2>
<div class="card step"><div class="num">1</div><div><h3>증거 모으기</h3>
<ul><li>상대의 한글 성명, 생년월일, 정당하게 받은 신분 정보</li>
<li>전화번호, 카카오톡 등 계정과 연락이 끊긴 시점</li>
<li>메시지, 함께 찍은 사진, 출입국 시기, 송금 내역</li>
<li>임신·병원 기록(동행했다면 특히 중요), 아이 출생증명서</li></ul></div></div>
<div class="card step"><div class="num">2</div><div><h3>임의인지 요청</h3><p>연락이 된다면 아버지가 시·구청이나 재외공관에 스스로 인지신고를 할 수 있습니다. 합의 하에 유전자 검사를 먼저 해도 됩니다.</p></div></div>
<div class="card step"><div class="num">3</div><div><h3>거부하면 인지청구의 소</h3>
<ul><li>민법 제863조: 자녀 또는 법정대리인(보통 엄마)이 아버지를 상대로 제기. 해외 거주 중에도 가능합니다.</li>
<li>상대방 주소지 관할 가정법원 전속관할(가사소송법 제26조 제2항), 원칙적으로 조정 먼저(제50조).</li>
<li>유전자 수검명령(제29조), 정당한 이유 없이 불응하면 1천만원 이하 과태료, 재차 불응 시 30일 범위 감치(제67조).</li>
<li>엄마와 아이의 검체를 해외에서 채취해 법원이 지정한 국내 기관에 보낸 사례가 있습니다.</li>
<li>인지청구권은 포기할 수 없습니다(대법원 2001므1353). 아버지 사망 시 사망을 안 날부터 2년 내 검사를 상대로 제기.</li></ul></div></div>
<div class="card step"><div class="num">4</div><div><h3>양육비 청구</h3><p>장래 양육비와 과거 양육비를 함께 청구할 수 있습니다. 코피노 사건에서 월 30만~50만원, 과거 양육비 2천만원 지급을 명한 판결이 있습니다.</p></div></div>
<div class="card step"><div class="num">5</div><div><h3>집행</h3><p>국내 급여·예금·부동산에 대한 강제집행이 가장 현실적입니다. 이행명령 불이행 시 양육비이행관리원(1644-6621)을 통해 출국금지 요청 등 제재가 가능합니다(양육비이행법 제21조의4). 해외 거주 신청인 접수 가능 여부는 관리원에 확인하세요. 한국·필리핀·베트남은 확인한 범위에서 2007년 헤이그 양육비협약 당사국이 아니어서 조약을 통한 집행은 기대하기 어렵습니다.</p></div></div>
<div class="card step"><div class="num">6</div><div><h3>아이의 한국 국적</h3><p>국적법 제3조: 한국인 아버지에게 인지된 아이가 민법상 미성년이고 출생 당시 아버지가 한국 국민이었다면 법무부장관에게 신고해 국적을 취득할 수 있습니다.</p></div></div>

<h2 id="help">무료 지원</h2>
<ul><li>대한법률구조공단 132: 중위소득 125% 이하 국민·국내 거주 외국인 대상 상담·소송대리</li>
<li>다누리콜센터 1577-1366: 24시간 13개 언어, 변호사 상담 예약 가능</li>
<li>양육비이행관리원 1644-6621</li>
<li>법원 소송구조: 소송비용 납입 유예</li>
<li>서류 번역(출생증명서 등): 제휴 번역 서비스 준비 중</li>
<li>필리핀: We Love Kopino(WLK), Kopino Children Association, 주필리핀 대사관 영사과</li></ul>

{{SUPPORT_KO}}
<h2 id="about">운영 원칙</h2>
<ul><li>특정 개인의 이름·사진·연락처 등 어떤 정보도 게시하지 않습니다.</li>
<li>게시판·댓글·업로드 기능이 없습니다.</li>
<li>법률 자문을 하지 않으며, 대가를 받고 변호사를 소개하지 않습니다(변호사법 준수).</li>
<li>개인정보를 수집하지 않습니다.</li></ul>
<p class="small">일반 정보이며 법률 자문이 아닙니다. 법령은 바뀔 수 있으니 실행 전 법률구조공단이나 변호사에게 확인하세요. 근거 법령: <a href="https://www.law.go.kr" rel="noopener">국가법령정보센터</a></p>
"""


def support_block(lang):
    if not KOFI_URL:
        return ""
    t = {
      "en": ("Support this free guide", "ParentRight Korea is independent and free. Donations keep the guide translated and up to date. Supporters do not get any legal service or priority, and donating is never required to use this site.", "Support on Ko-fi"),
      "vi": ("Ủng hộ trang hướng dẫn miễn phí này", "Trang này độc lập và miễn phí. Tiền ủng hộ giúp duy trì bản dịch và cập nhật thông tin. Bạn không cần ủng hộ để sử dụng trang.", "Ủng hộ qua Ko-fi"),
      "ko": ("이 무료 안내를 후원해 주세요", "ParentRight Korea는 독립적으로 운영되는 무료 사이트입니다. 후원금은 번역과 정보 업데이트에 쓰이며, 후원과 관계없이 누구나 모든 내용을 이용할 수 있습니다.", "Ko-fi로 후원하기"),
    }[lang]
    return (f'<h2>{t[0]}</h2><div class="card"><p>{t[1]}</p>'
            f'<p><a href="{KOFI_URL}" rel="noopener" target="_blank" style="display:inline-block;background:var(--accent);color:#fff;padding:10px 18px;border-radius:10px;text-decoration:none;font-weight:600">{t[2]} ☕</a></p></div>')

PAGES = [
    ("en", "/", "index.html", "Find Your Child's Korean Father Legally | ParentRight Korea", "How mothers abroad can prove paternity in a Korean court, claim child support from a Korean father, and secure Korean nationality for their child. Free help listed.", EN_HOME, EN_NAV),
    ("en", "/find-help.html", "find-help.html", "Where to Get Help in Korea: Child Support & Paternity | ParentRight Korea", "Answer 6 questions to see which Korean offices, legal aid and organizations can help you claim paternity and child support from a Korean father.", EN_FIND, EN_NAV),
    ("en", "/philippines.html", "philippines.html", "Kopino Child Support & Paternity Guide | ParentRight Korea", "Filipino mothers of Kopino children: Korean court cases that worked, organizations that help, and documents to prepare.", EN_PH, EN_NAV),
    ("en", "/vietnam.html", "vietnam.html", "Vietnamese Mothers: Korean Father Child Support | ParentRight Korea", "Vietnamese mothers whose child's Korean father disappeared: legal steps in Korea, free Vietnamese-language help, documents.", EN_VN, EN_NAV),
    ("en", "/about.html", "about.html", "About & Privacy | ParentRight Korea", "What ParentRight Korea does and never does: no personal information about anyone, no legal advice, no paid referrals.", EN_ABOUT, EN_NAV),
    ("vi", "/vi/", "vi/index.html", "Tìm bố người Hàn của con một cách hợp pháp | ParentRight Korea", "Hướng dẫn cho mẹ Việt Nam: xác nhận cha con tại tòa án Hàn Quốc, yêu cầu tiền cấp dưỡng và quốc tịch Hàn Quốc cho con. Hỗ trợ miễn phí bằng tiếng Việt.", VI_HOME, VI_NAV),
    ("ko", "/ko/", "ko/index.html", "한국인 아버지 인지청구·양육비 안내 | ParentRight Korea", "해외에서 한국인 아버지와 연락이 끊긴 아이를 위한 인지청구, 양육비 청구, 국적취득 절차와 무료 지원기관 안내.", KO_HOME, KO_NAV),
]

os.makedirs("site/vi", exist_ok=True); os.makedirs("site/ko", exist_ok=True)
for lang, path, fn, title, desc, body, nav in PAGES:
    with open(f"site/{fn}", "w", encoding="utf-8") as f:
        body = body.replace('{{SUPPORT_EN}}', support_block('en')).replace('{{SUPPORT_VI}}', support_block('vi')).replace('{{SUPPORT_KO}}', support_block('ko')).replace('{{DONATION_PRIVACY}}', 'Donations are handled entirely by Ko-fi and PayPal; we never see card details.' if KOFI_URL else '')
        html = page(lang, path, title, desc, body, nav).replace('href="/', f'href="{PREFIX}/')
        f.write(html)

with open("site/robots.txt", "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
with open("site/sitemap.xml", "w") as f:
    urls = "".join(f"<url><loc>{BASE}{p[1]}</loc></url>" for p in PAGES)
    f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
with open("site/_headers", "w") as f:
    f.write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n")
open("site/.nojekyll","w").close()
print("built", len(PAGES), "pages")
