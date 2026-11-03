# ParentRight Korea — 프로젝트 노트

해외(필리핀·베트남 등)에 사는 엄마가 아이의 한국인 아버지에게 **인지(친자 인정)·양육비·국적**을 합법적으로 청구할 수 있도록 공식 절차와 지원기관을 안내하는 정보 사이트.

- 사이트: https://parentright.org (Cloudflare Pages 프로젝트 `parentright-korea`, main 푸시 시 자동 배포. 미리보기 https://parentright-korea.pages.dev)
- 도메인: Cloudflare Registrar에서 2026-11-03 구매, 1년, 자동 갱신 $11.20/년
- 언어: 영어(메인), 베트남어(/vi/), 타갈로그어(/tl/), 한국어(/ko/)
- 연락처: contact@parentright.org (Cloudflare Email Routing → 운영자 Gmail로 전달, 수신 전용). 사이트의 "Found a mistake?" 안내에 표시
- 가이드: /guides/ — 매달 1일·15일 10시 예약 작업 `parentright-guide-writer`(Claude 앱, Auto 모드)가 다음 글감을 써서 자동 게시. 첫 글 2026-11-03
- 이미지 생성: Cloudflare Workers AI(FLUX.1 schnell). 토큰은 Windows 사용자 환경 변수 `CLOUDFLARE_AI_TOKEN`, 계정 ID는 `CLOUDFLARE_ACCOUNT_ID` (저장소에 저장하지 않음)
- 후원: https://ko-fi.com/intid85 (표시 이름 ParentRight Korea, PayPal 연결, USD, 최소 $5)

## 운영 원칙 (법적 안전장치)

- 특정 개인의 이름·사진·연락처 등 어떤 정보도 게시하지 않는다 (명예훼손·개인정보보호법 위험).
- 게시판·댓글·업로드·이름 입력란을 만들지 않는다.
- "Find help" 질문 답변은 브라우저 안에서만 처리, 서버 전송·저장 없음.
- 법률 자문을 하지 않는다. 모든 페이지에 "general information, not legal advice" 표시.
- 대가를 받고 변호사를 소개하지 않는다 (변호사법 위반). 건당·성공보수형 제휴 금지.
- 후원은 선택이며 법률 서비스나 우선권을 사는 것이 아니라고 명시.
- 도움 찾기 페이지·국가별 페이지에는 후원 버튼을 넣지 않는다.

## 수익 방향 (결정)

- 후원: Ko-fi + PayPal (Buy Me a Coffee는 Stripe 전용 정산이라 한국에서 사용 어려움, Stripe도 한국 미지원).
- 번역: 출생증명서·판결문 공증 번역 제휴 — 사이트에는 "Coming soon"으로 표시, 제휴처 미정.
- Work Route 사이트와는 서로 링크를 걸지 않는다.

## 사이트 구조

| 파일 | 내용 |
|---|---|
| `index.html` | 영어 홈: 6단계 절차, 무료 지원기관, 후원 |
| `find-help.html` | 6개 질문 → 상황별 추천 기관 (클라이언트 JS) |
| `philippines.html`, `vietnam.html` | 국가별 안내 |
| `about.html` | 운영 원칙·개인정보 |
| `vi/index.html`, `tl/index.html`, `ko/index.html` | 베트남어·타갈로그어·한국어판 |
| `guides/` | 가이드 글 (생성물). 원본은 `guides.py` |
| `guides.py` | 가이드 글 목록 (제목, 본문, 출처, 날짜) |
| `assets/guides/<slug>/` | 가이드 이미지 5장 (Workers AI 생성) |
| `tools/gen_image.py` | 이미지 생성 스크립트 |
| `docs/guide-writing-rules.md`, `docs/guide-topics.md` | 가이드 작성 규칙과 글감 목록 (예약 작업이 따름) |
| `docs/outreach-posts.md` | 커뮤니티·단체 홍보 글 초안 |
| `build.py` | 모든 페이지 생성 스크립트 (내용 수정은 여기서) |
| `assets/logo.png` | 로고 (Ko-fi 프로필과 동일, 시안 1번) |
| `assets/brand/` | 로고 시안 5개와 비교 이미지 |

### 수정 방법

1. `build.py` 내용 수정
2. `python3 build.py` → `site/` 폴더 생성
3. `site/` 안의 파일을 저장소 루트로 복사하고 `site/` 삭제
4. 커밋·푸시 (Cloudflare Pages가 main 브랜치 루트를 자동 배포)

Cloudflare Pages는 `/x.html`을 `/x`로 넘기므로 canonical·sitemap은 확장자 없는 주소를 씀(`build.py`의 `clean()`).

