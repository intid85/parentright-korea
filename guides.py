# Guide articles for /guides/. Newest last; build.py lists them newest first.
# Rules for adding one: docs/guide-writing-rules.md. Topic queue: docs/guide-topics.md.
#
# Each guide:
#   slug     - URL name, lowercase-with-dashes (page is /guides/<slug>.html)
#   date     - publish date, YYYY-MM-DD
#   title    - page title (no site name; build.py appends it)
#   desc     - one-sentence meta description, under 160 characters
#   body     - HTML fragment. Images live in assets/guides/<slug>/ and are
#              referenced as <figure><img src="/assets/guides/<slug>/1.svg" alt="..."><figcaption>...</figcaption></figure>
#   sources  - list of (label, url) that back every fact and number in the body
#   checked  - date the sources were last checked, YYYY-MM-DD

GUIDES = [
    {
        "slug": "first-week-after-contact-stops",
        "date": "2026-11-03",
        "checked": "2026-11-03",
        "title": "Your child's Korean father stopped answering: what to do in the first week",
        "desc": "Five calm, practical steps for the first week after a Korean father cuts contact: save evidence, protect yourself, and find free help.",
        "body": """
<p>When messages stop being read and calls go unanswered, it is easy to panic or to want to tell the whole world. This guide is about the first week: small, safe steps that keep every legal option open for your child.</p>
<div class="note"><strong>Your child's rights do not expire because he went silent.</strong> Under Korean law, a child (or the mother as legal representative) can ask a Korean family court to recognize the father, and that right cannot be given up by agreement. It does not depend on whether he still answers you.</div>

<h2>1. Do not delete anything, and do not argue</h2>
<figure><img src="/assets/guides/first-week-after-contact-stops/1.jpg" alt="A phone lying face down on a table beside two cups of tea" loading="lazy"><figcaption>Put the phone down before you send an angry message. Everything you have now may become evidence.</figcaption></figure>
<p>Old chats, photos and voice messages are often the strongest proof that you had a relationship and that he knew about the child. Do not delete chats, even painful ones, and do not "unsend" your own messages. If he blocks you, the history usually stays on your phone, so keep it.</p>
<p>Avoid long arguments or threats. Messages you send can be read by a court too.</p>

<h2>2. Make two copies of your evidence</h2>
<figure><img src="/assets/guides/first-week-after-contact-stops/2.jpg" alt="A cloud shape above a USB stick" loading="lazy"><figcaption>One copy on your phone is not enough. Phones get lost, broken or reset.</figcaption></figure>
<p>Save screenshots and exports in two places, for example a cloud account only you can open and a USB stick or a second phone. Collect:</p>
<ul>
<li>His full name (in Korean letters if you have it), date of birth, and any ID or passport details he gave you</li>
<li>His phone numbers and accounts (KakaoTalk, LINE, Facebook, Instagram, Zalo) and the date each one stopped working</li>
<li>Messages, photos of you together, travel dates and money transfers he sent</li>
<li>Pregnancy and hospital records, especially if he came with you</li>
<li>Your child's birth certificate</li>
</ul>
<p class="small">You do not need his address to start. These details help legal aid and the court find him through official channels.</p>

<h2>3. Keep it private: do not post his name or photo</h2>
<figure><img src="/assets/guides/first-week-after-contact-stops/3.jpg" alt="A closed folder with a padlock on it" loading="lazy"><figcaption>Your evidence belongs in a court file, not on social media.</figcaption></figure>
<p>It is tempting to post his face in "find the father" groups. Please don't. In Korea, publicly stating even true facts that damage someone's reputation can be a crime under Article 307(1) of the Criminal Act, punishable by up to 2 years in prison or a fine of up to 5 million won. Posting also warns him, can make him hide money, and can be used against you in court.</p>
<p>Be careful of anyone who offers to "find the father" for a fee paid in advance. Real legal aid and support groups do not ask for large upfront payments.</p>

<h2>4. Talk to free help in your language</h2>
<figure><img src="/assets/guides/first-week-after-contact-stops/4.jpg" alt="A telephone headset on a desk between two houseplants" loading="lazy"><figcaption>Free counselling is available in Tagalog, Vietnamese, English and other languages.</figcaption></figure>
<ul>
<li><strong>Danuri Helpline 1577-1366</strong> (Korea): open 24 hours, 365 days, in 13 languages including English, Tagalog and Vietnamese. It is for migrants and multicultural families in Korea, but family or friends in Korea can call for information.</li>
<li><strong>Korea Legal Aid Corporation 132</strong> (Korea): free or low-cost legal help for people with household income at or below 125% of the national median income, including foreign residents of Korea.</li>
<li><strong>The Korean embassy or consulate</strong> in your country: ask about family-registration paperwork. Korean embassies accept family-registration reports from Koreans abroad.</li>
</ul>
<p>Not sure which fits you? Answer 6 questions on <a href="/find-help.html">Find help</a>. Your answers stay in your browser.</p>

<h2>5. Know the two roads ahead</h2>
<figure><img src="/assets/guides/first-week-after-contact-stops/5.jpg" alt="A winding path through green fields toward a distant city at sunrise" loading="lazy"><figcaption>Most cases take one of two roads. You do not have to choose this week.</figcaption></figure>
<ul>
<li><strong>If he answers again:</strong> he can recognize the child voluntarily by filing an acknowledgment report (임의인지). This is the fastest and cheapest route.</li>
<li><strong>If he stays silent or refuses:</strong> the child, or you as legal representative, can file a case for acknowledgment in the Korean family court where he lives, usually together with a claim for child support. If he denies being the father, the court can order a DNA test.</li>
</ul>
<p>Both roads are explained in the <a href="/#steps">6 steps</a>.</p>

<h2>Your first-week checklist</h2>
<div class="card"><ul style="margin:0">
<li>Nothing deleted, no angry messages sent</li>
<li>Evidence saved in two places</li>
<li>Nothing posted about him online</li>
<li>One call made to free help (Danuri, legal aid or the embassy)</li>
<li>Read the 6 steps once, slowly</li>
</ul></div>
""",
        "sources": [
            ("Civil Act Art. 863-864: suit for acknowledgment (summary)", "https://korea.legal/wiki/%EC%9D%B8%EC%A7%80%EC%B2%AD%EA%B5%AC%EC%9D%98-%EC%86%8C/"),
            ("Supreme Court 2001Meu1353: the right to acknowledgment cannot be waived (summary)", "https://korea.legal/wiki/2001%eb%af%801353/"),
            ("Family Litigation Act Art. 26: court where the father lives (summary)", "https://korea.legal/wiki/%ea%b0%80%ec%82%ac%ec%86%8c%ec%86%a1%eb%b2%95-%ec%a0%9c26%ec%a1%b0/"),
            ("Family Litigation Act Art. 67: DNA test orders and sanctions (summary)", "https://korea.legal/wiki/%ea%b0%80%ec%82%ac%ec%86%8c%ec%86%a1%eb%b2%95-%ec%a0%9c67%ec%a1%b0/"),
            ("Criminal Act Art. 307(1): defamation by stating facts", "https://www.nepla.ai/wiki/형사/명예-신용범죄/사실적시-명예훼손죄-형법-제307조-제1항-jxm9lpj4npgr"),
            ("Danuri Helpline hours and languages (Ministry of Gender Equality and Family)", "https://www.mogef.go.kr/cc/dcc/cc_dcc_f001.do"),
            ("Korea Legal Aid eligibility: 125% of median income, including foreign residents", "https://www.index.go.kr/unify/idx-info.do?idxCd=2479"),
            ("Family registration reports at Korean embassies (Act Art. 20, Rules Art. 40)", "https://korea.legal/wiki/%ea%b0%80%ec%a1%b1%ea%b4%80%ea%b3%84%ec%9d%98-%eb%93%b1%eb%a1%9d-%eb%93%b1%ec%97%90-%ea%b4%80%ed%95%9c-%ea%b7%9c%ec%b9%99-%ec%a0%9c40%ec%a1%b0/"),
        ],
    },
]
