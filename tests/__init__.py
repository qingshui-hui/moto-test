import os
from pathlib import Path

# pytnamodbの設定を上書き
os.environ["PYNAMODB_CONFIG"] = str(Path(__file__).parent.joinpath("pynamodb_settings.py"))

os.environ["AWS_DEFAULT_REGION"] = "ap-northeast-1"

