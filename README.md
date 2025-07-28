# 📝 Letters - 익명 편지 플랫폼 ✉️

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)

## 🌟 프로젝트 소개

**Letters**는 익명으로 마음을 전달할 수 있는 편지 플랫폼입니다. Django Framework를 사용하여 구현되었으며, 사용자들이 안전하고 편리하게 익명 편지를 주고받을 수 있도록 설계되었습니다.

### 🎯 주요 목표
- 익명성 보장을 통한 안전한 소통 환경 제공
- 직관적이고 감성적인 사용자 인터페이스 구현
- 개인 편지함을 통한 체계적인 편지 관리
- 모바일 친화적인 반응형 디자인

### ✨ 핵심 특징
- **완전한 익명성**: 로그인 없이도 편지 작성 가능
- **개인 URL 시스템**: 각 사용자별 고유한 편지함 URL 제공
- **해시 ID 보안**: 편지 ID를 해시화하여 임의 접근 예방
- **실시간 알림**: 편지함 상태를 시각적으로 표시
- **모던 UI/UX**: 감성적이고 직관적인 인터페이스

## 📸 스크린샷
| **메인 화면(로그인O)** | **내 편지함** | **편지 상세보기** |
|:---:|:---:|:---:|
| <img width="270" alt="main" src="https://github.com/user-attachments/assets/aa69d563-0715-49cd-a379-ca1be456a699" > | <img width="270" alt="myPage" src="https://github.com/user-attachments/assets/1944702f-57d7-4836-ac90-31faab02a2a0" > | <img width="270" alt="letter_detail" src="https://github.com/user-attachments/assets/1806ec64-e3cc-4aff-b14f-9c0d823d3624" > |
| **편지 작성** | **로그인** | **회원가입** |
| <img width="270" alt="write_page" src="https://github.com/user-attachments/assets/e257d312-9d6a-4e2d-a4ce-5ca7a7d38b68" > | <img width="270" alt="login" src="https://github.com/user-attachments/assets/d967c162-b116-49c7-a9f2-79a09836ed3d" > | <img width="270" alt="signup" src="https://github.com/user-attachments/assets/6b8f47c5-5aa4-4ed5-9d1d-6b60cd2735ef" /> |

## 🚀 주요 기능

### 📮 편지 시스템
- **익명 편지 작성**: 로그인 없이 누구나 편지 작성 가능
- **편지 수신**: 개인 URL을 통해 편지 받기
- **편지함 관리**: 받은 편지들을 시간순으로 정리
- **편지 상세 보기**: 해시 ID를 통한 안전한 편지 열람

### 👥 사용자 관리
- **회원가입**: 간단한 정보로 빠른 가입
- **로그인/로그아웃**: Django 인증 시스템 활용
- **개인 URL 생성**: 회원가입 시 자동으로 고유 URL 생성
- **한국어 오류 메시지**: 사용자 친화적인 한국어 피드백

### 🔒 보안 기능
- **해시 ID**: 편지 ID를 해시화하여 직접 접근 방지
- **CSRF 보호**: Django CSRF 미들웨어 적용
- **XSS 방지**: 콘텐츠 보안 정책 적용

### 📱 UI/UX
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 최적화
- **직관적 네비게이션**: 사용자 친화적인 인터페이스

## 🛠 기술 스택

### Backend
* **Python 3.x**
* **Django 4.2.7**
* **python-dotenv 1.0.0** - 환경변수 관리

### Database
* **SQLite3** (dev)
* **PostgreSQL** (prod)

### Frontend
* **HTML5/CSS3**
* **JavaScript (Vanilla)**

### 배포 및 서버
* **Gunicorn 21.2.0** (WSGI 서버)
* **WhiteNoise 6.6.0** (정적 파일 서빙)

## 📂 프로젝트 구조

```
letters/
├── mysite/                  # Django 프로젝트 설정 디렉토리
│   ├── __init__.py
│   ├── settings.py         # 프로젝트 설정
│   ├── urls.py            # 메인 URL 설정
│   ├── wsgi.py            # WSGI 설정
│   └── asgi.py            # ASGI 설정
├── letters/               # 메인 앱 (편지 관련 기능)
│   ├── migrations/        # 데이터베이스 마이그레이션
│   ├── templates/letters/ # 템플릿 파일들
│   ├── models.py         # 데이터 모델 (User, Letter, LetterCase)
│   ├── views.py          # 뷰 로직
│   ├── forms.py          # 폼 정의
│   ├── urls.py           # URL 패턴
│   ├── utils.py          # 유틸리티 함수
│   └── admin.py          # 관리자 설정
├── accounts/              # 계정 관리 앱
│   ├── templates/accounts/# 인증 관련 템플릿
│   ├── views.py          # 회원가입, 로그인 뷰
│   ├── forms.py          # 사용자 폼
│   └── urls.py           # 인증 URL 패턴
├── static/               # 정적 파일
│   ├── css/style.css     # 메인 스타일시트
│   ├── fonts/           # 폰트 파일
│   └── img/             # 이미지 파일
├── templates/           # 공통 템플릿
│   └── base.html        # 기본 템플릿
├── requirements.txt     # Python 의존성
├── manage.py           # Django 관리 스크립트
└── create_database.sql # 데이터베이스 생성 스크립트
```

## 🚀 향후 개선 계획

* **알림 시스템**: 새 편지 도착 시 이메일 알림
