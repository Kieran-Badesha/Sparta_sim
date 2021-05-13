@echo off
if exist venv\ (
  echo ok
) else (
  python -m venv venv
)
CALL venv\Scripts\activate.bat
cd sparta_sim
python -m pip --disable-pip-version-check install . -q
python -m runsim
pause