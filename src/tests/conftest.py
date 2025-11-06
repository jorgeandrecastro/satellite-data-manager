import sys
from pathlib import Path

# ajoute le dossier src/ au path pour que pytest trouve les modules
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