`build.py` 맨 위 설정값:
- `PREFIX` — 하위 경로. 자체 도메인 루트에서 서비스하므로 `""`.
- `BASE` — 사이트 기준 주소 (canonical, sitemap에 사용).
- `KOFI_URL` — 비워두면 후원 버튼이 사라짐.
- `CONTACT_EMAIL` — 비워두면 오류 제보 안내가 사라짐.

## 조사한 법적 근거 (2026-11 기준)

- 민법 제863조: 자녀·법정대리인이 부를 상대로 인지청구의 소 제기.
- 가사소송법 제26조 제2항: 상대방 주소지 가정법원 전속관할. 제50조: 조정전치.
- 가사소송법 제29조: 유전자 수검명령. 제67조: 불응 시 1천만원 이하 과태료, 재차 불응 시 30일 이내 감치.
- 인지청구권은 포기 불가(대법원 2001므1353). 부 사망 시 사망을 안 날부터 2년 내 검사를 상대로.
- 해외에서 검체를 채취해 법원 지정 국내 기관으로 보내 인지판결을 받은 사례 있음(우즈베키스탄 여성 사건).
- 2014 서울가정법원: 필리핀 거주 코피노 2명 첫 친자 인정(이투데이 보도). 이후 월 30만원 양육비 판결 보도 확인. "월 50만원", "과거 양육비 2천만원"은 출처 미확인이라 2026-11-03 사이트에서 삭제.
- 국적법 제3조: 한국인 부에게 인지된 미성년 자녀는 출생 당시 부가 국민이었으면 법무부장관 신고로 국적 취득.
- 양육비이행법 제21조의4: 지급명령·이행명령 불이행 시 성평등가족부장관이 양육비이행심의위원회 심의를 거쳐 출국금지 요청 가능(2025-10 개정 반영). 양육비이행관리원 1644-6621. 해외 거주 신청인 접수 여부는 **미확인**(사이트에 "확인하라"로 표시).
- 대한법률구조공단 132: 중위소득 125% 이하 국민·국내 거주 외국인.
- 다누리콜센터 1577-1366: 24시간 13개 언어(영어·베트남어·타갈로그어 포함), 화요일 변호사 상담 예약.
- 2007 헤이그 양육비협약: 필리핀은 2022-10-01 발효로 당사국, 한국·베트남은 비당사국(HCCH 현황표, 2026-09-16 갱신분 기준). 예전 노트의 "필리핀 비당사국"은 틀렸음.
- 아포스티유 협약: 한국·필리핀(2019-05-14) 당사국, 베트남도 2026-09-11 발효로 당사국(HCCH 현황표).
- 2026-11-03 사이트 사실관계 점검: 법조문(민법 863·864, 가사소송법 26·29·50·67, 국적법 3), 2001므1353, 법률구조공단 기준, 다누리 언어는 일치 확인.
- 지원단체: We Love Kopino(WLK), Kopino Children Association.

## 남은 일

- [x] Cloudflare에서 도메인 구매 (parentright.org)
- [x] Cloudflare Pages로 호스팅 이전 (이 저장소 연결, 빌드 명령 없음, 출력 디렉터리 루트)
- [x] 도메인 연결 후 `build.py`의 `PREFIX = ""`, `BASE = "https://parentright.org"`으로 바꾸고 재빌드
- [x] GitHub Pages 끄기 (2026-11-03)
- [x] Ko-fi 프로필 Website 주소를 새 도메인으로 변경
- [x] Google Search Console 등록(도메인 속성, DNS TXT 인증), sitemap 제출 (2026-11-03). Cloudflare DNS의 google-site-verification TXT는 지우지 말 것
- [x] 오류 제보 메일(contact@parentright.org) 전달 설정, 출처 목록 추가 (2026-11-03)
- [x] 가이드 섹션과 2주 자동 게시 설정 (2026-11-03)
- [ ] contact@parentright.org로 시험 메일을 보내 Gmail 수신 확인
- [ ] 11-15 첫 자동 가이드 게시 결과 확인
- [ ] 홍보: docs/outreach-posts.md 초안으로 지원단체·페이스북 그룹에 공유 (운영자가 직접)
- [ ] 양육비이행관리원이 해외 거주 신청인을 받는지 확인
- [ ] (선택) Gmail에서 contact@ 주소로 보내기 설정, 방문 통계(Cloudflare Web Analytics, 켤 때 About의 개인정보 문구 먼저 수정)
- [ ] 베트남어판 원어민 검수
- [ ] 타갈로그어판(/tl/) 원어민 검수 (2026-11-03 검수 없이 게시하기로 결정)
- [ ] 번역 제휴처 확정 후 "Coming soon" 교체
- [ ] (나중에) Ko-fi 목표(Goal)·첫 게시물 작성
