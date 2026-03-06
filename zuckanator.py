# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Taha Janibek
# 2026 🄯 Zuckanator

"""
Zuckanator v3.1 — Instagram Profile Photo
Dev: github.com/tahajanibek
API: instagram120 (RapidAPI) — multi-endpoint fallback
"""

import os, sys, json, shutil, re, requests
from pathlib import Path
from datetime import datetime

def install(pkg):
    import subprocess
    subprocess.check_call([sys.executable,"-m","pip","install",pkg,"--break-system-packages","-q"])

try: import requests
except ImportError: install("requests"); import requests

try: import pyfiglet
except ImportError: install("pyfiglet"); import pyfiglet

class C:
    RED="\033[91m"; GREEN="\033[92m"; YELLOW="\033[93m"; BLUE="\033[94m"
    MAGENTA="\033[95m"; CYAN="\033[96m"; WHITE="\033[97m"; GRAY="\033[90m"
    BOLD="\033[1m"; DIM="\033[2m"; RESET="\033[0m"

ANSI = re.compile(r'\033\[[0-9;]*m')
def vlen(s): return len(ANSI.sub('', s))
def tw(): return shutil.get_terminal_size((80,24)).columns
def sep(): print(f"{C.GRAY}{'─'*tw()}{C.RESET}")

BIG = [
    "███████╗██╗   ██╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗",
    "╚══███╔╝██║   ██║██╔════╝██║ ██╔╝██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
    "  ███╔╝ ██║   ██║██║     █████╔╝ ███████║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝",
    " ███╔╝  ██║   ██║██║     ██╔═██╗ ██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗",
    "███████╗╚██████╔╝╚██████╗██║  ██╗██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║",
    "╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝",
]
BIG_W = max(len(l) for l in BIG)

def make_logo(w):
    if w >= BIG_W + 2: return BIG
    for font in ["small", "smslant", "mini", "term"]:
        try:
            lines = pyfiglet.figlet_format("Zuckanator", font=font).strip().splitlines()
            if lines and max(len(l) for l in lines) <= w - 2:
                return lines
        except: pass
    return ["Zuckanator"]

