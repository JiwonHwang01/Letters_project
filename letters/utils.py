import uuid
import base64
import codecs
import hashlib
from django.conf import settings

def generate_random_slug_code(length=12):
    """
    UUID 기반으로 랜덤한 URL-safe 문자열 생성 (우편함 URL용)
    """
    code = base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]
    return code

def generate_letter_hash_id(letter_id, length=16):
    """
    편지 ID를 기반으로 해시 ID 생성
    보안을 위해 SECRET_KEY와 함께 해싱
    """
    secret_key = getattr(settings, 'SECRET_KEY', 'default-secret')
    
    # 편지 ID와 SECRET_KEY를 조합하여 해시 생성
    hash_input = f"{letter_id}-{secret_key}-letter"
    hash_object = hashlib.sha256(hash_input.encode())
    hex_digest = hash_object.hexdigest()
    
    # 첫 번째 길이만큼만 사용 (기본 16자리)
    return hex_digest[:length]

def generate_user_slug_code(length=12, existing_codes_checker=None):
    """
    사용자 우편함 URL 생성 (중복 확인 포함)
    existing_codes_checker: 중복 확인 함수 (예: lambda code: User.objects.filter(lettercase_url=code).exists())
    """
    from letters.models import User
    
    if existing_codes_checker is None:
        existing_codes_checker = lambda code: User.objects.filter(lettercase_url=code).exists()
    
    code = None
    max_attempts = 10  # 무한 루프 방지
    attempts = 0
    
    while (not code or existing_codes_checker(code)) and attempts < max_attempts:
        code = generate_random_slug_code(length)
        attempts += 1
    
    if attempts >= max_attempts:
        # 최대 시도 횟수 도달 시 더 긴 코드 생성
        code = generate_random_slug_code(length + 4)
    
    return code

def verify_letter_hash_id(hash_id, letter_id):
    """
    편지 해시 ID 검증
    """
    expected_hash = generate_letter_hash_id(letter_id)
    return hash_id == expected_hash 