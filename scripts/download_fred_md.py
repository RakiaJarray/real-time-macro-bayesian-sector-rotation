
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone

# Official FRED-MD source
URL = (
    "https://www.stlouisfed.org/-/media/project/frbstl/"
    "stlouisfed/research/fred-md/monthly/current.csv"
)

# Repository root and destination
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "raw" / "fred_md"
OUTPUT_FILE = OUTPUT_DIR / "fred_md_current.csv"

def download_fred_md():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading FRED-MD...")

    with urlopen(URL, timeout=60) as response:
        content = response.read()

    if not content:
        raise ValueError("Downloaded file is empty.")

    # Basic CSV validation
    first_line = content.decode("utf-8-sig").splitlines()[0]
    if "sasdate" not in first_line.lower():
        raise ValueError("Unexpected FRED-MD CSV format.")

    OUTPUT_FILE.write_bytes(content)

    print(f"Download successful: {OUTPUT_FILE}")
    print(f"File size: {len(content):,} bytes")
    print(
        "Downloaded at:",
        datetime.now(timezone.utc).isoformat()
    )

if __name__ == "__main__":
    download_fred_md()