def print_banner():
    os.system("clear" if os.name=="posix" else "cls")
    w = tw()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    logo = make_logo(w)
    pad  = max(0, (w - max(len(l) for l in logo)) // 2)
    print()
    for line in logo:
        print(f"{' '*pad}{C.MAGENTA}{C.BOLD}{line}{C.RESET}")
    print()
    for text in [
        f"{C.CYAN}Zuckanator v3.1{C.RESET}  {C.GRAY}│{C.RESET}  Instagram Profile Photo HD Extractor",
        f"{C.CYAN}Dev{C.RESET}  {C.GRAY}│{C.RESET}  github.com/tahajanibek",
        f"{C.GRAY}{'─'*40}{C.RESET}",
        f"{C.DIM}{now}{C.RESET}",
    ]:
        p = max(0, (w - vlen(text)) // 2)
        print(f"{' '*p}{text}")
    print()

SCRIPT_DIR  = Path(__file__).parent.resolve()
CONFIG_FILE = SCRIPT_DIR / "zuckanator_config.json"

def load_config():
    if CONFIG_FILE.exists():
        try: return json.loads(CONFIG_FILE.read_text())
        except: pass
    return {}

def save_config(data):
    CONFIG_FILE.write_text(json.dumps(data, indent=2))

def fetch_user(username, api_key):
    headers_base = {
        "x-rapidapi-key" : api_key,
        "x-rapidapi-host": "instagram120.p.rapidapi.com",
        "Content-Type"   : "application/json",
    }
    attempts = [
        lambda: requests.post(
            "https://instagram120.p.rapidapi.com/api/instagram/userInfo",
            headers=headers_base,
            json={"username": username},
            timeout=20
        ),
        lambda: requests.post(
            "https://instagram120.p.rapidapi.com/api/instagram/profile",
            headers=headers_base,
            json={"username": username},
            timeout=20
        ),
        lambda: requests.get(
            "https://instagram120.p.rapidapi.com/api/instagram/user",
            headers={**headers_base, "Content-Type": "application/json"},
            params={"username": username},
            timeout=20
        ),
        lambda: requests.post(
            "https://instagram120.p.rapidapi.com/api/instagram/posts",
            headers=headers_base,
            json={"username": username, "nextMaxId": ""},
            timeout=20
        ),
    ]

    last_err = None
    for i, attempt in enumerate(attempts, 1):
        try:
            print(f"  {C.GRAY}    [{i}/{len(attempts)}] endpoint deneniyor...{C.RESET}", end="\r")
            r = attempt()
            if r.status_code == 200:
                data = r.json()
                user = None
                if isinstance(data, dict):
                    result = data.get("result", [])
                    if isinstance(result, list) and result:
                        u = result[0]
                        user = u.get("user", u)
                    else:
                        user = data.get("user", data)
                if user and ("pk" in user or "profile_pic_url" in user):
                    print(f"  {C.GREEN}    [✓] Bağlantı başarılı (endpoint {i}){C.RESET}      ")
                    return user
            last_err = f"HTTP {r.status_code}"
        except Exception as e:
            last_err = str(e)

    raise Exception(f"Tüm endpointler başarısız. Son hata: {last_err}")

def extract_photos(user):
    photos, seen = [], set()
    def add(url, label):
        if url and url not in seen:
            seen.add(url); photos.append({"index":len(photos)+1,"url":url,"label":label})

    hd = user.get("hd_profile_pic_url_info",{})
    if isinstance(hd, dict) and hd.get("url"):
        add(hd["url"], f"Profile Photo #1  [{hd.get('width','?')}x{hd.get('height','?')}] ★ HD")

    for v in user.get("hd_profile_pic_versions",[]):
        n = len(photos)+1
        add(v.get("url",""), f"Profile Photo #{n}  [{v.get('width','?')}x{v.get('height','?')}]")

    add(user.get("profile_pic_url",""), f"Profile Photo #{len(photos)+1}  [150x150] Standard")
    return photos

def extract_info(user):
    return {
        "full_name"   : user.get("full_name","—"),
        "bio"         : (user.get("biography","") or "").replace("\n"," "),
        "user_id"     : user.get("pk","—"),
        "followers"   : user.get("follower_count",0),
        "following"   : user.get("following_count",0),
        "posts"       : user.get("media_count",0),
        "is_private"  : user.get("is_private",False),
        "is_verified" : user.get("is_verified",False),
        "external_url": user.get("external_url",""),
    }

def get_size(url):
    try:
        r = requests.head(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=8)
        s = int(r.headers.get("content-length",0))
        return f"{s/1024:.1f} KB" if s else "—"
    except: return "—"

def download_photo(url, filepath):
    r = requests.get(url, headers={"User-Agent":"Mozilla/5.0","Referer":"https://www.instagram.com/"},
                     timeout=30, stream=True)
    r.raise_for_status()
    total = int(r.headers.get("content-length",0))
    done  = 0
    with open(filepath,"wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk); done += len(chunk)
            if total:
                pct = done/total*100
                bar = "█"*int(pct/5)+"░"*(20-int(pct/5))
                print(f"\r    {C.CYAN}[{bar}] {pct:5.1f}%{C.RESET}", end="", flush=True)
    print(); return done

def main():
    print_banner()

    cfg     = load_config()
    api_key = cfg.get("rapidapi_key","")

    if not api_key:
        print(f"  {C.YELLOW}RapidAPI Key (instagram120):{C.RESET} ", end="")
        api_key = input().strip()
        if not api_key:
            print(f"  {C.RED}[✗] Key girilmedi!{C.RESET}"); sys.exit(1)
        cfg["rapidapi_key"] = api_key
        save_config(cfg)
        print(f"  {C.GREEN}[✓] Key kaydedildi → {CONFIG_FILE}{C.RESET}\n")
    else:
        print(f"  {C.GREEN}[✓] API Key yüklendi{C.RESET}\n")

    sep()
    print(f"\n  {C.YELLOW}Target username (@'siz): {C.RESET}", end="")
    username = input().strip().lstrip("@")
    if not username:
        print(f"  {C.RED}[✗] Kullanıcı adı girilmedi!{C.RESET}"); sys.exit(1)

    print(f"\n  {C.CYAN}[~] Scanning @{username} ...{C.RESET}\n")

    try:
        user = fetch_user(username, api_key)
    except Exception as e:
        print(f"\n  {C.RED}[✗] {e}{C.RESET}")
        print(f"  {C.YELLOW}    → instagram120 şu an çevrimdışı olabilir, biraz bekleyin.{C.RESET}")
        sys.exit(1)

    info   = extract_info(user)
    photos = extract_photos(user)

    sep()
    print(f"\n  {C.MAGENTA}{C.BOLD}TARGET  {C.RESET}{C.WHITE}@{username}{C.RESET}\n")
    for label, val in [
        ("Full Name", info["full_name"]),
        ("Bio",       info["bio"][:72] or "—"),
        ("User ID",   str(info["user_id"])),
        ("Followers", f"{info['followers']:,}"),
        ("Following", f"{info['following']:,}"),
        ("Posts",     str(info["posts"])),
        ("Private",   "🔒 Yes" if info["is_private"] else "🌐 No"),
        ("Verified",  "✓ Yes" if info["is_verified"] else "✗ No"),
        ("URL",       info["external_url"] or "—"),
    ]:
        print(f"  {C.GRAY}│{C.RESET}  {C.WHITE}{label:<12}{C.RESET}  {C.DIM}{val}{C.RESET}")
    print(); sep()

    print()
    if not photos:
        print(f"  {C.RED}[✗] Profil fotoğrafı bulunamadı!{C.RESET}\n"); return

    count = len(photos)
    print(f"  {C.GREEN}{C.BOLD}[✓] {count} profil fotoğrafı bulundu!{C.RESET}\n")
    for p in photos:
        size = get_size(p["url"])
        print(f"  {C.CYAN}{C.BOLD}[{p['index']:02d}]{C.RESET}  {C.WHITE}{p['label']}{C.RESET}")
        print(f"  {C.GRAY}      Size : {size}{C.RESET}")
        print(f"  {C.BLUE}      Link : {p['url']}{C.RESET}")
        print()
    sep()

    print(f"\n  {C.YELLOW}[?] Fotoğrafları kaydet? (e/h): {C.RESET}", end="")
    if input().strip().lower() == "e":
        save_dir = SCRIPT_DIR / "zuckanator_output" / username
        save_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n  {C.CYAN}[~] İndiriliyor → {save_dir}/{C.RESET}\n")
        ok = 0
        for p in photos:
            fname = save_dir / f"{username}_pp_{p['index']:02d}.jpg"
            print(f"  {C.GRAY}[{p['index']}/{count}]{C.RESET}  {fname.name}")
            try:
                s = download_photo(p["url"], fname)
                print(f"    {C.GREEN}[✓] Kaydedildi ({s/1024:.1f} KB){C.RESET}\n")
                ok += 1
            except Exception as e:
                print(f"\n    {C.RED}[✗] Hata: {e}{C.RESET}\n")
        sep()
        print(f"\n  {C.GREEN}{C.BOLD}[✓] {ok}/{count} fotoğraf → {save_dir}/{C.RESET}")
    else:
        print(f"\n  {C.GRAY}[─] Kaydedilmedi.{C.RESET}")

    print(f"\n  {C.GRAY}Zuckanator v3.1  │  github.com/tahajanibek{C.RESET}\n")

if __name__ == "__main__":
    main()