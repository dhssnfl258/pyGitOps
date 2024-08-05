#!/bin/bash

# 스크립트 실행을 위한 오류 처리
set -e

# 프로젝트 디렉토리 설정 (예시로 현재 디렉토리 사용)
PROJECT_DIR=$(pwd)

# 가상 환경 설정 (가상 환경이 필요하지 않은 경우 이 부분은 생략 가능)
VENV_DIR="$PROJECT_DIR/venv"
python3 -m venv $VENV_DIR

# 가상 환경 활성화
source $VENV_DIR/bin/activate

# 필요한 외부 라이브러리 설치
pip install -r requirements.txt

# pyinstaller 설치
pip install pyinstaller

# 파이썬 스크립트를 실행 파일로 패키징
pyinstaller --onefile your_script.py

# 빌드된 실행 파일을 출력 디렉토리로 복사 (예: dist 디렉토리)
BUILD_OUTPUT_DIR="$PROJECT_DIR/build_output"
mkdir -p $BUILD_OUTPUT_DIR
cp dist/your_script $BUILD_OUTPUT_DIR/

# 가상 환경 비활성화
deactivate

# 빌드 완료 메시지
echo "Build and packaging completed successfully. Executable is located in $BUILD_OUTPUT_DIR"
